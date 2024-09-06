import schedule
import time
from datetime import datetime,timedelta
import threading
from db import Product_BDB_Transaction_Sale,Branch, Bakery, Delivery, Employee,Products,Transaction,Sale,Salary,Status,Asset,App,Account
from config import db
import warnings
from PIL import Image
import io

warnings.filterwarnings("ignore")
class dbBranch:

    totalacceptedproducts = 0
    branchtotalsaleinmonye = 0


    def __init__(self, branchname='DefaultBranch', location='DefaultLocation', 
                 controlers_id=0,totalworkers=0, branchyearsalegoal=0, 
                 branchmonthsalegoal=0, branchdaysalegoal=0, 
                 branchdayworikinghouregoal=0,branchimage=None):
        
        self.branchname = branchname
        self.location = location
        self.controlers_id = controlers_id
        self.totalworkers = totalworkers
        self.branchyearsalegoal = branchyearsalegoal
        self.branchmonthsalegoal = branchmonthsalegoal
        self.branchdaysalegoal = branchdaysalegoal
        self.branchdayworikinghouregoal = branchdayworikinghouregoal
        self.branchimage = self.convert_image_to_binary(branchimage) if branchimage else None

    #converting image in to binary
    def convert_image_to_binary(self,image_file):
        if image_file is None:
            return None
    # Load the image from the uploaded file
        image = Image.open(image_file).convert('L')
    
    # Convert the image to binary
        binary_image = image.point(lambda x: 0 if x < 128 else 255, '1')
    
    # Save the binary image to a byte stream
        binary_stream = io.BytesIO()
        binary_image.save(binary_stream, format='PNG')
        binary_stream.seek(0)
    
        return binary_stream.getvalue()

    # calculate the total accpeted products
    def setproducts(self):
        def set_totalacceptedproducts():
            branch_instance  = Branch.query.filter_by(BranchName=self.branchname).first()
            if branch_instance:
                branchid = branch_instance.BranchId
                self.totalacceptedproducts = Product_BDB_Transaction_Sale.query.filter_by(Branch_id=branchid).count()
            else:
                return 'Error:BRANCH NOT FOUND'
        schedule.every(24).hours.do(set_totalacceptedproducts)
        while True:
            schedule.run_pending()
            time.sleep(18000)
        
    #calculate the total branch sale in monye
    def setsale(self):
        def set_branchtotalsaleinmonye():
            branch_instance = Branch.query.filter_by(BranchName=self.branchname).first()
            if branch_instance:
                branchid = branch_instance.BranchId
                results = Product_BDB_Transaction_Sale.query.filter_by(Branch_id=branchid).all()
                for result in results:
                    saleid = result.Sale_id
                    sale_instance = Sale.query.filter_by(SaleId=saleid).first()
                    if sale_instance:
                        self.branchtotalsaleinmonye += sale_instance.TotalSaledMoney
            else:
                return 'Error:BRANCH NOT FOUND'
        schedule.every(24).hours.do(set_branchtotalsaleinmonye)
        while True:
            schedule.run_pending()
            time.sleep(18000)

    #insertes data in to database 
    def insert_branchdata(self):
        branchdata =Branch(BranchName=self.branchname,BranchImage=self.branchimage, Location=self.location, 
               ControllerId=self.controlers_id, TotalWorkers=self.totalworkers, TotalAcceptedProducts=self.totalacceptedproducts,
               BranchTotalSaleInMoney=self.branchtotalsaleinmonye,BranchYearSaleGoalInMoney=self.branchyearsalegoal,
               BranchMonthSaleGoalInMoney=self.branchyearsalegoal, BranchDaySaleGoalInMoney=self.branchdaysalegoal,
               BranchDayWorikingHoureGoal=self.branchdayworikinghouregoal)
        
        db.session.add(branchdata)
        db.session.commit()

    #gives branch data from database
    def output_branchdata(self):
        return Branch.query.all()
    
    #gives accepted products data form database
    def output_acceptedproductdata(self):
        branches = Branch.query.all()
        accepted_products_data = []
        now = datetime.now()
        last_24_hours = now - timedelta(hours=24)
        for branch in branches:
            trans_results = Product_BDB_Transaction_Sale.query.filter_by(Branch_id=branch.BranchId).filter(
                Product_BDB_Transaction_Sale.Time >=  last_24_hours
            ).all()
            for result in trans_results:
                product_id = result.Product_id
                product = Products.query.filter_by(ProductId=product_id).first()
                branch_last_24_sale = Sale.query.filter_by(SaleId = result.Sale_id).first()
                accepted_products_data.append(
                    {
                        'productname':product.ProductName,
                        'branchname': branch.BranchName,
                        'totalproductaccepted':product.TotalDeliveredProducts,
                        'totalproductselled': branch_last_24_sale.TotalSaledMoney,
                        'acceptedtime': result.Time,
                        'deliveryid	':result.Deliver_id,
                        'branchSalein$': branch.BranchTotalSaleInMoney
                    }
                )
        return accepted_products_data
    
    #gives monthly branch status data
    def monthly_branch_statusdata(self):
        statusdata = []
        now = datetime.now()
        last_730_hours = now - timedelta(hours=730)
        branches = Branch.query.all()
        for branch in branches:
            monthlytotalsale = 0
            monthlygoal = False
            monthly_acceptedproducts = 0
            trans_results = Product_BDB_Transaction_Sale.query.filter_by(Branch_id=branch.BranchId).filter(
                Product_BDB_Transaction_Sale.Time >=  last_730_hours
            ).all()
            for result in trans_results:
                sale =  Sale.query.filter_by(SaleId = result.Sale_id).first()
                monthly_acceptedproducts += Product_BDB_Transaction_Sale.query.filter_by(Product_id = result.Product_id).count()
                monthlytotalsale += sale.TotalSaledMoney
                goaldata = self.checker()
                for result in goaldata:
                    if branch.BranchId == result['branch_id']:
                        monthlygoal = result['monthgoal']
                        break
                    else:
                        print(f'Warning: Branch ID {branch.BranchId} does not match any goal data.')
                statusdata.append(
                    {
                        'branch_id':branch.Branchid,
                        'monthlytotalsale':monthlytotalsale,
                        'monthly_acceptedproducts':monthly_acceptedproducts,
                        'monthlygoal':monthlygoal
                        #total woriking hour will be enter in this line
                    }
                )
        return statusdata
    
    #gives year branch status data
    def year_branch_statudata(self):
        statusdata = []
        branches = Branch.query.all()
        now = datetime.now()
        last_8760_hours = now - timedelta(hours=8760)
        for branch in branches:
            totalyearsale = 0
            yeargoal = False
            totalyearacceptedproducts = 0
            trans_results = Product_BDB_Transaction_Sale.query.filter_by(Branch_id=branch.BranchId).filter(
                Product_BDB_Transaction_Sale.Time >= last_8760_hours
            ).all()
            for result in trans_results:
                sale = Sale.query.filter_by(SaleId=result.Sale_id).first()
                totalyearsale += sale.TotalSaledMoney
                totalyearacceptedproducts += Product_BDB_Transaction_Sale.query.filter_by(Proudct_id=result.Product_id).count()
                
                goaldata = self.checker()
                for result in goaldata:
                    if result['branch_id'] == branch.BranchId:
                        yeargoal = True
                        break
                    else:
                        print(f'Warning: Branch ID {branch.BranchId} does not match any goal data.')
                statusdata.append(
                    {
                        'branch_id':branch.Branchid,
                        'totalyearsale':totalyearsale,
                        'totalacceptedproduct':totalyearacceptedproducts,
                        'yeargoal':yeargoal
                        #total working hours will be in this line
                    }
                )
        return statusdata
    #gives day branch status data
    def day_branch_statusdata(self):
        statusdata = []
        branches = Branch.query.all()
        for branch in branches:
            mostdata = self.output_acceptedproductdata()
            totaldaysale = 0
            totaldayproductaccepted = 0
            for data in mostdata:
                if branch.BranchName == data['branchname']:
                    totaldaysale = data['totalproductselled']
                    totaldayproductaccepted = data['totalproductaccepted']
                    break
                else:
                   print(f'Warning: Branch ID {branch.BranchName} does not match any goal data.')
            goaldata = self.checker()
            daystatus = False
            for result in goaldata:
                if branch.BranchId == result['branch_id']:
                    daystatus = result['daygoal']
                else:
                    print(f'Warning: Branch ID {branch.BranchId} does not match any goal data.')
            statusdata.append(
                {
                    'branch_id':branch.Branchid,
                    'totaldaysale':totaldaysale,
                    'totaldayproductaccepted':totaldayproductaccepted,
                    'daygoal':daystatus
                    #day working will be enter in this line
                }
            )
        return statusdata    

    #update branch data
    def update_branchdata(self, id, co_name, value):
        branch = Branch.query.filter_by(BranchId = id).first()
        if branch:
            if hasattr(branch, co_name):
                setattr(branch, co_name, value)
                db.session.commit()
            else:
                print(f'Warning: Branch Column "{co_name}" Not Found')
        else:
            print(f'Warning: Branch With This ID {id} Not Found')
    #delete branch data 
    
    def delete_branchdata(self,id):
        branch = Branch.query.filter_by(BranchId = id).first()
        if branch:
            db.session.delete(branch)
            db.session.commit()
            print(f'Branch with ID {id} has been deleted.')
        else:
            print(f'Warning: Branch With This ID {id} Not Found')

    #checker day,month,year, sale goals
    def checker(self):
        now = datetime.now()
        last_24_hours = now - timedelta(hours=24)
        branchs = Branch.query.all()
        checker_status_data = []
        for branch in branchs:
            totaldaysale = 0
            trans_results = Product_BDB_Transaction_Sale.query.filter_by(Branch_id=branch.BranchId).filter(
                Product_BDB_Transaction_Sale.Time >=  last_24_hours
            ).all()
            for result in trans_results:
                sale =  Sale.query.filter_by(SaleId = result.Sale_id).first()
                totaldaysale += sale.TotalSaledMoney
            daygoal =  totaldaysale >= self.branchdaysalegoal
            monthgoal = totaldaysale * 30 >= self.branchmonthsalegoal
            yeargoal = totaldaysale * 365 >= self.branchyearsalegoal

            checker_status_data.append(
                {
                    'branch_id':branch.BranchId,
                    'daygoal':daygoal,
                    'monthgoal':monthgoal,
                    'yeargoal':yeargoal
                }
            )
        return checker_status_data
                
            


class dbDelivery:
        
    totalacceptedproducts = 0
    totaldeliverdproducts = 0
    totalbranchdeliverd = 0

    def __init__(self, deliveryid, vicalplateNo,vicaltype,workingbakeryid,
                 totalworkers,totaldayacceptedproductsgoal,
                 totalmonthacceptedproductsgoal,totalyearacceptedproductsgoal,
                 totaldaydeliverdproductsgoal,totalmonthdeliverdproductsgoal,
                 totalyeardeliverdproductsgoal
                 ):
        self.deliveryid = deliveryid
        self.vicalplateNo = vicalplateNo
        self.vicaltype = vicaltype
        self.workingbakeryid = workingbakeryid
        self.totalworkinghour = 0
        self.totalworkers = totalworkers
        self.totaldayacceptedproductsgoal = totaldayacceptedproductsgoal
        self.totalmonthacceptedproductsgoal = totalmonthacceptedproductsgoal
        self.totalyearacceptedproductsgoal = totalyearacceptedproductsgoal
        self.totaldaydeliverdproductsgoal = totaldaydeliverdproductsgoal
        self.totalmonthdeliverdproductsgoal = totalmonthdeliverdproductsgoal
        self.totalyeardeliverdproductsgoal = totalyeardeliverdproductsgoal
    
    def insert_dilverydata(self):
        dilverydata = Delivery(
            DriverID=self.deliveryid,VehiclePlateNo=self.vicalplateNo,Vech
        )

#threading to products sale
def run_scheduled_tasks():
    branch = dbBranch('BranchName', 'Location', 1, 10, 100000, 10000, 1000, 8)
    threading.Thread(target=branch.setproducts).start()
    threading.Thread(target=branch.setsale).start()
run_scheduled_tasks()

branch = dbBranch()
#data = branch.output_branchdata()
#print(data)

print(branch.test())