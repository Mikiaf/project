from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
import logging
import schedule
import time
from datetime import datetime,timedelta
import calendar
import threading
from db import Product_BDB_Transaction_Sale,Branch, Bakery, Delivery, Employee,Products,Transaction,Sale,Salary,Status,Asset,App,Account,Cost,Order,Connection,Admin
from config import db
import warnings
from PIL import Image
import io
import base64
import bcrypt
import os
import re
from sqlalchemy.exc import IntegrityError 
from PIL import Image

warnings.filterwarnings("ignore")
logging.basicConfig(
    filename='app_errors.log',  # File to write logs to
    filemode='a',               # Append to the file
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    level=logging.ERROR         # Only log errors and above
)
engine = create_engine('mysql://root:root@localhost/cobakery')
Session = sessionmaker(bind=engine)



    #gives the image of the employee
def save_image(image_file, filename):
    # Define the directory path
    directory_path = r'C:\Users\outis\Desktop\Oneproject\static\image\employees'
        
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        
    # Define the full image path
    image_path = os.path.join(directory_path, re.sub(r"\s+", "", filename))
        
    # Load and save the image
    image = Image.open(image_file)
    image.save(image_path, format='PNG')
        
    return image_path



class dbBranch:
    totalacceptedproducts = 0
    branchtotalsaleinmonye = 0

    def __init__(self,adminid,branchtype,branchname, location, 
                 controlers_id,totalworkers, branchyearsalegoal, 
                 branchmonthsalegoal, branchdaysalegoal, 
                 branchdayworikinghouregoal,branchimage):
        
        self.adminid = adminid
        self.branchname = branchname
        self.branchtype = branchtype
        self.location = location
        employee = Employee.query.filter_by(EmployeeId=controlers_id).first()
        if employee:
            if employee.WorkingPositionName == None:
                self.controlers_id = controlers_id
            else:
                logging.error(f"Error:Employee occupied for controlers_id {controlers_id}")
                raise ValueError(f"Error:Employee occupied for controlers_id {controlers_id}")
        else:
            logging.error(f"Error:Employee not found for controlers_id {controlers_id}")
            raise ValueError(f"Error:Employee not found for controlers_id {controlers_id}")
        self.totalworkers = totalworkers
        self.branchyearsalegoal = branchyearsalegoal
        self.branchmonthsalegoal = branchmonthsalegoal
        self.branchdaysalegoal = branchdaysalegoal
        self.branchdayworikinghouregoal = branchdayworikinghouregoal
        self.branchimage = branchimage
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

    #update branch data
    @classmethod
    def update_branchdata(cls, id, co_name, value):
        try:
            branch = Branch.query.filter_by(BranchId = id).first()
            old_image_name = f'branch{branch.BranchName}.png'
            if branch:
                if hasattr(branch, co_name):
                    setattr(branch, co_name, value)
                    if co_name == "ControllerId":
                        employee2 = Employee.query.filter_by(EmployeeId=value).first()
                        if employee2.WorkingPositionName == None:
                            employee1 = Employee.query.filter_by(EmployeeId=branch.ControllerId).first()
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='WorkingPositionName',value=None)
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='WorkingPosition',value=None)
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='Role',value=None)
                            
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='WorkingPositionName',value=branch.BranchName)
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='WorkingPosition',value="branch")
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='Role',value="controller")
                            db.session.commit()
                            return f"Branch data with id {id} has been updated",True
                        else:
                            return f"Error:Employee occupied:Branch data with id {id} has not been updated",False
                    if co_name == "BranchName":
                        directory_path = r'C:\Users\outis\Desktop\Oneproject\static\image\employees'
                        # Add file extension to image name
                        current_file_path = os.path.join(directory_path, old_image_name)
                        new_image_name = f'branch{branch.BranchName}.png'
                        new_file_path = os.path.join(directory_path, new_image_name)
                        # Ensure paths are different before renaming
                        if current_file_path != new_file_path:
                            os.rename(current_file_path, new_file_path)
                        db.session.commit() 
                    else:
                        db.session.commit()
                        return f"Branch data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_branchdata,Branch Column {co_name} Not Found")
                    return f'Error: Branch Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_branchdata,Branch With This ID {id} Not Found")
                return f'Error: Branch With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_branchdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #delete branch data 
    @classmethod
    def delete_branchdata(cls,id):
        try:
            branch = Branch.query.filter_by(BranchId = id).first()
            if branch:
                db.session.delete(branch)
                db.session.commit()
                employee = Employee.query.filter_by(EmployeeId=branch.ControllerId).first()
                account = Account.query.filter_by(DeId=branch.BranchId).first()
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='WorkingPositionName',value=None)
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='WorkingPosition',value=None)
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='Role',value=None)
                dbAccount.delete_accountdata(id=account.AccountId)
                return f'Branch with ID {id} has been deleted',True
            else:
                logging.error(f"Error:occurred in delete_branchdata,Branch With This ID {id} Not Found")
                return f'Error: Branch With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_branchdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #insertes data in to database 
    def insert_branchdata(self):
        try:
            branchdata =Branch(AdminId=self.adminid,BranchName=self.branchname,BrnachType=self.branchtype,BranchImage=self.branchimage, Location=self.location, 
                ControllerId=self.controlers_id, TotalWorkers=self.totalworkers, TotalAcceptedProducts=self.totalacceptedproducts,
                BranchTotalSaleInMoney=self.branchtotalsaleinmonye,BranchYearSaleGoalInMoney=self.branchyearsalegoal,
                BranchMonthSaleGoalInMoney=self.branchyearsalegoal, BranchDaySaleGoalInMoney=self.branchdaysalegoal,
                BranchDayWorikingHoureGoal=self.branchdayworikinghouregoal)
            
            db.session.add(branchdata)
            db.session.commit()
            dbEmployee.update_employeedata(id=self.controlers_id,co_name='WorkingPositionName',value=branchdata.BranchName)
            dbEmployee.update_employeedata(id=self.controlers_id,co_name='WorkingPosition',value="branch")
            dbEmployee.update_employeedata(id=self.controlers_id,co_name='Role',value="controller")
            return 'successful',True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_branchdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #gives branch data from database
    @classmethod
    def output_branchdata(cls,adminid):
        try:
            branches=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                branches = Branch.query.all()
            else:
                branches = Branch.query.filter_by(AdminId=adminid).all()
            branchdata = []
            for branch in branches:
                branchdata.append({
                    'time':datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                    "adminid":branch.AdminId,
                    'branchid':branch.BranchId,
                    'branchname':branch.BranchName,
                    "branchtype":branch.BrnachType,
                    'branchimage':branch.BranchImage,
                    'location':branch.Location,
                    'controllerid':branch.ControllerId,
                    'totalworkers':branch.TotalWorkers,
                    'branchStartingdate':branch.BranchStartingDate,
                    'totalacceptedproducts':branch.TotalAcceptedProducts,
                    'branchtotalsaleinmoney':branch.BranchTotalSaleInMoney,
                    'branchyearsalegoalinmoney ':branch.BranchYearSaleGoalInMoney,
                    'branchmonthsalegoalinmoney':branch.BranchMonthSaleGoalInMoney,
                    'branchdaysalegoalinmoney':branch.BranchDaySaleGoalInMoney,
                    'branchdayworikinghouregoal':branch.BranchDayWorikingHoureGoal
                })
            return branchdata
        except Exception as e:
            logging.error(f"Error:occurred in output_branchdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    # calculate the total accpeted products
    def set_totalacceptedproducts(self):
            try:
                with Session() as session:
                    errors = []
                    branch_instance  = Branch.query.filter_by(BranchName=self.branchname).first()
                    if not branch_instance:
                        errors.append(f'Error:BRANCH NOT FOUND FOR BRANCH NAME {self.branchname}')
                        return f'Error:BRANCH NOT FOUND FOR BRANCH NAME {self.branchname}',False
                    
                    branchid = branch_instance.BranchId
                    trans_results =  session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branchid).all()
                    if not trans_results:
                        errors.append(f'Error:TRANSACTION NOT FOUND FOR BRANCH ID {branchid}')
                        return f'Error:TRANSACTION NOT FOUND FOR BRANCH ID {branchid}',False
                    
                    for result in trans_results:
                        transaction_instance = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                        if not transaction_instance:
                            errors.append( f'Error: TRANSACTION INSTANCE NOT FOUND FOR TRANSACTION ID {result.Transaction_id}')
                            continue
                        
                        self.totalacceptedproducts += transaction_instance.DeliveredProductQuantity
                    branch_instance.TotalAcceptedProducts =  self.totalacceptedproducts
                    db.session.commit()
                    if errors:
                        logging.error(f"Error:occurred in set_totalacceptedproducts,Error:{errors} HAS BEEN FOUND")
                        return f'Completed with {len(errors)} error(s) ',errors
                    return f'successfull'
            except Exception as e:
                logging.error(f"Error:occurred in set_totalacceptedproducts,Error:{e} HAS BEEN FOUND")
                return f"Error:{e} HAS BEEN FOUND",False
    def setproducts(self):
        schedule.every(24).hours.do(self.set_totalacceptedproducts)
        while True:
            schedule.run_pending()
            time.sleep(18000)
    #calculate the total branch sale in monye
    def set_branchtotalsaleinmonye(self):
            try:
                with Session() as session:
                    errors = []
                    branch_instance = Branch.query.filter_by(BranchName=self.branchname).first()
                    if branch_instance:
                        errors.append(f'Error:BRANCH NOT FOUND FOR BRANCH NAME {self.branchname}')
                        return f'Error:BRANCH NOT FOUND FOR BRANCH NAME {self.branchname}',False
                    
                    branchid = branch_instance.BranchId
                    trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branchid).all()
                    if not trans_result:
                        errors.append(f'Error:TRANSACTION NOT FOUND FOR BRANCH ID {branchid}')
                        return f'Error:TRANSACTION NOT FOUND FOR BRANCH ID {branchid}',False
                    
                    for result in trans_result:
                        saleid = result.Sale_id
                        sale_instance = Sale.query.filter_by(SaleId=saleid).first()
                        if not sale_instance:
                            errors.append(f'Error:SALE_INSTANCE NOT FOUND FOR SALE ID {saleid}')
                            continue
                        self.branchtotalsaleinmonye += sale_instance.TotalSaledMoney
                    branch_instance.BranchTotalSaleInMoney = self.branchtotalsaleinmonye
                    db.session.commit()
                    if errors:
                        logging.error(f"Error:occurred in set_branchtotalsaleinmonye,Error:{errors} HAS BEEN FOUND")
                        return f'Completed with {len(errors)} error(s) ',errors
                    return f'successfull.'
            except Exception as e:
                logging.error(f"Error:occurred in set_branchtotalsaleinmonye,Error:{e} HAS BEEN FOUND")
                return f"Error:{e} HAS BEEN FOUND",False
    def setsale(self):
        schedule.every(24).hours.do(self.set_branchtotalsaleinmonye)
        while True:
            schedule.run_pending()
            time.sleep(18000)
    
    #gives last 24 hours accepted products data form database
    @classmethod
    def output_acceptedproductdata(cls,adminid):
        try:
            with Session() as session:
                branches=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    branches = Branch.query.all()
                else:
                    branches = Branch.query.filter_by(AdminId=adminid).all()
                products_data = []
                errors = []
                now = datetime.now()
                last_24_hours = now - timedelta(hours=24)
                sales =  Sale.query.filter(Sale.SaleTime >=last_24_hours).all()
                for branch in branches:
                    trans_results = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branch.BranchId).filter(
                        Product_BDB_Transaction_Sale.c.Time >=  last_24_hours
                    ).all()
                    branch_last_24_sale = 0
                    branch_last_24_accepted = 0 
                    if not trans_results:
                        errors.append(f'Error:TRANSACTION NOT FOUND FOR BRANCH ID {branch.BranchId}')
                        continue
                    for result in trans_results:
                            transactions = Transaction.query.filter(BranchId = result.Branch_id).all()
                            matching_sales = []
                            for s in sales:
                                if s.SaleBranchId == result.Branch_id and s.TransactionId == result.Transaction_id:
                                    matching_sales.append(s)
                            if not matching_sales:
                                errors.append(f"Error:SALE NOT FOUND FOR BRANCH ID {result.Branch_id}")
                                continue
                            for sale in matching_sales:
                                branch_last_24_sale += sale.TotalSaledMoney
                            for transaction in transactions:
                                product = Products.query.filter(ProductId = transaction.Product_id).first()
                                products_data.append({
                                    'time':now.strftime("%d/%m/%y  %H:%M:%S"),
                                    'branchid':branch.BranchId,
                                    "adminid":branch.AdminId,
                                    'branchname': branch.BranchName,
                                    'productid':product.ProductId,
                                    'productname':product.ProductName,
                                    'productquantityaccepted':transaction.DeliveredProductQuantity,
                                    'totaldayproductselledIn$': branch_last_24_sale,
                                    'acceptedtime': transaction.TransEndingTime,
                                    'deliveryid	':result.Delivery_id,
                                    'branchSalein$': branch_last_24_sale
                                })
                if errors:
                    logging.error(f"Error:occurred in output_acceptedproductdata,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s) ', errors, products_data
                return products_data
        except Exception as e:
            logging.error(f"Error:occurred in output_acceptedproductdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    

    #gives a single branch data output
    @classmethod
    def single_outputbranchdata(cls,id):
        branch = Branch.query.filter_by(BranchId=id).first()
        branchdata = {
            'branchid': branch.BranchId,
            'adminid':branch.AdminId,
            'branchname': branch.BranchName,
            'location':branch.Location,
            'controllerid':branch.ControllerId,
            'totalworkers':branch.TotalWorkers,
            'branchstartingdate':branch.BranchStartingDate,
            'totalacceptedproducts':branch.TotalAcceptedProducts,
            'branchtotalsaleinmoney':branch.BranchTotalSaleInMoney,
            'branchyearsalegoalinmoney':branch.BranchYearSaleGoalInMoney,
            'branchmonthsalegoalinmoney':branch.BranchMonthSaleGoalInMoney,
            'branchdaysalegoalinmoney':branch.BranchDaySaleGoalInMoney,
            'branchdayworikinghouregoal':branch.BranchDayWorikingHoureGoal
        }
        return branchdata
    
    #gives monthly branch status data
    @classmethod
    def monthly_branchstatusdata(cls,adminid):
        try:
            with Session() as session:
                branches=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    branches = Branch.query.all()
                else:
                    branches = Branch.query.filter_by(AdminId=adminid).all()
                monthstatus = []
                errors = []
                now = datetime.now()
                last_730_hours = now - timedelta(hours=730)
                sales = Sale.query.filter(Sale.SaleTime >= last_730_hours).all() 
                transactions = Transaction.query.filter(Transaction.TransStartingTime >= last_730_hours).all()
                for branch in branches:
                    trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branch.BranchId).filter(
                        Product_BDB_Transaction_Sale.c.Time >=last_730_hours
                    ).all()
                    if not trans_result:
                        errors.append(f"Error:TRANSACTION NOT FOUND FOR BRANCH ID {branch.BranchId}")
                        continue
                    totalmonthsoldproductsInmoney = 0
                    totalmonthacceptedproductsvalue = 0
                    monthsalegoal = False
                    monthworkinghour = 0
                    for result in trans_result:
                        matching_sales = []
                        for s in sales: 
                            if s.SaleBranchId == result.Branch_id and s.TransactionId == result.Transaction_id: 
                                matching_sales.append(s)
                        if not matching_sales:
                            errors.append(f"Error:SALE NOT FOUND FOR BRANCH ID {result.Branch_id}")
                            continue
                        for sale in matching_sales:
                            totalmonthsoldproductsInmoney += sale.TotalSaledMoney
                        matching_transaction = []
                        for t in transactions: 
                            if t.BranchId == result.Branch_id: 
                                matching_transaction.append(t)
                        if not matching_transaction:
                            errors.append(f"Error:TRANSACTION NOT FOR TRANSACTION ID {result.Transaction_id}")
                            continue
                        for transaction in matching_transaction:
                            totalmonthacceptedproductsvalue += transaction.TotalAcceptedProductValueInMoney
                    goaldata = cls.checker()
                    for data in goaldata:
                        if data["branchid"] == branch.BranchId:
                            monthsalegoal = data["monthgoal"]
                    monthstatus.append({
                        "date":now.strftime("%m/%y"),
                        "branchid":branch.BranchId,
                        "adminid":branch.AdminId,
                        "branchname":branch.BranchName,
                        "controllerid":branch.ControllerId,
                        "totalmonthsoldproductsInmoney":totalmonthsoldproductsInmoney,
                        "totalmonthacceptedproductsvalue":totalmonthacceptedproductsvalue,
                        "monthsalegoal":monthsalegoal
                    })
                if errors:
                    logging.error(f"Error:occurred in monthly_branchstatusdata,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)', errors, monthstatus
                return monthstatus
        except Exception as e:
            logging.error(f"Error:occurred in monthly_branchstatusdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #gives year branch status data
    @classmethod
    def year_branchstatudata(cls,adminid):
        try:
            with Session() as session:
                branches=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    branches = Branch.query.all()
                else:
                    branches = Branch.query.filter_by(AdminId=adminid).all()
                yearstatus = []
                errors = []
                now = datetime.now()
                last_8760_hours = now - timedelta(hours=8760)
                sales = Sale.query.filter(Sale.SaleTime >= last_8760_hours).all() 
                transactions = Transaction.query.filter(Transaction.TransStartingTime >= last_8760_hours).all()
                for branch in branches:
                    trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branch.BranchId).filter(
                        Product_BDB_Transaction_Sale.c.Time >=last_8760_hours 
                    ).all()
                    if not trans_result:
                        errors.append(f"Error:TRANSACTION NOT FOUND FOR BRANCH ID {branch.BranchId}")
                        continue
                    totalyearsoldproductsInmoney = 0
                    totalyearacceptedproductsvalue = 0
                    yearsalegoal = False
                    yearworkinghour = 0
                    for result in trans_result:
                        matching_sales = []
                        for s in sales: 
                            if s.SaleBranchId == result.Branch_id and s.TransactionId == result.Transaction_id: 
                                matching_sales.append(s)
                        if not matching_sales:
                            errors.append(f"Error:SALE NOT FOUND FOR BRANCH ID {result.Sale_id}")
                            continue
                        for sale in matching_sales:
                            totalyearsoldproductsInmoney += sale.TotalSaledMoney
                        matching_transaction = []
                        for t in transactions: 
                            if t.BranchId == result.Branch_id: 
                                matching_transaction.append(t)
                                
                        if not matching_transaction:
                            errors.append(f"Error:TRANSACTION NOT FOR TRANSACTION ID {result.Transaction_id}")
                            continue
                        for transaction in matching_transaction:
                            totalyearacceptedproductsvalue += transaction.TotalAcceptedProductValueInMoney
                    goaldata = cls.checker()
                    for data in goaldata:
                        if data["branchid"] == branch.BranchId:
                            yearsalegoal = data["monthgoal"]
                    yearstatus.append({
                        "date":now.strftime("%m/%y"),
                        "branchid":branch.BranchId,
                        "adminid":branch.AdminId,
                        "branchname":branch.BranchName,
                        "controllerid":branch.ControllerId,
                        "totalyearsoldproductsInmoney":totalyearsoldproductsInmoney,
                        "totalyearacceptedproductsvalue":totalyearacceptedproductsvalue,
                        "yearsalegoal":yearsalegoal
                    })
                if errors:
                    logging.error(f"Error:occurred in year_branchstatudata,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)', errors, yearstatus
                return yearstatus
        except Exception as e:
            logging.error(f"Error:occurred in year_branchstatudata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    #gives day branch status data
    @classmethod
    def day_branchstatusdata(cls,adminid):
        try:
            with Session() as session:
                errors = []
                daystatus = []
                branches=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    branches = Branch.query.all()
                else:
                    branches = Branch.query.filter_by(AdminId=adminid).all()
                now = datetime.now()
                last_24_hours = now - timedelta(hours=24)
                sales = Sale.query.filter(Sale.SaleTime >= last_24_hours).all() 
                transactions = Transaction.query.filter(Transaction.TransStartingTime >= last_24_hours).all()
                for branch in branches:
                            trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branch.BranchId).filter(
                                Product_BDB_Transaction_Sale.c.Time >= last_24_hours
                            ).all()
                            if not trans_result:
                                errors.append(f"Error:TRANSACTION NOT FOUND FOR BRANCH ID {branch.BranchId}")
                                continue
                            totaldaysoldproductsinmoney = 0
                            totaldayacceptedproductsinmoney = 0 
                            totaldayworking = 0
                            daysalegoal = False
                            for result in trans_result:
                                matching_sales = []
                                for s in sales: 
                                    if s.SaleBranchId == result.Branch_id and s.TransactionId == result.Transaction_id: 
                                        matching_sales.append(s)
                                if not matching_sales:
                                    errors.append(f"Error:SALE NOT FOUND FOR BRANCH ID {result.Sale_id}")
                                    continue
                                for sale in matching_sales:
                                    totaldaysoldproductsinmoney += sale.TotalSaledMoney
                                matching_transactions = []
                                for t in transactions:
                                    if t. BranchId == result.Branch_id: 
                                        matching_transactions.append(t)
                                if not matching_transactions:
                                    errors.append(f"Error:TRANSACTION NOT FOR TRANSACTION ID {result.Transaction_id}")
                                    continue
                                for transaction in matching_transactions:
                                    totaldayacceptedproductsinmoney += transaction.TotalAcceptedProductValueInMoney
                            goaldata = cls.checker()
                            for data in goaldata:
                                if data["branchid"] == branch.BranchId:
                                    daysalegoal = data["daygoal"]
                                    break
                            daystatus.append({
                                "date":now.strftime("%d/%m/%y"),
                                "branchid":branch.BranchId,
                                "adminid":branch.AdminId,
                                "controllerid":branch.ControllerId,
                                "branchname":branch.BranchName,
                                "totaldaysoldproductsinmoney":totaldaysoldproductsinmoney,
                                "totaldayacceptedproductsinmoney":totaldayacceptedproductsinmoney,
                                "daysalegoal":daysalegoal
                            })
                if errors:
                    logging.error(f"Error:occurred in day_branchstatusdata,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s).',errors, daystatus
                return daystatus
        except Exception as e:
            logging.error(f"Error:occurred in day_branchstatusdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False


    #checkes day,month,year, sale goals
    def checker(self):
        try:
            with Session() as session:
                errors = []
                now = datetime.now()
                last_24_hours = now - timedelta(hours=24)
                last_730_hours = now - timedelta(hours=730)
                last_8760_hours = now - timedelta(hours=8760)
                branchs = Branch.query.all()
                checker_status_data = []
                for branch in branchs:
                    totaldaysale = 0
                    totalmonthsale = 0
                    totalyearsale = 0 

                    #checkes day sale goal
                    daytrans_results = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branch.BranchId).filter(
                        Product_BDB_Transaction_Sale.c.Time >=  last_24_hours
                    ).all()
                    if not daytrans_results:
                        errors.append(f"DAY TRANSACTION NOT FOUND FOR BRANCH ID {branch.BranchId}")
                        continue
                    for result in daytrans_results:
                        sale =  Sale.query.filter_by(SaleBranchId = result.Branch_id).first()
                        if not sale:
                            errors.append(f"DAY SALE NOT FOUND FOR BRANCH ID {result.Sale_id}")
                            continue
                        totaldaysale += sale.TotalSaledMoney
                    daygoal =  totaldaysale >= self.branchdaysalegoal

                    #checkes  month sale goal
                    monthtrans_results = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branch.BranchId).filter(
                        Product_BDB_Transaction_Sale.c.Time >=  last_730_hours
                    ).all()
                    if not monthtrans_results:
                        errors.append(f"MONTH TRANSACTION NOT FOUND FOR BRANCH ID {branch.BranchId}")
                        continue
                    for result in monthtrans_results:
                        sale =  Sale.query.filter_by(SaleBranchId = result.Branch_id).first()
                        if not sale:
                            errors.append(f"MONTH SALE NOT FOUND FOR BRANCH ID {result.Sale_id}")
                            continue
                        totalmonthsale += sale.TotalSaledMoney
                    monthgoal = totalmonthsale >= self.branchmonthsalegoal

                    #checkes year sale goal
                    yeartrans_results = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branch.BranchId).filter(
                        Product_BDB_Transaction_Sale.c.Time >=  last_8760_hours
                    ).all()
                    if not yeartrans_results:
                        errors.append(f"YEAR TRANSACTION NOT FOUND FOR BRANCH ID {branch.BranchId}")
                        continue
                    for result in yeartrans_results:
                        sale =  Sale.query.filter_by(SaleBranchId = result.Branch_id).first()
                        if not sale:
                            errors.append(f"YEAR SALE NOT FOUND FOR BRANCH ID {result.Sale_id}")
                            continue
                        totalyearsale += sale.TotalSaledMoney
                    yeargoal = totalyearsale >= self.branchyearsalegoal
                    checker_status_data.append(
                        {
                            'branchid':branch.BranchId,
                            'daygoal':daygoal,
                            'monthgoal':monthgoal,
                            'yeargoal':yeargoal
                        }
                    )
                if errors:
                    logging.error(f"Error:occurred in checker,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s).', errors, checker_status_data
                return checker_status_data
        except Exception as e:
            logging.error(f"Error:occurred in checker,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
                
            
class dbBakery:
    totalbakedproducts = 0
    totalsendoutproduct = 0 

    def __init__(self,adminid,bakeryname,bakerytype,managerid,loacation,totalworkers,
                 totaldaytobakeproductsgoal,totalmonthtobakeproductsgoal,
                 totalyeartobakeproductsgoal,totaldaytosendoutproductsgoal,
                 totalmonthtosendoutproductsgoal,totalyeartosendoutproductsgoal,
                 bakeryimage):
        self.bakeryname = bakeryname
        self.bakerytype = bakerytype
        self.adminid = adminid
        employee = Employee.query.filter_by(EmployeeId=managerid).first()
        if employee:
            if employee.WorkingPositionName == None:
                self.managerid = managerid
            else:
                logging.error(f"Error:Employee occupied for managerid {managerid}")
                raise ValueError(f"Error:Employee occupied for managerid {managerid}")
        else:
            logging.error(f"Error:Employee not found for managerid{managerid}")
            raise ValueError(f"Error:Employee not found for managerid{managerid}")
        self.totalworkerhours = 0
        self.loacation = loacation
        self.totalworkers = totalworkers
        self.totaldaytobakeproductsgoal = totaldaytobakeproductsgoal
        self.totalmonthtobakeproductsgoal = totalmonthtobakeproductsgoal
        self.totalyeartobakeproductsgoal = totalyeartobakeproductsgoal
        self.totaldaytosendoutproductsgoal = totaldaytosendoutproductsgoal
        self.totalmonthtosendoutproductsgoal = totalmonthtosendoutproductsgoal
        self.totalyeartosendoutproductsgoal = totalyeartosendoutproductsgoal
        self.bakeryimage = bakeryimage

    #gives the image of the bakery factor
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
    #insert bakery data into database
    def insert_bakerydata(self):
        try:
            bakerydata = Bakery(AdminId=self.adminid,BakeryName=self.bakeryname,BakeryType=self.bakerytype,BakeryImage=self.bakeryimage,ManagerID=self.managerid,Location=self.loacation,TotalWorkingHours=self.totalworkerhours,
                   TotalBakedProducts=self.totalbakedproducts,TotalSendOutProducts=self.totalsendoutproduct,TotalWorkers=self.totalworkers,
                   TotalDayToBakeProductsGoal=self.totaldaytobakeproductsgoal,TotalMonthToBakeProductsGoal=self.totalmonthtobakeproductsgoal,
                   TotalYearToBakeProductsGoal=self.totalyeartobakeproductsgoal,TotalDayToSendOutProductsGoal=self.totaldaytosendoutproductsgoal,
                   TotalMonthToSendOutProductsGoal=self.totalmonthtosendoutproductsgoal,TotalYearToSendOutProductsGoal=self.totalyeartosendoutproductsgoal)
            db.session.add(bakerydata)
            db.session.commit()
            dbEmployee.update_employeedata(id=self.managerid,co_name='WorkingPositionName',value=bakerydata.BakeryName)
            dbEmployee.update_employeedata(id=self.managerid,co_name='WorkingPosition',value="bakery")
            dbEmployee.update_employeedata(id=self.managerid,co_name='Role',value="manager")
            return 'successful',True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_bakerydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #gives bakery data into database
    @classmethod
    def output_bakerydata(cls,adminid):
        try:
            bakeryes=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                bakeryes = Bakery.query.all()
            else:
                bakeryes = Bakery.query.filter_by(AdminId=adminid).all()
            bakerydata = []
            for bakery in bakeryes:
                bakerydata.append({
                    'time':datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                    'adminid':bakery.AdminId,
                    'bakeryid':bakery.BakeryId,
                    "bakeryname":bakery.BakeryName,
                    "bakerytype":bakery.BakeryType,
                    'bakeryimage':bakery.BakeryImage,
                    'managerid':bakery.ManagerID,
                    'bakerystarteddate':bakery.BakeryStartedDate,
                    'totalworkinghours':bakery.TotalWorkingHours,
                    'location':bakery.Location,
                    'totalworkers':bakery.TotalWorkers,
                    'totalbakedproducts':bakery.TotalBakedProducts,
                    'totalsendoutproducts':bakery.TotalSendOutProducts,
                    'totaldaytobakeproductsgoal':bakery.TotalDayToBakeProductsGoal,
                    'totalmonthtobakeproductsgoal':bakery.TotalMonthToBakeProductsGoal,
                    'totalyeartobakeproductsgoal':bakery.TotalYearToBakeProductsGoal,
                    'totaldaytosendoutproductsgoal':bakery.TotalDayToSendOutProductsGoal,
                    'totalmonthtosendoutproductsgoal':bakery.TotalMonthToSendOutProductsGoal,
                    'totalyeartosendoutproductsgoal':bakery.TotalYearToSendOutProductsGoal
                })
            return bakerydata
        except Exception as e:
            logging.error(f"Error:occurred in output_bakerydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    @classmethod
    def single_outputbakerydata(cls,id):
        bakery = Bakery.query.filter_by(BakeryId=id).first()
        bakerydata={
            'bakeryid': bakery.BakeryId,
            'adminid':bakery. AdminId,
            'bakeryname': bakery.BakeryName,
            'managerid': bakery.ManagerID,
            'bakerystarteddate': bakery.BakeryStartedDate,
            'totalworkinghours': bakery.TotalWorkingHours,
            'location': bakery.Location,
            'totalworkers': bakery.TotalWorkers,
            'totalbakedproducts': bakery.TotalBakedProducts,
            'totalsendoutproducts': bakery.TotalSendOutProducts,
            'totaldaytobakeproductsgoal': bakery.TotalDayToBakeProductsGoal,
            'totalmonthtobakeproductsgoal': bakery.TotalMonthToBakeProductsGoal,
            'totalyeartobakeproductsgoal': bakery.TotalYearToBakeProductsGoal,
            'totaldaytosendoutproductsgoal': bakery.TotalDayToSendOutProductsGoal,
            'totalmonthtosendoutproductsgoal': bakery.TotalMonthToSendOutProductsGoal,
            'totalyeartosendoutproductsgoal': bakery.TotalYearToSendOutProductsGoal,
        }
        return bakerydata
    #updates bakery data
    @classmethod
    def update_bakerydata(cls,id,co_name,value):
        try:
            bakery = Bakery.query.filter_by(BakeryId=id).first()
            old_image_name = f'bakery{bakery.BakeryName}.png'
            if bakery:
                if hasattr(bakery,co_name):
                    setattr(bakery,co_name,value)
                    if co_name == "ManagerID":
                        employee2 = Employee.query.filter_by(EmployeeId=value).first()
                        if employee2.WorkingPositionName == None:
                            employee1 = Employee.query.filter_by(EmployeeId=bakery.ManagerID).first()
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='WorkingPositionName',value=None)
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='WorkingPosition',value=None)
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='Role',value=None)
        
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='WorkingPositionName',value=bakery.ManagerID)
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='WorkingPosition',value="bakery")
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='Role',value="manager")
                            db.session.commit()
                            return f"Bakery data with id {id} has been updated",True
                        else:
                           return f"Error:Employee occupied:Bakery data with id {id} has not been updated",False
                    if co_name == "BakeryName":
                        directory_path = r'C:\Users\outis\Desktop\Oneproject\static\image\employees'
                        # Add file extension to image name
                        current_file_path = os.path.join(directory_path, old_image_name)
                        new_image_name = f'bakery{bakery.BakeryName}.png'
                        new_file_path = os.path.join(directory_path, new_image_name)
                        # Ensure paths are different before renaming
                        if current_file_path != new_file_path:
                            os.rename(current_file_path, new_file_path)
                        db.session.commit()
                    else:
                        db.session.commit()
                        return f"Bakery data with id {id} has been updated",True
                else:
                    return f"Error with column {co_name} UNIDENTEFINDE",False
            else:
                logging.error(f"Error:occurred in update_bakerydata,Error:  bakery with id {id} NOT FOUND")
                return f"Error: bakery with id {id} NOT FOUND",False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_bakerydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deletes delivery data
    @classmethod
    def delete_bakerydata(cls,id):
        try:
            bakery = Bakery.query.filter_by(BakeryId=id).first()
            if bakery:
                db.session.delete(bakery)
                db.session.commit()
                employee = Employee.query.filter_by(EmployeeId=bakery.ManagerID).first()
                account = Account.query.filter_by(DeId=bakery.BakeryId).first()
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='WorkingPositionId',value=None)
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='WorkingPosition',value=None)
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='Role',value=None)
                dbAccount.delete_accountdata(id=account.AccountId)
                return f'bakery with id {id} has been deleted',True
            else:
                logging.error(f"Error:occurred in delete_bakerydata,Bakery With This ID {id} Not Found")
                return f'Error: Bakery With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_bakerydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    #calculate total product baked & sendout
    # included in thrend 
    def set_totalproducts(self):
            try:
                with Session() as session:
                    errors = []
                    bakery_instance = Bakery.query.filter_by(BakeryName=self.bakeryname).first()
                    if not bakery_instance:
                        logging.error(f"Error:occurred in set_totalproducts,Error: BAKERY NOT FOUND")
                        return 'Error: BAKERY NOT FOUND',False
                    bakery_id = bakery_instance.BakeryId
                    products = Products.query.filtery_by(BakeryId=bakery_id).all()
                    if not products:
                        errors.append(f'Error:PRODUCTS NOT FOUND FOR BAKERY ID {bakery_id}')
                        return f'Error:PRODUCTS NOT FOUND FOR BAKERY ID {bakery_id}',False
                    for product in products:
                        self.totalbakedproducts += product.TotalBakedProducts
                    trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Bakery_id=bakery_id).all()
                    if not trans_result:
                        errors.append(f"Error:TRANSACTION NOT FOUND FOR BAKERY ID {bakery_id}")
                        return f"Error:TRANSACTION NOT FOUND FOR BAKERY ID {bakery_id}",False
                    for result in trans_result:
                        transaction = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                        self.totalsendoutproduct += transaction.AcceptedProductQuantity
                    
                    bakery_instance.TotalBakedProducts = self.totalbakedproducts 
                    bakery_instance.TotalSendOutProducts = self.totalsendoutproduct

                    db.session.commit()
                if errors:
                    logging.error(f"Error:occurred in set_totalproducts,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s).',errors
                return 'successful'
            except Exception as e:
                logging.error(f"Error:occurred in bakery set_totalproducts,Error:{e} HAS BEEN FOUND")
                return f"Error:{e} HAS BEEN FOUND",False
    
    def setproducts(self):
        schedule.every(24).hours.do(self.set_totalproducts)
        while True:
            schedule.run_pending()
            time.sleep(18)

    
    #outputing bakery product data
    @classmethod
    def output_productdata(cls,adminid):
        try:
            with Session() as session:
                errors = []
                product_data = []
                bakeries=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    bakeries = Bakery.query.all()
                else:
                    bakeries = Bakery.query.filter_by(AdminId=adminid).all()
                now = datetime.now()
                last_24_hours = now - timedelta(hours=24)
                for bakery in bakeries:
                    products_result = Products.query.filter_by(BakeryId=bakery.BakeryId).filter(
                        Products.TimeOfBakery >= last_24_hours
                    ).all()
                    if not products_result:
                        errors.append(f"Error:PRODUCT NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                        continue
                    for result in products_result:
                        products_remaining =  result.TotalBakedProducts - result.TotalProductsSendOut
                        product_data.append({
                            'time':now.strftime("%d/%m/%y  %H:%M:%S"),
                            'bakeryid':bakery.BakeryId,
                            'adminid':bakery.AdminId,
                            'bakeryname':bakery.BakeryName,
                            'productid':result.ProductId,
                            'productname':result.ProductName,
                            'timeofbakery':result.TimeOfBakery,
                            'numberofproductbaked':result.TotalBakedProducts,
                            'totalproductssendout':result.TotalProductsSendOut,
                            'numberofproductsremaining':products_remaining,
                            'usedproductsforbakery':result.ProductsUsedForBakery,
                            'moneyusedtobaketheproduct':result.MoneyUsedToBakeTheProduct,
                            'totalbakedproductvalue':result.TotalBakedProductValue,
                            'totalsendoutproductvalue':result.TotalProductsSendOutValue,
                            'oneproductvalue':result.OneProductValueInMoney
                        })
                if errors:
                    logging.error(f"Error:occurred in output_productdata,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)',errors,product_data  
                return product_data
        except Exception as e:
                logging.error(f"Error:occurred in bakery output_productdata,Error:{e} HAS BEEN FOUND")
                return f"Error:{e} HAS BEEN FOUND",False
    
    #gives day bakery status data
    @classmethod
    def day_bakerystatus(cls,adminid):
        try:
            with Session() as session:
                errors = []
                now = datetime.now()
                last_24_hours = now - timedelta(hours=24)
                bakeryes=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    bakeryes = Bakery.query.all()
                else:
                    bakeryes = Bakery.query.filter_by(AdminId=adminid).all()
                daystatus = []
                for bakery in bakeryes:
                        totalbakedproductvalue = 0
                        totalsendoutproductvalue = 0
                        totalbakedproducts = 0
                        totalsendoutproducts = 0
                        products = Products.query.filter_by(BakeryId=bakery.BakeryId).filter(
                            Products.TimeOfBakery >=last_24_hours
                        ).all()
                        if not products:
                            errors.append(f"Error:PRODUCT NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                            continue
                        for product in products:
                            totalbakedproductvalue += product.TotalBakedProductValue
                            totalsendoutproductvalue += product.TotalProductsSendOutValue
                            totalbakedproducts += product.TotalBakedProducts
                            totalsendoutproducts += product.TotalProductsSendOut
                        
                        goaldata = cls.cheker()
                        daybakerygoal = False
                        daysendoutgoal = False
                        for data in goaldata:
                            if bakery.BakeryId == data["bakeryid"]:
                                daybakerygoal = data["daybakedgoal"]
                                daysendoutgoal = data["daysendoutgoal"]
                        
                        daystatus.append({
                            'data':now.strftime("%d%m/%y"),
                            'bakeryid':bakery.BakeryId,
                            'adminid':bakery.AdminId,
                            'bakeryname':bakery.BakeryName,
                            'managerid':bakery.ManagerID,
                            'totalbakedproducts ':totalbakedproducts,
                            'totalsendoutproducts':totalsendoutproducts,
                            'totalbakedproductvalue':totalbakedproductvalue,
                            'totalsendoutproductvalue':totalsendoutproductvalue,
                            'daybakerygoal':daybakerygoal,
                            'daysendoutgoal':daysendoutgoal

                        })
                if errors:
                    logging.error(f"Error:occurred in output_productdata,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)',errors,daystatus  
                return daystatus
        except Exception as e:
            logging.error(f"Error:occurred in bakery day_bakerystatus,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #gives month bakery status data
    @classmethod
    def month_bakerystatus(cls,adminid):
        try:
            errors = []
            now = datetime.now()
            last_730_hours = now - timedelta(hours=730)
            bakeryes=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                bakeryes = Bakery.query.all()
            else:
                bakeryes = Bakery.query.filter_by(AdminId=adminid).all()
            monthstatus = []
            for bakery in bakeryes:
                totalbakedproductvalue = 0
                totalsendoutproductvalue = 0
                totalbakedproducts = 0
                totalsendoutproducts = 0
                products = Products.query.filter_by(BakeryId=bakery.BakeryId).filter(
                        Products.TimeOfBakery >=last_730_hours
                ).all()
                if not products:
                        errors.append(f"Error:PRODUCT NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                        continue
                for product in products:
                    totalbakedproductvalue += product.TotalBakedProductValue
                    totalsendoutproductvalue += product.TotalProductsSendOutValue
                    totalbakedproducts += product.TotalBakedProducts
                    totalsendoutproducts += product.TotalProductsSendOut
                goaldata = cls.cheker()
                monthbakerygoal = False
                monthsendoutgoal = False
                for data in goaldata:
                    if bakery.BakeryId == data["bakeryid"]:
                        monthbakerygoal = data["monthbakedgoal"]
                        monthsendoutgoal = data["monthsendoutgoal"]
                monthstatus.append({
                        'data':now.strftime("%m/%y"),
                        'bakeryid':bakery.BakeryId,
                        'adminid':bakery.AdminId,
                        'bakeryname':bakery.BakeryName,
                        'managerid':bakery.ManagerID,
                        'bakerystartingdate':bakery.BakeryStartedDate,
                        'monthtotalbakedproducts ':totalbakedproducts,
                        'monthtotalsendoutproducts':totalsendoutproducts,
                        'monthtotalbakedproductvalue':totalbakedproductvalue,
                        'monthtotalsendoutproductvalue':totalsendoutproductvalue,
                        'monthbakerygoal':monthbakerygoal,
                        'monthsendoutgoal':monthsendoutgoal
                })
            if errors:
                logging.error(f"Error:occurred in output_productdata,Error:{errors} HAS BEEN FOUND")
                return f'Completed with {len(errors)} error(s)',errors,monthstatus  
            return monthstatus
        except Exception as e:
            logging.error(f"Error:occurred in bakery day_bakerystatus,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #gives year bakery status data
    @classmethod
    def year_bakerystatus(cls,adminid):
        try:
            errors = []
            now = datetime.now()
            last_8760_hours = now - timedelta(hours=8760)
            bakeryes=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                bakeryes = Bakery.query.all()
            else:
                bakeryes = Bakery.query.filter_by(AdminId=adminid).all()
            yearstatus = []
            for bakery in bakeryes:
                totalbakedproductvalue = 0
                totalsendoutproductvalue = 0
                totalbakedproducts = 0
                totalsendoutproducts = 0
                products = Products.query.filter_by(BakeryId=bakery.BakeryId).filter(
                        Products.TimeOfBakery >=last_8760_hours
                ).all()
                if not products:
                        errors.append(f"Error:PRODUCT NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                        continue
                for product in products:
                    totalbakedproductvalue += product.TotalBakedProductValue
                    totalsendoutproductvalue += product.TotalProductsSendOutValue
                    totalbakedproducts += product.TotalBakedProducts
                    totalsendoutproducts += product.TotalProductsSendOut
                goaldata = cls.cheker()
                yearbakerygoal = False
                yearsendoutgoal = False
                for data in goaldata:
                    if bakery.BakeryId == data["bakeryid"]:
                        yearbakerygoal = data["yearbakedgoal"]
                        yearsendoutgoal = data["yearsendoutgoal"]
                yearstatus.append({
                        'data':now.strftime("%m/%y"),
                        'bakeryid':bakery.BakeryId,
                        'adminid':bakery.AdminId,
                        'bakeryname':bakery.BakeryName,
                        'managerid':bakery.ManagerID,
                        'bakerystartingdate':bakery.BakeryStartedDate,
                        'yeartotalbakedproducts ':totalbakedproducts,
                        'yeartotalsendoutproducts':totalsendoutproducts,
                        'yeartotalbakedproductvalue':totalbakedproductvalue,
                        'yeartotalsendoutproductvalue':totalsendoutproductvalue,
                        'yearbakerygoal':yearbakerygoal,
                        'yearsendoutgoal':yearsendoutgoal
                })
            if errors:
                logging.error(f"Error:occurred in output_productdata,Error:{errors} HAS BEEN FOUND")
                return f'Completed with {len(errors)} error(s)',errors,yearstatus
            return yearstatus
        except Exception as e:
            logging.error(f"Error:occurred in bakery day_bakerystatus,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
  
    #checkes day,month,year bakery data goals
    def cheker(self):
        try:
            with Session() as session:
                errors = []
                now = datetime.now()
                last_24_hours = now - timedelta(hours=24)
                last_730_hours = now - timedelta(hours=730)
                last_8760_hours = now - timedelta(hours=8760)
                bakeryes = Bakery.query.all()
                checker_status_data = []

                for bakery in bakeryes:
                    totaldaybaked = 0
                    totaldaysendout = 0
                    totalmonthbaked = 0
                    totalmonthsendout = 0
                    totalyearbaked = 0
                    totalyearsendout = 0
                    #day bakery status cheker
                    dayproduct_status = Products.query.filter_by(BakeryId=bakery.BakeryId).filter(
                        Products.TimeOfBakery >=last_24_hours
                    ).all()
                    
                    if not dayproduct_status:
                        errors.append(f"Error:DAY STATUS PRODUCT NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                        continue
                    for result in dayproduct_status:
                        totaldaybaked += result.TotalBakedProducts
                        totaldaysendout += result.TotalProductsSendOut
                    daybakedgoal = totaldaybaked >= self.totaldaytobakeproductsgoal
                    daysendoutgoal = totaldaysendout >= self.totaldaytosendoutproductsgoal
                    
                    #month bakery status cheker
                    monthproduct_status = Products.query.filter_by(BakeryId=bakery.BakeryId).filter(
                        Products.TimeOfBakery >=last_730_hours
                    ).all()
                    
                    if not monthproduct_status:
                        errors.append(f"Error:MONTH STATUS PRODUCT NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                        continue
                    for result in monthproduct_status:
                        totalmonthbaked += result.TotalBakedProducts
                        totalmonthsendout += result.TotalProductsSendOut
                    monthbakedgoal = totalmonthbaked >= self.totalmonthtobakeproductsgoal
                    monthsendoutgoal = totalmonthsendout >= self.totalmonthtosendoutproductsgoal

                    #year bakery status cheker
                    yearproduct_status = Products.query.filter_by(BakeryId=bakery.BakeryId).filter(
                        Products.TimeOfBakery >=last_8760_hours
                    ).all()
                    
                    if not yearproduct_status:
                        errors.append(f"Error:YEAR STATUS PRODUCT NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                        continue
                    for result in yearproduct_status:
                        totalyearbaked += result.TotalBakedProducts
                        totalyearsendout += result.TotalProductsSendOut
                    yearbakedgoal = totalyearbaked >= self.totalyeartobakeproductsgoal
                    yearsendoutgoal = totalyearsendout >= self.totalyeartosendoutproductsgoal

                    checker_status_data.append({
                        'bakeryid':bakery.BakeryId,
                        'daybakedgoal':daybakedgoal,
                        'daysendoutgoal':daysendoutgoal,
                        'monthbakedgoal':monthbakedgoal,
                        'monthsendout':monthsendoutgoal,
                        'yearbakedgoal':yearbakedgoal,
                        'yearsendoutgoal':yearsendoutgoal
                    })

            if errors:
                logging.error(f"Error:occurred in output_productdata,Error:{errors} HAS BEEN FOUND")
                return f'Completed with {len(errors)} error(s)',errors,checker_status_data  
            return checker_status_data
        except Exception as e:
                logging.error(f"Error:occurred in bakery cheker,Error:{e} HAS BEEN FOUND")
                return f"Error:{e} HAS BEEN FOUND",False


class dbDelivery:
        
    totalacceptedproducts = 0
    totaldeliverdproducts = 0
    totalbranchdeliverd = 0

    def __init__(self, adminid, DriverId, vicalplateNo,vicaltype,workingbakeryid,
                 totalworkers,totaldayacceptedproductsgoal,
                 totalmonthacceptedproductsgoal,totalyearacceptedproductsgoal,
                 totaldaydeliverdproductsgoal,totalmonthdeliverdproductsgoal,
                 totalyeardeliverdproductsgoal,vicaimage
                 ):
        self.adminid = adminid
        employee = Employee.query.filter_by(EmployeeId=DriverId).first()
        if employee:
            if employee.WorkingPositionName == None:
                self.DriverId  = DriverId
            else:
                logging.error(f"Error:Employee occupied for DriverId {DriverId}")
                raise ValueError(f"Error:Employee occupied for DriverId {DriverId}")
        else:
            logging.error(f"Error:Employee not found for DriverId{DriverId}")
            raise ValueError(f"Error:Employee not found for DriverId{DriverId}") 
        self.vicalplateNo = vicalplateNo
        self.vicaltype = vicaltype
        bakery = Bakery.query.filter_by(BakeryId=workingbakeryid).first()
        if bakery:
            self.workingbakeryid = bakery.BakeryId
        else:
            logging.error(f"Error:BAKERY NOT FOUND FOR BAKERY ID{workingbakeryid}")
        self.totalworkinghour = 0
        self.totalworkers = totalworkers
        self.totaldayacceptedproductsgoal = totaldayacceptedproductsgoal
        self.totalmonthacceptedproductsgoal = totalmonthacceptedproductsgoal
        self.totalyearacceptedproductsgoal = totalyearacceptedproductsgoal
        self.totaldaydeliverdproductsgoal = totaldaydeliverdproductsgoal
        self.totalmonthdeliverdproductsgoal = totalmonthdeliverdproductsgoal
        self.totalyeardeliverdproductsgoal = totalyeardeliverdproductsgoal
        self.vicalimage = vicaimage


    #gives the image of the delivery car    
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
    #insert delivery data into database
    def insert_deliverydata(self):
        try:
            delverydata = Delivery(
                DriverId=self.DriverId,AdminId=self.adminid ,VicalPlateNo=self.vicalplateNo,VicalType=self.vicaltype, VicalImage=self.vicalimage,
                WorkingBakeryId=self.workingbakeryid,TotalWorkingHours=self.totalworkinghour,TotalAcceptedProducts=self.totalacceptedproducts,
                TotalDeliveredProducts=self.totaldeliverdproducts,TotalBranchesDelivered=self.totalbranchdeliverd,
                TotalWorkers=self.totalworkers, TotalDayAcceptedProductsGoal=self.totaldayacceptedproductsgoal,
                TotalMonthAcceptedProductsGoal=self.totalmonthacceptedproductsgoal, TotalYearAcceptedProductsGoal=self.totalyearacceptedproductsgoal,
                TotalDayDeliveredProductsGoal=self.totaldaydeliverdproductsgoal, TotalMonthDeliveredProductsGoal=self.totalmonthdeliverdproductsgoal,
                TotalYearDeliveredProductsGoal=self.totalyeardeliverdproductsgoal
            )
            db.session.add(delverydata)
            db.session.commit()
            dbEmployee.update_employeedata(id=self.DriverId,co_name='WorkingPositionName',value=delverydata.VicalPlateNo)
            dbEmployee.update_employeedata(id=self.DriverId,co_name='WorkingPosition',value="delivery")
            dbEmployee.update_employeedata(id=self.DriverId,co_name='Role',value="driver")
            return 'successful',True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_deliverydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    #gives delivery data from database
    @classmethod
    def output_deliverydata(cls,adminid):
        try:
            deliveries=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                deliveries = Delivery.query.all()
            else:
                deliveries = Delivery.query.filter_by(AdminId=adminid).all()
            deliverydata = []
            for delivery in deliveries:
                deliverydata.append(
                    {
                        'time':datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                        'deliveryid': delivery.DeliveryId,
                        'driverid': delivery.DriverId,
                        'vicalplateno': delivery.VicalPlateNo,
                        'vicaltype': delivery.VicalType,
                        'vicalimage':delivery.VicalImage,
                        'workingbakeryid': delivery.WorkingBakeryId,
                        'totalworkinghours': delivery.TotalWorkingHours,
                        'totalacceptedproducts': delivery.TotalAcceptedProducts,
                        'totaldeliveredproducts': delivery.TotalDeliveredProducts,
                        'totalbranchesdelivered': delivery.TotalBranchesDelivered,
                        'deliverystartingdate': delivery.DeliveryStartingDate,
                        'totalworkers': delivery.TotalWorkers,
                        'totaldayacceptedproductsgoal': delivery.TotalDayAcceptedProductsGoal,
                        'totalmonthacceptedproductsgoal': delivery.TotalMonthAcceptedProductsGoal,
                        'totalyearacceptedproductsgoal': delivery.TotalYearAcceptedProductsGoal,
                        'totaldaydeliveredproductsgoal': delivery.TotalDayDeliveredProductsGoal,
                        'totalmonthdeliveredproductsgoal': delivery.TotalMonthDeliveredProductsGoal,
                        'totalyeardeliveredproductsgoal': delivery.TotalYearDeliveredProductsGoal,
                    }
                )
            return deliverydata
        except Exception as e:
            logging.error(f"Error:occurred in output_deliverydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS FOUND",False
    @classmethod
    def single_outputdeliverydata(cls,id):
        delivery = Delivery.query.filter_by(DeliveryId=id).first()
        deliverydata={
           'deliveryid': delivery.DeliveryId,
           'adminid':delivery.AdminId,
           'driverid': delivery.DriverId,
           'vicalplateno': delivery.VicalPlateNo,
           'vicaltype': delivery.VicalType,
           'workingbakeryid': delivery.WorkingBakeryId,
           'totalworkinghours': delivery.TotalWorkingHours,
           'totalacceptedproducts': delivery.TotalAcceptedProducts,
           'totaldeliveredproducts': delivery.TotalDeliveredProducts,
           'totalbranchesdelivered': delivery.TotalBranchesDelivered,
           'deliverystartingdate': delivery.DeliveryStartingDate,
           'totalworkers': delivery.TotalWorkers,
           'totaldayacceptedproductsgoal': delivery.TotalDayAcceptedProductsGoal,
           'totalmonthacceptedproductsgoal': delivery.TotalMonthAcceptedProductsGoal,
           'totalyearacceptedproductsgoal': delivery.TotalYearAcceptedProductsGoal,
           'totaldaydeliveredproductsgoal': delivery.TotalDayDeliveredProductsGoal,
           'totalmonthdeliveredproductsgoal': delivery.TotalMonthDeliveredProductsGoal,
           'totalyeardeliveredproductsgoal': delivery.TotalYearDeliveredProductsGoal,
        }
        return deliverydata
    #updates delivery data
    @classmethod
    def update_deliverydata(cls,id,co_name,value):
        try:
            delivery = Delivery.query.filter_by(DeliveryId=id).first()
            old_image_name = f'delivery{delivery.VicalPlateNo}.png'
            if delivery:
                if hasattr(delivery,co_name):
                    setattr(delivery,co_name,value)
                    if co_name == "DriverId":
                        employee2 = Employee.query.filter_by(EmployeeId=value).first()
                        if employee2.WorkingPositionName == None:
                            employee1 = Employee.query.filter_by(EmployeeId=delivery.DriverId).first()
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='WorkingPositionName',value=None)
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='WorkingPosition',value=None)
                            dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='Role',value=None)
                            
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='WorkingPositionName',value=delivery.DriverId)
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='WorkingPosition',value="delivery")
                            dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='Role',value="driver")
                            db.session.commit()
                            return f"Delivery data with id {id} has been updated",True
                        else:
                            return f"Error:Employee occupied:Delivery data with id {id} has not been updated",False
                    if co_name == "VicalPlateNo":
                        directory_path = r'C:\Users\outis\Desktop\Oneproject\static\image\employees'
                        # Add file extension to image name
                        current_file_path = os.path.join(directory_path, old_image_name)
                        new_image_name = f'delivery{delivery.VicalPlateNo}.png'
                        new_file_path = os.path.join(directory_path, new_image_name)
                        # Ensure paths are different before renaming
                        if current_file_path != new_file_path:
                            os.rename(current_file_path, new_file_path)
                        db.session.commit()
                    else:
                        db.session.commit()
                        return f"Delivery data with id {id} has been updated",True
                else:
                    return f"Error with column {co_name} UNIDENTEFINDE",False
            else:
                logging.error(f"Error:occurred in update_deliverydata,Error: delivery with id {id} NOT FOUND")
                return f"Error:delivery with id {id} NOT FOUND",False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_deliverydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deletes delivery data
    @classmethod
    def delete_deliverdata(cls,id):
        try:
            delivery = Delivery.query.filter_by(DeliveryId=id).first()
            if delivery:
                db.session.delete(delivery)
                db.session.commit()
                employee = Employee.query.filter_by(EmployeeId=delivery.DeliveryId).first()
                account = Account.query.filter_by(DeId=delivery.BakeryId).first()
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='WorkingPositionId',value=None)
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='WorkingPosition',value=None)
                dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='Role',value=None)
                dbAccount.delete_accountdata(id=account.AccountId)
                return f'Delivery with id {id} has been deleted',True
            else:
                logging.error(f"Error:occurred in delete_deliverdata,Delivery With This ID {id} Not Found")
                return f'Error: Delivery With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_deliverdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #calculate total product accepted & deliverd & total braches deliverd
    def set_totalproducts(self):
            try:
                with Session() as session:
                    errors = []
                    delivery_instance = Delivery.query.filter_by(VicalPlateNo=self.vicalplateNo).first()
                    if not delivery_instance:
                        logging.error(f"Error:occurred in set_totalproducts,Error: DELIVERY NOT FOUND")
                        return 'Error: DELIVERY NOT FOUND',False
                    
                    deliverid = delivery_instance.DeliveryId
                    trans_results = session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=deliverid).all()

                    for result in trans_results:
                        if  not result:
                            logging.error(f"Error:occurred in set_totalproducts,Error: TRANSACTION NOT FOUND FOR DELIVERY ID {deliverid}")
                            return f'Error: TRANSACTION NOT FOUND FOR DELIVERY ID {deliverid}',False
                        
                        transaction_instance = Transaction.query.filter_by(TransId=result.Transaction_id).first()

                        if not transaction_instance:
                            errors.append(f"Error:transaction_instance NOT FOUND WITH Transaction ID {result.Transaction_id}")
                            continue
                            
                        self.totalacceptedproducts += transaction_instance.AcceptedProductQuantity
                        self.totaldeliverdproducts += transaction_instance.DeliveredProductQuantity

                        if transaction_instance.BranchId:
                            self.totalbranchdeliverd += Transaction.query.filter_by(TransId=transaction_instance.TransId).count()
                    
                    delivery_instance.TotalAcceptedProducts = self.totalacceptedproducts
                    delivery_instance.TotalDeliveredProducts = self.totaldeliverdproducts
                    delivery_instance.TotalBranchesDelivered = self.totalbranchdeliverd

                    db.session.commit()
                    if errors:
                        logging.error(f"Error:occurred in set_totalproducts,Error:{errors} HAS BEEN FOUND")
                        return f'Completed with {len(errors)} error(s)',errors
                        
                    return f'successfull.',True
            except Exception as e:
                logging.error(f"Error:occurred in delivery set_totalproducts,Error:{e} HAS BEEN FOUND")
                return f"Error:{e} HAS BEEN FOUND",False
    def setproducts(self):
        schedule.every(24).hours.do(self.set_totalproducts)
        while True:
            schedule.run_pending()
            time.sleep(18)

    #gives product data from database
    @classmethod
    def output_productdata(cls,adminid):
        try:
            with Session() as session:
                errors = []
                deliveryes=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    deliveryes = Delivery.query.all()
                else:
                    deliveryes = Delivery.query.filter_by(AdminId=adminid).all()
                product_data = []
                now = datetime.now()
                last_24_hours = now - timedelta(hours=24)
                for delivery in deliveryes:
                    trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=delivery.DeliveryId).filter(
                        Product_BDB_Transaction_Sale.c.Time >= last_24_hours
                    ).all()
                    if not trans_result:
                        errors.append(f"Error:TRANSACTION NOT FOUND FOR DELIVERY ID {delivery.DeliveryId}")
                        continue

                    for result in trans_result:
                        product_id = result.Product_id
                        product = Products.query.filter_by(ProductId=product_id).first()
                        if not product:
                            errors.append(f"Error: PRODUCT NOT FOUND FOR PRODUCT ID {product_id}")
                            continue
                        trans_id = result.Transaction_id
                        acceptedtime = None
                        deliverdtime = None
                        transaction = Transaction.query.filter_by(TransId=trans_id).first()
                        if not transaction:
                            errors.append(f"TRANSACTION NOT FOUND FOR DBTRANSACTION ID {trans_id}")
                            continue
                        else:
                            acceptedtime = transaction.TransStartingTime
                            deliverdtime = transaction.TransEndingTime

                        product_data.append(
                            {
                                'time':now.strftime("%d/%m/%y  %H:%M:%S"),
                                "deliveryid":delivery.DeliveryId,
                                "adminid":delivery.AdminId,
                                "productid":product_id,
                                "productname":product.ProductName,
                                "totalproductaccepted":transaction.AcceptedProductQuantity,
                                "totalproductdeliverd":transaction.DeliveredProductQuantity,
                                "viclapaleteno":delivery.VicalPlateNo,
                                "acceptedfrom":result.Bakery_id,
                                "timeofacceptance":acceptedtime,
                                "deliverdto":result.Deliverd_id,
                                "timeofdelivery":deliverdtime
                            }
                        )
                if errors:
                    logging.error(f"Error:occurred in output_productdata,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)',errors,product_data
                return product_data
        except Exception as e:
            logging.error(f"Error:occurred in delivery output_productdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #gives day delivery status data
    @classmethod
    def day_deliverystatus(cls,adminid):
        try:
            with Session() as session:
                errors = []
                now = datetime.now()
                last_24_hours = now-timedelta(hours=24)
                deliveres=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    deliveres = Delivery.query.all()
                else:
                    deliveres = Delivery.query.filter_by(AdminId=adminid).all()
                daystatus = []
                for delivery in deliveres:
                    dayacceptedproductsinmonye = 0
                    daydeliveredproductsinmonye = 0
                    totalbranchesdelivered = 0
                    dayacceptedgoal = False
                    daydeliveredgoal = False
                    goaldata = cls.checker()
                    trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id = delivery.DeliveryId).filter(
                        Product_BDB_Transaction_Sale.c.Time >= last_24_hours
                    ).all()
                    if not trans_result:
                        errors.append(f"TRANSACTION NOT FOUND FOR DELIVERY ID {delivery.DeliveryId}")
                        continue
                    for data in goaldata:
                        if data['deliveryid'] == delivery.DeliveryId:
                            dayacceptedgoal = data["dayacceptedgoal"]
                            daydeliveredgoal = data["daydeliveredgoal"]

                    for result in trans_result:
                        transaction = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                        if not transaction:
                            errors.append(f"Error:TRANSACTION NOT FOUND FOR TRANSACTION ID {result.Transaction_id}")
                            continue
                        if result.Delivery_id is not None:
                            dayacceptedproductsinmonye +=  transaction.AcceptedProductQuantity
                        if result.Branch_id is not None:
                            daydeliveredproductsinmonye +=  transaction.DeliveredProductQuantity
                        if result.Branch_id is not None:
                            totalbranchesdelivered += session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id = delivery.DeilveryId).filter(
                                                            Product_BDB_Transaction_Sale.c.Time >= last_24_hours
                                                            ).count()
                    daystatus.append({
                            'date':now.strftime("%d/%m/%y"),
                            'deliveryid':delivery.DeliveryId,
                            'adminid':delivery.AdminId,
                            'driverid':delivery.DriverId,
                            'workingbakeryid':delivery.WorkingBakeryId,
                            'vicalplateNo':delivery.VicalPlateNo,
                            'dayacceptedproductsinmonye':dayacceptedproductsinmonye,
                            'daydeliveredproductsinmonye':daydeliveredproductsinmonye,
                            'totalbranchesdelivered':totalbranchesdelivered,
                            'dayacceptedgoal':dayacceptedgoal,
                            'daydeliverdgoal':daydeliveredgoal
                        })
                if errors:
                    logging.error(f"Error:occurred in day_deliverystatus,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)',errors, daystatus
                return daystatus
        except Exception as e:
            logging.error(f"Error:occurred in day_deliverystatus,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False



    #gives month delivery status data
    @classmethod
    def month_deliverystatus(cls,adminid):
        try:
            with Session() as session:
                errors = []
                deliveres=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    deliveres = Delivery.query.all()
                else:
                    deliveres = Delivery.query.filter_by(AdminId=adminid).all()
                monthstatus = []
                now = datetime.now()
                last_730_hours = now - timedelta(hours=730)

                for delivery in deliveres:
                    trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=delivery.DeliveryId).filter(
                        Product_BDB_Transaction_Sale.c.Time >= last_730_hours
                    ).all()
                    if not trans_result:
                        errors.append(f"Error:TRANSACTION NOT FOUND DELIVERY ID {delivery.DeliveryId}")
                        continue
                    
                    totalmonthacceptedproductsInmonye = 0
                    totalmonthdeliveredproductsInmonye = 0
                    totalmonthbranchesdelivered = 0 
                    monthacceptedgoal = False
                    monthdeliveredgoal =False
                    goaldata = cls.checker()
                    for result in trans_result:
                        transaction = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                        if not transaction:
                            errors.append(f"Error:TRANSACTION NOT FOUND FOR TRANSACTION ID {result.Transaction_id}")
                            continue
                        if result.Delivery_id is not None:
                            totalmonthacceptedproductsInmonye +=  transaction.AcceptedProductQuantity
                        if result.Branch_id is not None:
                            totalmonthdeliveredproductsInmonye +=  transaction.DeliveredProductQuantity
                        if result.Branch_id is not None:
                            totalmonthbranchesdelivered += session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=delivery.DeliveryId).filter(
                        Product_BDB_Transaction_Sale.c.Time >= last_730_hours
                    ).count()
                    for data in goaldata:
                        if data['deliverid'] == delivery.DeliveryId:
                            monthacceptedgoal = data['monthacceptedgoal']
                            monthdeliveredgoal = data['monthdeliveredgoal']

                    monthstatus.append({
                        'date':now.strftime("%m/%y"),
                        'deliveryid':delivery.DeliveryId,
                        'adminid':delivery.AdminId,
                        'driverid':delivery.DriverId,
                        'vicalplateno':delivery.VicalPlateNo,
                        'workingbakeryid':delivery.WorkingBakeryId,
                        'totalmonthacceptedproductsInmonye':totalmonthacceptedproductsInmonye,
                        'totalmonthdeliveredproductsInmonye':totalmonthdeliveredproductsInmonye,
                        'totalmonthbranchesdelivered':totalmonthbranchesdelivered,
                        'monthacceptedgoal':monthacceptedgoal,
                        'monthdeliveredgoal':monthdeliveredgoal
                    })
                if errors:
                    logging.error(f"Error:occurred in month_deliverystatus,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)', errors ,monthstatus
                return monthstatus
        except Exception as e:
            logging.error(f"Error:occurred in month_deliverystatus,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #gives year delivery status data
    @classmethod
    def year_deliverystatus(cls,adminid):
        try:
            with Session() as session:
                errors = []
                deliveryes=None
                admin=Admin.query.filter_by(AdminId=adminid).first()
                if not admin: 
                    logging.error(f"Admin not found for AdminId {adminid}") 
                    return f"Admin not found for AdminId {adminid}", False
                if admin.AdminType == "totaladmin":
                    deliveryes = Delivery.query.all()
                else:
                    deliveryes = Delivery.query.filter_by(AdminId=adminid).all()
                now = datetime.now()
                last_8760_hours = now - timedelta(hours=8760)
                yearstatus = []

                for delivery in deliveryes:
                    totalyearacceptedproductsInmonye =0
                    totalyeardeliveredproductsInmonye =0
                    totalyearbranchesdelivered = 0
                    yearacceptedgoal = False 
                    yeardeliveredgoal = False 
                    goaldata = cls.checker()
                    trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=delivery.DeliveryId).filter(
                        Product_BDB_Transaction_Sale.c.Time >= last_8760_hours
                    ).all()
                    if not trans_result:
                        errors.append(f'Error:TRANSACTION NOT FOUND FOR DELIVERY ID {delivery.DeliveryId}')
                        continue
                    for result in trans_result:
                        transaction = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                        if not transaction:
                            errors.append(f"Error:TRANSACTION NOT FOUND FOR TRANSACTION ID {result.Transaction_id}")
                            continue
                        
                        if result.Delivery_id is not None:
                            totalyearacceptedproductsInmonye +=  transaction.AcceptedProductQuantity
                        if result.Branch_id is not None:
                            totalyeardeliveredproductsInmonye +=  transaction.DeliveredProductQuantity
                        if result.Branch_id is not None:
                            totalyearbranchesdelivered += session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=delivery.DeliveryId).filter(
                                Product_BDB_Transaction_Sale.c.Time >= last_8760_hours
                            ).count()
                    for data in goaldata:
                        if data["deliveryid"] == delivery.DeliveryId:
                            yearacceptedgoal = data["yearacceptedgoal"]
                            yeardeliveredgoal = data["yeardeliverygoal"]
                    yearstatus.append(
                        {
                            'date':now.strftime("%y"),
                            'deliveryid':delivery.DeliveryId,
                            'adminid':delivery.AdminId,
                            'driverid':delivery.DriverId,
                            'vicalplateNo':delivery.VicalPlateNo,
                            'workingbakeryid':delivery.WorkingBakeryId,
                            'totalyearacceptedproductsInmonye':totalyearacceptedproductsInmonye,
                            'totalyeardeliveredproductsInmonye':totalyeardeliveredproductsInmonye,
                            'totalyearbranchesdelivered':totalyearbranchesdelivered,
                            'yearacceptedgoal':yearacceptedgoal,
                            'yeardeliveredgoal':yeardeliveredgoal
                        }
                    )
                if errors:
                    logging.error(f"Error:occurred in year_deliverystatus,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)',errors,yearstatus
                return yearstatus
        except Exception as e:
            logging.error(f"Error:occurred in year_deliverystatus,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #checkes day,month,year delivery data goals
    def checker(self):
        try:
            with Session() as session:
                errors = []
                now = datetime.now()
                last_24_hours = now - timedelta(hours=24)
                last_730_hours = now - timedelta(hours=730)
                last_8760_hours = now - timedelta(hours=8760)
                deliveres = Delivery.query.all()
                checker_status_data = []

                for delivery in deliveres:
                    deliveryid = delivery.DeliveryId
                    totaldayaccepted = 0
                    totaldaydeliverd = 0
                    totalmonthaccepted = 0
                    totalmonthdeliverd = 0
                    totalyearaccepted = 0
                    totalyeardeliverd = 0

                    #checkes dayly accepted and deliverd data
                    daytrans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=deliveryid).filter(
                        Product_BDB_Transaction_Sale.c.Time >= last_24_hours
                    ).all()
                    if not daytrans_result:
                        errors.append(f'Error:DAY TRANSACTIION NOT FOUND FOR DELIVERY ID {deliveryid}')
                        continue
                    
                    for result in daytrans_result:
                        transaction = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                        if not transaction:
                            errors.append(f"Error:TRANSACTION NOT FOUND FOR TRANSACTION ID {result.Transaction_id}")
                            continue
                        totaldayaccepted += transaction.AcceptedProductQuantity
                        totaldaydeliverd += transaction.DeliveredProductQuantity
                    dayacceptedgoal = totaldayaccepted >= self.totaldayacceptedproductsgoal
                    daydeliverdgoal = totaldaydeliverd >= self.totaldaydeliverdproductsgoal
                    
                    #checkes monthly accepted and deliverd data
                    monthtrans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=deliveryid).filter(
                        Product_BDB_Transaction_Sale.c.Time >= last_730_hours
                    ).all()
                    if not monthtrans_result:
                        errors.append(f'Error:MONTH TRANSACTIION NOT FOUND FOR DELIVERY ID{deliveryid}')
                        continue
                    
                    for result in monthtrans_result:
                        transaction = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                        if not transaction:
                            errors.append(f"Error:TRANSACTION NOT FOUND FOR TRANSACTION ID {result.Transaction_id}")
                            continue
                        totalmonthaccepted += transaction.AcceptedProductQuantity
                        totalmonthdeliverd += transaction.DeliveredProductQuantity
                    monthacceptedgoal = totalmonthaccepted >= self.totalmonthacceptedproductsgoal
                    monthdeliverdgoal = totalmonthdeliverd >= self.totalmonthdeliverdproductsgoal

                    #checkes yearly accepted and deliverd data
                    yeartrans_result =session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=deliveryid).filter(
                        Product_BDB_Transaction_Sale.c.Time >= last_8760_hours
                    ).all()
                    if not yeartrans_result:
                        errors.append(f'Error:YEAR TRANSACTIION NOT FOUND FOR DELIVERY ID {deliveryid}')
                        continue

                    for result in yeartrans_result:
                        transaction = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                        if not transaction:
                            errors.append(f"Error:TRANSACTION NOT FOUND FOR TRANSACTION ID {result.Transaction_id}")
                            continue
                        totalyearaccepted += transaction.AcceptedProductQuantity
                        totalyeardeliverd += transaction.DeliveredProductQuantity
                        
                    yearacceptedgoal = totalyearaccepted >= self.totalyearacceptedproductsgoal
                    yeardeliverygoal = totalyeardeliverd >= self.totalyeardeliverdproductsgoal

                    checker_status_data.append(
                        {
                            'deliveryid':deliveryid,
                            'dayacceptedgoal':dayacceptedgoal,
                            'daydeliveredgoal':daydeliverdgoal,
                            'monthacceptedgoal':monthacceptedgoal,
                            'monthdeliverdgoal':monthdeliverdgoal,
                            'yearacceptedgoal':yearacceptedgoal,
                            'yeardeliverygoal':yeardeliverygoal
                        }
                        )
                if errors:
                    logging.error(f"Error:occurred in checker,Error:{errors} HAS BEEN FOUND")
                    return f'Completed with {len(errors)} error(s)',errors ,checker_status_data
                return checker_status_data
        except Exception as e:
            logging.error(f"Error:occurred in checker,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False



class dbEmployee:

    totalpaidsalaryfroemployee = 0
    TotalWorkingHours = 0

    def __init__(self,adminid,employeefname,employeemname,employeelname, workingposition,workingpositionname,
                 dayworkinghourgoal,employeeimage,role,underid):
        self.adminid = adminid
        self.employeefname = employeefname
        self.employeemname = employeemname
        self.employeelname = employeelname
        self.workingposition = workingposition
        self.role = None
        self.underid= None
        self.workingpositionname = None
        if workingposition == "branch":

            branch = Branch.query.filter_by(BranchName=workingpositionname).first()
            if branch:
                self.workingpositionname = workingpositionname
                if branch.ControllerId == None:
                    self.role = role
                else:
                    self.role = "under"
                    self.underid = branch.ControllerId
                    logging.error(f"Error:Role occupied for Branch  dename {workingpositionname}")
            else:
                self.workingpositionname = None
                self.role = None
                self.underid = None
                logging.error(f"Error:Branch not found for from dename {workingpositionname}")
        elif workingposition == "delivery":
            delivery = Delivery.query.filter_by(VicalPlateNo=workingpositionname).first()
            if delivery:
                self.workingpositionname = workingpositionname
                if  delivery.DriverId == None:
                    self.role = role
                else:
                    self.role = "under"
                    self.underid = delivery.DriverId
                    logging.error(f"Error:Role occupied for Delivery  dename {workingpositionname}")
            else:
                self.workingpositionname = None
                self.underid = None
                self.role = None
                logging.error(f"Error:delivery not found for from dename {workingpositionname}")
        elif workingposition == "bakery":
            bakery = Bakery.query.filter_by(BakeryName=workingpositionname).first()
            if bakery:
                self.workingpositionname = workingpositionname
                if bakery.ManagerID == None:
                    self.role = role
                else:
                    self.role = "under"
                    self.underid = bakery.ManagerID
                    logging.error(f"Error:Role occupied for Bakery  dename {workingpositionname}")
            else:
                self.role = None
                self.underid = None
                self.workingpositionname = None
                logging.error(f"Error:bakery not found for from dename {workingpositionname}")
        elif workingposition == "admin":
            admin = Admin.query.filter_by(AdminName=workingpositionname).first()
            if admin:
                self.workingpositionname = workingpositionname
                if admin.AdminId == None:
                    self.role = role
                else:
                    self.role = "under"
                    self.underid = adminid.AdminId
                    logging.error(f"Error:Role occupied for Admin  dename {workingpositionname}")
            else:
                self.workingpositionname = None
                self.role = None
                self.underid = None
                logging.error(f"Error:admin not found for from dename {workingpositionname}")
        elif workingposition == "totaladmin":
            admin = Admin.query.filter_by(AdminName=workingpositionname).first()
            if admin:
                self.workingpositionname = workingpositionname
                if admin.AdminId == None:
                    self.role = role
                else:
                    self.role = "under"
                    self.underid = adminid.AdminId
                    logging.error(f"Error:Role occupied for Admin  dename {workingpositionname}")
            else:
                self.workingpositionname = None
                self.role = None
                self.underid = None
                logging.error(f"Error:admin not found for from dename {workingpositionname}")
        self.dayworkinghourgoal = dayworkinghourgoal
        self.employeeimage = employeeimage
    
    @classmethod
    def convert_image_to_binary(cls, image_file):
        if image_file is None:
            return None
        
        # Load the image from the uploaded file without converting to grayscale
        image = Image.open(image_file)
        
        # Save the image to a byte stream
        binary_stream = io.BytesIO()
        image.save(binary_stream, format='PNG', optimize=True, quality=85)
        binary_stream.seek(0)

        return binary_stream.getvalue()

    #insert employee data into database
    def insert_employeedata(self):
        try:
            employeedata = Employee(EmployeeFname=self.employeefname,AdminId=self.adminid,EmployeeLname=self.employeelname,
                                    Role=self.role,UnderId=self.underid,
                                    EmployeeMname=self.employeemname,EmployeeImage=self.employeeimage,WorkingPosition=self.workingposition,
                                    WorkingPositionName=self.workingpositionname,TotalWorkingHours=self.TotalWorkingHours,
                                    TotalPaidSalaryForEmployee=self.totalpaidsalaryfroemployee,DayWorkingHourGoal=self.dayworkinghourgoal)
            db.session.add(employeedata)
            db.session.commit()
            return 'successful',True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_employeedata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #update employee data
    @classmethod
    def update_employeedata(cls, id, co_name, value):
        try:
            employee = Employee.query.filter_by(EmployeeId=id).first()
            old_image_name = f'employee{employee.EmployeeFname}{employee.EmployeeMname}{employee.EmployeeLname}.png'
            if employee:
                if hasattr(employee, co_name):
                    setattr(employee, co_name, value)
                    
                    if co_name == "WorkingPositionName" or co_name == "WorkingPosition":
                        if employee.WorkingPositionName is not None:
                            return "Error:Department connected: You cannot update WorkingPosition or WorkingPositionName", False
                        else:
                            db.session.commit()
                    if co_name in ["EmployeeFname", "EmployeeMname", "EmployeeLname"]:
                        directory_path = r'C:\Users\outis\Desktop\Oneproject\static\image\employees'
                        # Add file extension to image name
                        current_file_path = os.path.join(directory_path, old_image_name)
                        new_image_name = f'employee{employee.EmployeeFname}{employee.EmployeeMname}{employee.EmployeeLname}.png'
                        print(new_image_name)
                        new_file_path = os.path.join(directory_path, new_image_name)
                        # Ensure paths are different before renaming
                        if current_file_path != new_file_path:
                            os.rename(current_file_path, new_file_path)
                        db.session.commit()
                    else:
                        db.session.commit()
                    return f"Employee data with id {id} has been updated", True
                
                else:
                    logging.error(f"Error: occurred in update_employeedata, Employee Column {co_name} Not Found")
                    return f'Error: Employee Column "{co_name}" Not Found', False
            else:
                logging.error(f"Error: occurred in update_employeedata, Employee With This ID {id} Not Found")
                return f'Error: Employee With This ID {id} Not Found', False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error: occurred in update_employeedata, Error: {e} HAS BEEN FOUND")
            return f"Error: {e} HAS BEEN FOUND", False


    #deletes employee data
    @classmethod
    def delete_employeedata(cls, id):
        try:
            if id is None:
                logging.error("Error: EmployeeId is None")
                return 'Error: EmployeeId cannot be None', False

            employee = Employee.query.filter_by(EmployeeId=id).first()

            if not employee:
                logging.error(f"Error: Employee with ID {id} Not Found")
                return f'Error: Employee with ID {id} Not Found', False

            branch = Branch.query.filter_by(ControllerId=id).first()
            delivery = Delivery.query.filter_by(DriverId=id).first()
            bakery = Bakery.query.filter_by(ManagerID=id).first()
            admin = Admin.query.filter_by(ControlerId=id).first()
            #account = Account.query.filter_by(EmployeeId=id).first()
            if branch or delivery or bakery or admin:
                if employee.WorkingPosition == 'branch':
                    return f'Error: Can not delete employee with ID {id} as they are linked with branch id {branch.BranchId}', False
                if employee.WorkingPosition == 'delivery':
                    return f'Error: Can not delete employee with ID {id} as they are linked with delivery id {delivery.DeliveryId}', False
                if employee.WorkingPosition == 'bakery':
                    return f'Error: Can not delete employee with ID {id} as they are linked with bakery id {bakery.BakeryId}', False
                if employee.WorkingPosition == 'admin':
                    return f'Error: Can not delete employee with ID {id} as they are linked with admin', False
                if employee.WorkingPosition == 'totaladmin':
                    return f'Error: Can not delete employee with ID {id} as they are linked with totaladmin', False
            else:
                db.session.delete(employee)
                db.session.commit()
                return f'Employee with ID {id} has been deleted', True
        except IntegrityError as e:
            return f'Error: Can not delete employee with ID {id} as they are linked to account ', False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error occurred in delete_employeedata: {e}")
            return f"Error: {e}", False
    
    #outputes employe data
    @classmethod
    def output_employeedata(cls,adminid):
        try:
            employees=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                employees = Employee.query.all()
            else:
                employees = Employee.query.filter_by(AdminId=adminid).all()
            employeedata = []
            for employee in employees:
                
                employeedata.append({
                    'time':datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                    'employeeid':employee.EmployeeId,
                    'adminid':employee.AdminId,
                    'employeefname':employee.EmployeeFname,
                    'employeemname':employee.EmployeeMname,
                    'employeelname':employee.EmployeeLname,
                    'employeeimage':employee.EmployeeImage,
                    'startingdate':employee.StartingDate,
                    'workingposition':employee.WorkingPosition,
                    'workingpositionname':employee.WorkingPositionName,
                    'role':employee.Role,
                    'underid':employee.UnderId,
                    #'accounts':employee.Accounts,
                    'totalworkinghours':employee.TotalWorkingHours,
                    'totalpaidsalaryforemployee':employee.TotalPaidSalaryForEmployee,
                    'dayworkinghourgoal':employee. DayWorkingHourGoal
                })
            return employeedata
        except Exception as e:
            logging.error(f"Error:occurred output_employeedata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    #gives one employee output
    @classmethod
    def single_outputemployeedata(cls,id):
        employee = Employee.query.filter_by(EmployeeId=id).first()
        employee_data = {
          'employeeid': employee.EmployeeId,
          'adminid':employee.AdminId,
          'employeefname': employee.EmployeeFname,
          'employeemname': employee.EmployeeMname,
          'employeelname': employee.EmployeeLname,
          'startingdate': employee.StartingDate,
          'workingposition': employee.WorkingPosition,
          'workingpositionname': employee.WorkingPositionName,
          'totalworkinghours': employee.TotalWorkingHours,
          'salary': employee.Salary,
          'totalPaidSalaryForEmployee': employee.TotalPaidSalaryForEmployee,
          'dayWorkinghourgoal': employee.DayWorkingHourGoal
        }
        return employee_data
    #set total paid salary for a single employee
    def set_totalpaidsalary(self):
        try:
            errors = []
            employee_instance = Employee.query.filter_by(EmployeeFname=self.employeefname, EmployeeMname=self.employeemname,
                                                          EmployeeLname=self.employeelname).first()

            for employee in employee_instance:
                salary = Salary.query.filter_by(EmployeeId=employee.EmployeeId).first()
                if not salary:
                    errors.append(f"Error:SALARY NOT FOUND FOR EMPLOYEE ID {employee.EmployeeId}")
                    continue
                self.totalpaidsalaryfroemployee += salary.PayedSalary
            employee_instance.TotalPaidSalaryForEmployee = self.totalpaidsalaryfroemployee
            db.session.commit()
            if errors:
                logging.error(f"Error:occurred set_totalpaidsalary,Error:{errors} HAS BEEN FOUND")
                return f'Completed with {len(errors)} error(s) ',errors
            return 'successful'
        except Exception as e:
            logging.error(f"Error:occurred set_totalpaidsalary,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    def setemployesalary(self):
        schedule.every(24).hours.do(self.set_totalpaidsalary)
        while True:
            schedule.run_pending()
            time.sleep(18)   

class dbSalary:
    totalpaidforemployee = 0
    totalpaidforallemployee = 0

    def __init__(self,adminid,employeeid,paidsalary):
        self.adminid = adminid
        self.paidsalary = paidsalary
        employee = Employee.query.filter_by(EmployeeId=employeeid).first()
        if employee:
            self.employeeid = employeeid
        else:
            logging.error(f"Error:Employee not found for employee id {self.employeeid}")
            raise ValueError(f"Error:Employee not found for employee id {self.employeeid}")
        self.monthsalary = employee.Salary
        self.workingposition = employee.WorkingPosition
    
    #inserting salary data
    def insert_salarydata(self):
        try:
            salarydata = Salary( AdminId=self.adminid,EmployeeId=self.employeeid,PayedSalary=self.paidsalary,
                                 MonthSalary=self.monthsalary,TotalPaidSalaryForEmployee =self.totalpaidforemployee,
                                TotalPaidSalaryForAllEmployees=self.totalpaidforallemployee)
            db.session.add(salarydata)
            db.session.commit()
            return 'successful',True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_salarydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEND FOUND",False
    
    #updatin salary data
    @classmethod 
    def update_salarydata(cls,id, co_name, value):
        try:
            salary = Salary.query.filter_by(SalaryId=id).first()
            if salary:
                if hasattr(salary, co_name):
                    setattr(salary, co_name, value)
                    db.session.commit()
                    return f"salary data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_salarydata,salary Column {co_name} Not Found")
                    return f'Error: salary Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_salarydata,salary With This ID {id} Not Found")
                return f'Error: salary With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_salarydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
        
    #deleting salary data
    @classmethod 
    def delete_salarydata(cls,id):
        try:
            salary = Salary.query.filter_by(SalaryId=id).first()
            if  salary:
                db.session.delete( salary)
                db.session.commit()
                return f' salary with ID {id} has been deleted',True
            else:
                logging.error(f"Error:occurred in delete_ salarydata, salary With This ID {id} Not Found")
                return f'Error:  salary With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_salarydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #seting salary  total paid for all employee
    def set_totalpaidforallemployee(self):
        try:
            errors=[]
            salaryes = Salary.query.all()
            for salary in salaryes:
                self.totalpaidforallemployee += salary.PayedSalary
            for s in salaryes:
                s.TotalPaidSalaryForAllEmployees = self.totalpaidforallemployee
                db.session.commit()
        except Exception as e:
            logging.error(f"Error:occurred in insert_salarydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEND FOUND",False
    def settotalallsalary(self):
        schedule.every(24).hours.do(self.set_totalpaidforallemployee)
        while True:
            schedule.run_pending()
            time.sleep(18)
    #seting salary  total paid for  employee
    def set_totalpaidsalaryForemployee(self):
        try:
            errors=[]
            employees = Employee.query.all()
            for employee in employees:
                salaryes = Salary.query.filter_by(EmployeeId=employee.EmployeeId).all()
                if not salaryes:
                    errors.append(f"Error:SALARY NOT FOUND FOR EMPLOYEE ID{employee.EmployeeId}")
                    continue
                for salary in salaryes:
                    self.totalpaidforemployee += salary.PayedSalary
                salaryes.TotalPaidSalaryForEmployee = self.totalpaidforemployee
                db.session.commit()
            if errors:
                logging.error(f"Error:occurred in set_totalpaidsalaryForemployee,Error:{errors} HAS BEEN FOUND")
                return f'Completed with {len(errors)} error(s) ',errors
            return 'successfull.'
        except Exception as e:
            logging.error(f"Error:occurred in insert_salarydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEND FOUND"
    def settotalsalary(self):
        schedule.every(24).hours.do(self.set_totalpaidsalaryForemployee)
        while True:
            schedule.run_pending()
            time.sleep(18) 
    
    #outputing salary data
    @classmethod
    def output_salarydata(cls,adminid):
        try:
            employees=None
            salarydata=None
            now = datetime.now()
            last_730_hours = now - timedelta(hours=730)
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                employees = Employee.query.all()
                salarydata = Salary.query.filter(
                Salary.PayDate >= last_730_hours
            ).all()
            else:
                employees = Employee.query.filter_by(AdminId=adminid).all()
                salarydata = Salary.query.filter_by(AdminId=adminid).filter(
                Salary.PayDate >= last_730_hours
            ).all()
            errors=[]
            employeesalarydata = []
            monthsalarydata = []
            allmonthsalarydata = []
            now = datetime.now()
            last_730_hours = now - timedelta(hours=730)
            checkerdata = cls.checker()
            for employee in employees:
                totalmonthpayed = 0
                totalmonthunpayed = 0
                #totalsalaryunpayedtoemployee = 0
                for data in checkerdata:
                    if employee.EmployeeId == data["employeeid"]:
                        totalmonthunpayed = len(checkerdata)
                employeesalary = Salary.query.filter_by(EmployeeId=employee.EmployeeId).first()
                if not employeesalary:
                    errors.append(f"Error:SALARY DATA NOT FOUND FOR EMPLOYEE ID{employee.EmployeeId}")
                    continue
                totalmonthpayed = Salary.query.filter_by(EmployeeId=employee.EmployeeId).count()
                employeesalarydata.append({
                    "date":datetime.now().strftime("%d/%m/%y"),
                    'employeeid':employee.EmployeeId,
                    'monthsalary':employeesalary.MonthSalary,
                    'employeeworkingposition':employee.WorkingPosition,
                    'employeeworkingpositionid':employee.WorkingPositionId,
                    'totalmonthpayed':totalmonthpayed,
                    'totalmonthunpayed':totalmonthunpayed,
                    'totalsalaryunpayedtoemployee':totalmonthunpayed * employeesalary.MonthSalary,
                    'totalsalarypayedforemployee':employeesalary.TotalPaidSalaryForEmployee,
                })
            totalbranchemployeepayedsalary=0
            totalbranchemployeeunpayedsalary=0
            totalbranchemployeeunpayedmonth = 0 
            totalbakeryeemployeepayedsalary=0
            totalbakeryeemployeeunpayedsalary=0
            totalbakeryemployeeunpayedmonth = 0 
            totaldeliveryeemployeepayedsalary=0
            totaldeliveryeemployeeunpayedsalary=0
            totaldeliveryemployeeunpayedmonth = 0 
            totalpaidsalaryforallemployees = 0

            for salary in salarydata:
                totalpaidsalaryforallemployees = salary.TotalPaidSalaryForAllEmployees
                for employee in employees:
                    if employee.WorkingPosition == "Branch":
                        if salary.EmployeeId == employee.EmployeeId:
                            totalbranchemployeepayedsalary += salary.PayedSalary
                    elif employee.WorkingPosition == "Bakery":
                        if salary.EmployeeId == employee.EmployeeId:
                            totalbakeryeemployeepayedsalary += salary.PayedSalary
                    elif employee.WorkingPosition == "Delivery":
                        if salary.EmployeeId == employee.EmployeeId:
                            totaldeliveryeemployeepayedsalary += salary.PayedSalary 
                    else:
                        errors.append(f"Error:EMPLOYEE WOKING POSITION {employee.WorkingPosition} DOSE NOT MATCH")
                        continue
                for data in checkerdata:
                    employeeid = data["employeeid"]
                    employee = Employee.query.filter_by(EmployeeId=employeeid).first()
                    if employee.WorkingPosition == "Branch":
                        totalbranchemployeeunpayedmonth = len(checkerdata) 
                        totalbranchemployeeunpayedsalary = len(checkerdata) * employee.Salary
                    elif employee.WorkingPosition == "Bakery":
                        totalbakeryemployeeunpayedmonth = len(checkerdata)
                        totalbakeryeemployeeunpayedsalary = len(checkerdata) * employee.Salary
                    elif employee.WorkingPosition == "Delivery":
                        totaldeliveryemployeeunpayedmonth = len(checkerdata)
                        totaldeliveryeemployeeunpayedsalary = len(checkerdata) * employee.Salary   

            monthsalarydata.append({
                "date":datetime.now().strftime("%d/%m/%y"),
                "totalbranchemployeepayedsalaryinmonth":totalbranchemployeepayedsalary,
                "totalbranchemployeeunpayedmonth":totalbranchemployeeunpayedmonth,
                "totalbranchemployeeunpayedsalary":totalbranchemployeeunpayedsalary,
                "totalbakeryeemployeeunpayedsalary":totalbakeryeemployeeunpayedsalary,
                "totalbakeryemployeeunpayedmonth":totalbakeryemployeeunpayedmonth,
                "totalbakeryeemployeepayedsalaryinmonth":totalbakeryeemployeepayedsalary,
                "totaldeliveryeemployeeunpayedsalary":totaldeliveryeemployeeunpayedsalary,
                "totaldeliveryemployeeunpayedmonth":totaldeliveryemployeeunpayedmonth,
                "totaldeliveryeemployeepayedsalaryinmonth":totaldeliveryeemployeepayedsalary,
                "totalsalarypayedinmonth":totalpaidsalaryforallemployees
            }) 
            allmonthsalarydata.append({
                  "date":now.strftime("%m"),
                  "data":monthsalarydata
            })          
            if errors:
                logging.error(f"Error:occurred in output_salarydata,Error:{errors} HAS BEEN FOUND")
                return f'Completed with {len(errors)} error(s) ',errors,employeesalarydata,allmonthsalarydata
            return employeesalarydata,allmonthsalarydata
        except Exception as e:
            logging.error(f"Error:occurred in output_salarydata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEND FOUND" ,False
    #check if salary payed or not
    @classmethod
    def checker(cls):
        try:
            errors = []
            salaryes = Salary.query.all()
            checkeddata =  []
            totalunpayedmonth = 0
            for salary in salaryes:
                data = []
                for month_number in range(1,13):
                    if salary.PayDate.month != month_number:
                        totalunpayedmonth +=1
                        data.append({
                            "employeeid":salary.EmployeeId,
                            "unpayedmonth":calendar.month_name[month_number],
                            "totalunpayedmonth":totalunpayedmonth
                        })
                if data:
                    checkeddata.append(data)
            if errors:
                logging.error(f"Error:occurred in salary checker,Error:{errors} HAS BEEN FOUND")
                return f'Completed with {len(errors)} error(s) ',errors,checkeddata
            return checkeddata
        except Exception as e:
            logging.error(f"Error:occurred in salary checker,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEND FOUND" 

class dbProducts:
    totalproductsendout=0
    totalproductleft = 0
    totalproductsendoutvalue=0
    def __init__(self, adminid,productname,bakeryid,totalbakedproducts,
                 productsusedforbakery,oneproductvalue,moneyusedtobaketheproduct,productimage):
        self.adminid=adminid
        self.productname=productname
        bakery  = Bakery.query.filter_by(BakeryId=bakeryid).first()
        if bakery:
            self.bakeryid=bakeryid
        else:
            logging.error(f"Error:bakery not found for bakery id {bakeryid}")
            raise ValueError(f"Error:bakery not found for bakery id {bakeryid}")
        self.bakeryid=bakeryid
        self.totalbakedproducts=totalbakedproducts
        self.totalbakedproductvalue= totalbakedproducts * oneproductvalue
        self.productusedforbakery=productsusedforbakery
        self.oneproductvalue=oneproductvalue
        self.moneyusedtobaketheproduct=moneyusedtobaketheproduct
        self.productimage = self.convert_image_to_binary(productimage) if productimage else None
    
    #gives the image of the employee
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
    
    #insert product data
    def insert_productdata(self):
        try:
            productdata =  Products(AdminId=self.adminid,ProductName=self.productname,BakeryId=self.bakeryid,TotalBakedProducts=self.totalbakedproducts,
                                TotalBakedProductValue=self.totalbakedproductvalue,TotalProductleft=self.totalproductleft,TotalProductsSendOut=self.totalproductsendout,
                               TotalProductsSendOutValue=self.totalproductsendoutvalue, ProductsUsedForBakery=self.productusedforbakery,
                               OneProductValue=self.oneproductvalue,MoneyUsedToBakeTheProduct=self.moneyusedtobaketheproduct)
            db.session.add(productdata)
            db.session.commit()
            return 'successful',True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_productdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #update product data
    @classmethod 
    def update_productdata(cls,id,co_name,value):
        try:
            product = Products.query.filter_by(ProductId=id).first()
            if product:
                if hasattr(product, co_name):
                    setattr(product, co_name, value)
                    db.session.commit()
                    return f"product data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_productdata,product Column {co_name} Not Found")
                    return f'Error: product Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_productdata,product With This ID {id} Not Found")
                return f'Error: product With This ID {id} Not Found',False               
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_productdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #delete product data
    @classmethod 
    def delete_productdata(cls,id):
        try:
            product = Products.query.filter_by(ProductId=id).first()
            if product:
                db.session.delete(product)
                db.session.commit()
                return f'product with ID {id} has been deleted',True
            else:
                logging.error(f"Error:occurred in delete_productdata,product With This ID {id} Not Found")
                return f'Error: product With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_productdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    # calculate the total send out products, product left,total send out product value 
    def set_productdata(self):
        try:
            errors=[]
            product_instance = Products.query.all()
            for product in product_instance:
                transactions = Transaction.query.filter_by(ProductId=product.ProductId).all()

                if not transaction:
                    errors.append(f"TRANSACTION NOT FOUND FOR PRODUCT ID {product.ProductId}")
                    continue
                for transaction in transactions:
                    self.totalproductsendout += transaction.AcceptedProductQuantity
                self.totalproductleft = product.TotalBakedProducts - self.totalproductsendout
                self.totalproductsendoutvalue = self.totalproductsendout * product.OneProductValue

                product.TotalProductsSendOut = self.totalproductsendout
                product.TotalProductleft= self.totalproductleft
                product.TotalProductsSendOutValue = self.totalproductsendoutvalue

                db.session.commit()
            if errors:
                logging.error(f"Error:occurred set_productdata,Error:{errors} HAS BEEN FOUND")
                return f'Completed with {len(errors)} error(s) ',errors
            return 'successful'
        except Exception as e:
            logging.error(f"Error:occurred set_productdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    def setproducts(self):
        schedule.every(24).hours.do(self.set_productdata)
        while True:
            schedule.run_pending()
            time.sleep(18000)
    #output product data
    @classmethod 
    def output_productdata(cls,adminid):
        try:
            products=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                products = Products.query.all()
            else:
                products = Products.query.filter_by(AdminId=adminid).all()
            productbakery_data = []
            for product in products:
                productbakery_data.append({
                   'time':datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                    "productid":product.ProductId,
                    "adminid":product. AdminId,
                    "productname":product.ProductName,
                    "bakeryid":product.BakeryId,
                    "totalbakedproducts":product.TotalBakedProducts,
                    "totalbakedproductvalue":product.TotalBakedProductValue,
                    "timeofbakery":product.TimeOfBakery,
                    "totalproductssendOut":product.TotalProductsSendOut,
                    "totalproductssendoutvalue":product.TotalProductsSendOutValue,
                    "productsusedforbakery":product. ProductsUsedForBakery,
                    "oneproductvalue":product.OneProductValue,
                    "moneyusedtobaketheproduct":product.MoneyUsedToBakeTheProduct
                })
            return productbakery_data
        except Exception as e:
            logging.error(f"Error:occurred in output_productdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False


class dbTransaction:
    transstage=""

    def __init__(self,bakeryid,adminid,deliveryid,branchid,productid,acceptedproductquantity,
                 deliveredproductquantity,transstartingtime,transendingtime,transgoal):
        self.bakeryid=bakeryid
        if not bakeryid == None:
            bakery  = Bakery.query.filter_by(BakeryId=bakeryid).first()
            if bakery:
               self.bakeryid=bakery.query.filter_by(bakeryid=bakeryid).first()
            else:
                logging.error(f"Error:bakery not found for bakery id {bakeryid}")
                raise ValueError(f"Error:bakery not found for bakery id {bakeryid}")
        else:
            bakeryid = None
        self.adminid=adminid
        if not deliveryid == None:
            delivery  = Delivery.query.filter_by(DeliveryId=deliveryid).first()
            if delivery:
               self.deliveryid=Delivery.query.filter_by(DeliveryId=deliveryid).first()
            else:
                logging.error(f"Error:delivery not found for delivery id {deliveryid}")
                raise ValueError(f"Error:delivery not found for delivery id {deliveryid}")
        else:
            deliveryid = None
        
        if not branchid == None:
            branch  = Branch.query.filter_by(BranchId=branchid).first()
            if branch:
                self.branchid=Branch.query.filter_by(BranchId=branchid).first()
            else:
                logging.error(f"Error:branch not found for branch id {branchid}")
                raise ValueError(f"Error:branch not found for branch id {branchid}")

        else:
            branchid = None
        if not productid == None:
            product  = Products.query.filter_by(ProductId=productid).first()
            if product:
                self.productid=Products.query.filter_by(ProductId=productid).first()
            else:
                logging.error(f"Error:product not found for product id {productid}")
                raise ValueError(f"Error:product not found for product id {productid}")

        else:
            productid = None
        self.acceptedproductquantity=acceptedproductquantity
        self.deliveredproductquantity=deliveredproductquantity
        product = Products.query.filter_by(ProductId=productid).first() 
        if product: 
            self.oneproductvalue = product.OneProductValue 
        else:
            self.oneproductvalue = 0
        self.totalacceptedproductvalueinmoney=self.oneproductvalue * self.acceptedproductquantity
        self.totaldeliveredproductvalueinmoney = self.oneproductvalue * self.deliveredproductquantity 
        self.transstartingtime=transstartingtime
        self.transendingtime=transendingtime
        self.transgoal= transgoal

    #inserting transaction data
    def insert_transactiondata(self):
        try:
            transaction = Transaction(BakeryId=self.bakeryid,AdminId=self.adminid,DeliveryId=self.deliveryid,BranchId=self.branchid,ProductId=self.productid,
                                      TransStage=self.transstage,TransStartingTime=self.transstartingtime, TransEndingTime=self.transendingtime,
                                       AcceptedProductQuantity=self.acceptedproductquantity,DeliveredProductQuantity=self.deliveredproductquantity,
                                       OneProductValue=self.oneproductvalue,TransGoal=self.transgoal,TotalAcceptedProductValueInMoney=self.totalacceptedproductvalueinmoney,
                                       TotalDeliveredProductValueInMoney=self.totaldeliveredproductvalueinmoney)
            db.session.add(transaction)
            db.session.commit()
            return 'successful',True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_transactiondata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #updating transaction data
    @classmethod 
    def update_transactiondata(cls,id,co_name,value):
        try:
            transaction =  Transaction.query.filter_by( TransId=id).first()
            if transaction:
                if hasattr(transaction, co_name):
                    setattr(transaction, co_name, value)
                    db.session.commit()
                    return f"transaction data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_transactiondata,transaction Column {co_name} Not Found")
                    return f'Error: transaction Column "{co_name}" Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_transactiondata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deleteing transaction data
    @classmethod 
    def delete_transactiondata(cls,id):
        try:
            transaction =  Transaction.query.filter_by( TransId=id).first()
            if transaction:
                db.session.delete(transaction)
                db.session.commit()
                return f'transaction with ID {id} has been deleted',True
            else:
                logging.error(f"Error:occurred in delete_transactiondata,product With This ID {id} Not Found")
                return f'Error: transaction With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_transactiondata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #outputing transaction data 
    @classmethod 
    def output_transactiondata(cls,adminid):
        try:
            transactions=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                transactions = Transaction.query.all()
            else:
                transactions = Transaction.query.filter_by(AdminId=adminid).all()
            transaction_data = []
            for transaction in transactions:
                transaction_data.append({
                    'time':datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                    "transid":transaction.TransId,
                    "adminid":transaction.AdminId,
                    "bakeryid":transaction.BakeryId,
                    "deliveryid":transaction.DeliveryId,
                    "branchid":transaction.BranchId,
                    "productid":transaction.ProductId,
                    "transstage":transaction.TransStage,
                    "transstartingtime":transaction.TransStartingTime,
                    "transendingtime":transaction.TransEndingTime,
                    "acceptedproductquantity":transaction.AcceptedProductQuantity,
                    "deliveredproductquantity":transaction.DeliveredProductQuantity,
                    "transgoal":transaction.TransGoal,
                })
            return transaction_data
        except Exception as e:
            logging.error(f"Error:occurred in output_transactiondata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #checkes transaction stage and set transaction stage
    @classmethod 
    def checker_seter(cls,status):
        goaldata=[]
        transactions = Transaction.query.all()
        for transaction in transactions:
            goal=False
            if status == True:
                goal=True
                transaction.TransStage = "finished"
                db.session.commit()
            else:
                transaction.TransStage = "inprocess"
                db.session.commit()
                goal=False
            goaldata.append({
                "transid":transaction.TransId,
                "goal":goal
            })
        return goaldata
    

class dbSale:
    
    def __init__(self,adminid,productid,bakeryid,salebranchid,totalproductquantitysold,
                 totalsoldemoney,oneproductvalue,transactionid):
        self.adminid=adminid
        product = Products.query.filter_by(ProductId=productid).first()
        if product:
            self.productid=productid
        else:
            logging.error(f"Error:Product not found for product id {productid}")
            raise ValueError(f"Error:Product not found for product id {productid}")
        
        bakery  = Bakery.query.filter_by(BakeryId=bakeryid).first()
        if bakery:
            self.bakeryid=bakeryid
        else:
            logging.error(f"Error:bakery not found for bakery id {bakeryid}")
            raise ValueError(f"Error:bakery not found for bakery id {bakeryid}")
        
        branch  = Branch.query.filter_by(BakeryId=bakeryid).first()
        if branch:
            self.salebranchid=salebranchid
        else:
            logging.error(f"Error:branch not found for branch id {salebranchid}")
            raise ValueError(f"Error:branch not found for branch id {salebranchid}")
        self.salebranchid=salebranchid
        self.totalproductquantitysold=totalproductquantitysold
        self.totalsoldemoney=totalsoldemoney
        self.oneproductvalue=oneproductvalue
        self.transactionid=transactionid

    #inserting data into database
    def insert_saledata(self):
        try:
            sale = Sale(AdminId=self.adminid,BakeryId=self.bakeryid,ProductId=self.productid,SaleBranchId=self.salebranchid,
                        TotalProductQuantitySold=self.totalproductquantitysold,TotalSaledMoney=self.totalsoldemoney,OneProductValue=self.oneproductvalue,
                        TransactionId=self.transactionid)
            db.session.add(sale)
            db.session.commit()
            return "successful",True
            
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_saledata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #updating sale data 
    @classmethod 
    def update_saledata(cls,id,co_name,value):
        try:
            sale = Sale.query.filter_by(SaleId=id).first()
            if sale:
                if hasattr(sale,co_name):
                    setattr(sale,co_name,value)
                    db.session.commit()
                    return f"sale data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_ saledata,sale Column {co_name} Not Found")
                    return f'Error: sale Column "{co_name}" Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_ saledata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #deleting sale data
    @classmethod 
    def delete_saledata(cls,id):
        try:
            sale = Sale.query.filter_by(SaleId=id).first()
            if sale:
                db.session.delete(sale)
                db.session.commit()
                return f'sale with ID {id} has been deleted',True
            else:
                logging.error(f"Error:occurred in delete_saledata,product With This ID {id} Not Found")
                return f'Error: sale With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_ saledata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #output sale data
    @classmethod 
    def output_saledata(cls,adminid):
        try:
            sales=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                sales = Sale.query.all()
            else:
                sales = Sale.query.filter_by(AdminId=adminid).all()
            sale_data = []
            for sale in sales:
                sale_data.append({
                    'time':datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                    "saleid":sale.SaleId,
                    "adminid":sale.AdminId,
                    "saletime":sale.SaleTime,
                    "productid":sale.ProductId,
                    "bakeryid":sale.BakeryId,
                    "salebranchid":sale.SaleBranchId,
                    "totalproductquantitysold":sale.TotalProductQuantitySold,
                    "totalsaledmoney":sale.TotalSaledMoney,
                    "oneproductvalue":sale.OneProductValue,
                    "transactionid":sale.TransactionId
                })
            return sale_data
        except Exception as e:
            logging.error(f"Error:occurred in insert_ saledata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False


class dbStatus:
    #inserting status data
    def insert_statusdata(self):
        with Session() as session:
            errors=[]
            now = datetime.now()
            last_8760_hours = now - timedelta(hours=8760)
            branches = Branch.query.all()
            deliveres = Delivery.query.all()
            bakeryes = Bakery.query.all()
            #inserting branch status data
            def insert_branchstatusdata(self):
                try:
                    for branch in branches:
                        costs = Cost.query.filter_by(DeId=branch.BranchId).filter(
                            Cost.PurchasedDate >= last_8760_hours
                        ).all()
                        if not costs:
                            errors.append(f"COST NOT FOUND FOR BRANCH ID {branch.BranchId}")
                            continue
                        sales = Sale.query.filter_by(SaleBranchId=branch.BranchId).filter(
                                Sale. SaleTime  >= last_8760_hours
                        ).all()
                        if not sales:
                            errors.append(f"SALE NOT FOUND FOR BRANCH ID {branch.BranchId}")
                            continue
                        trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Branch_id=branch.BranchId).filter(
                            Product_BDB_Transaction_Sale.c.Time >= last_8760_hours
                        ).all()
                        if not trans_result:
                            errors.append(f"Product_BDB_Transaction_Sale NOT FOUND FOR BRANCH ID {branch.BranchId}")
                            continue
                        adminid = branch.AdminId
                        totalyearsale = 0
                        totalyearprofit = 0
                        totalyearcost = 0
                        totalyearlose = 0
                        totalyearaccepted = 0
                        for cost in costs:
                            if cost.DeName == "branch":
                                totalyearcost += cost.CostPrice
                            else:
                                continue
                        for sale in sales:
                            totalyearsale += sale.TotalSaledMoney
                        for result in trans_result:
                            transaction = Transaction.query.filter_by(TransId=result.Transaction_id).first()
                            totalyearaccepted += transaction.AcceptedProductQuantity
                        totalpl = totalyearsale - totalyearcost
                        if totalpl >= 0:
                            totalyearprofit = totalpl
                            totalyearlose = 0
                        else:
                            totalyearlose = totalpl
                            totalyearprofit = 0
                        branchstatusdata =  Status(AdminId=adminid,DeName='branch',DeId=branch.BranchId,TotalYearSale=totalyearsale,
                                                TotalYearProfit=totalyearprofit,TotalYearLoss=totalyearlose,
                                                TotalYearCost=totalyearcost,TotalYearAccepted=totalyearaccepted)
                        db.session.add(branchstatusdata)
                        db.session.commit()
                        return "successful",True
                    if errors:
                        logging.error(f"Error:occurred in insert_branchstatusdata,Error:{errors} HAS BEEN FOUND")
                        return f'Completed with {len(errors)} error(s)',errors
                except Exception as e:
                    db.session.rollback()
                    logging.error(f"Error:occurred in insert_branchstatusdata,Error:{e} HAS BEEN FOUND")
                    return f"Error:{e} HAS BEEN FOUND",False
            #calling insert_branchstatusdata      
            insert_branchstatusdata(self)

            #inserting delivery status data
            def insert_deliverystatusdata(self):
                try:
                    for delivery in deliveres:
                        costs = Cost.query.filter_by(DeId=delivery.DeliveryId).filter(
                            Cost.PurchasedDate >= last_8760_hours
                        ).all
                        if not costs:
                            errors.append(f"COST NOT FOUND FOR DELIVERY ID {delivery.DeliveryId}")
                            continue
                        trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Delivery_id=delivery.DeliveryId).filter(
                            Product_BDB_Transaction_Sale.c.Time >= last_8760_hours
                        ).all()
                        if not trans_result:
                            errors.append(f"Product_BDB_Transaction_Sale  NOT FOUND FOR BRANCH ID {delivery.DeliveryId}")
                            continue
                        adminid = delivery.AdminId
                        totalyearcost = 0
                        totalyearaccepted = 0
                        totalyeardelivered = 0

                        for cost in costs:
                            totalyearcost += cost.CostPrice
                        for result in trans_result:
                            transaction =  Transaction.query.filter_by(TransId=result.Transaction_id).first()
                            totalyearaccepted += transaction.AcceptedProductQuantity
                            totalyeardelivered += transaction.DeliveredProductQuantity
                        deliverystatusdata = Status(AdminId=adminid,DeName="delivery",Deid=delivery.DeliveryId,TotalYearCost=totalyearcost,
                                                    TotalYearAccepted=totalyearaccepted,TotalYearDelivered=totalyeardelivered)
                        db.session.add(deliverystatusdata)
                        db.session.commit()
                        return "successful",True
                    if errors:
                        db.session.rollback()
                        logging.error(f"Error:occurred in insert_deliverystatusdata,Error:{errors} HAS BEEN FOUND")
                        return f'Completed with {len(errors)} error(s)',errors
                except Exception as e:
                    logging.error(f"Error:occurred in insert_deliverystatusdata,Error:{e} HAS BEEN FOUND")
                    return f"Error:{e} HAS BEEN FOUND",False
            #calling insert_deliverystatusdata
            insert_deliverystatusdata(self)
            
            #inserting delivery status data
            def insert_bakerystatusdata(self):
                try:
                   for bakery in bakeryes:
                        costs = Cost.query.filter_by(DeId=bakery.BakeryId).filter(
                            Cost.PurchasedDate >= last_8760_hours
                        ).all()
                        if not costs:
                            errors.append(f"COST NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                            continue
                        trans_result = session.query(Product_BDB_Transaction_Sale).filter_by(Bakery_id=bakery.BakeryId).filter(
                            Product_BDB_Transaction_Sale.c.Time >= last_8760_hours
                        ).all()
                        if not trans_result:
                            errors.append(f"Product_BDB_Transaction_Sale NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                            continue
                        products= Products.query.filter_by(BakeryId=bakery.BakeryId).filter(
                            Products.TimeOfBakery >= last_8760_hours
                        ).all()
                        if not products:
                            errors.append(f"PRODUCTS NOT FOUND FOR BAKERY ID {bakery.BakeryId}")
                            continue
                        adminid = bakery.AdminId
                        totalyearcost = 0
                        totalyearsendout = 0
                        totalyearbaked = 0
                        for cost in costs:
                            totalyearcost += cost.CostPrice

                        for result in trans_result:
                            transaction =  Transaction.query.filter_by(TransId=result.Transaction_id).first()
                            totalyearsendout += transaction.AcceptedProductQuantity
                        for product in products:
                            totalyearbaked += product.TotalBakedProducts
                        bakerystatusdata = Status(AdminId=adminid,DeName="delivery",DeId=bakery.BakeryId,TotalYearCost=totalyearcost,
                                                    TotalYearSendOut=totalyearsendout,TotalYearBaked=totalyearbaked)
                        db.session.add(bakerystatusdata)
                        db.session.commit()
                        return "successful",True
                   if errors:
                        logging.error(f"Error:occurred in insert_bakerystatusdata,Error:{errors} HAS BEEN FOUND")
                        return f'Completed with {len(errors)} error(s)',errors
                except Exception as e:
                    db.session.rollback()
                    logging.error(f"Error:occurred in insert_bakerydata,Error:{e} HAS BEEN FOUND")
                    return f"Error:{e} HAS BEEN FOUND",False
            #calling insert_bakerystatusdata
            insert_bakerystatusdata(self)
    #updating status data
    def setinsertstatusdata(self):
        schedule.every(24).hours.do(self.insert_statusdata)
        while True:
            schedule.run_pending()
            time.sleep(18000)
    #updating status data
    @classmethod      
    def update_statusdata(cls,id,co_name,value):
        try:
            status = Status.query.filter_by(StatusId=id).first()
            if status:
                if hasattr(status,co_name):
                    setattr(status,co_name,value)
                    return f"status data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_statusdata,status Column {co_name} Not Found")
                    return f'Error: Status Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_statusdata,status With This ID {id} Not Found")
                return f'Error: status With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_statusdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deleting status data
    @classmethod 
    def delete_statusdata(cls,id):
        try:
           status = Status.query.filter_by(StatusId=id).first()
           if status:
               db.session.delete(status)
               db.session.commit()
               return f'status with ID {id} has been deleted',True
           else:
                logging.error(f"Error:occurred in delete_statusdata,Status With This ID {id} Not Found")
                return f'Error: Status With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_statusdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #outputing status data
    @classmethod 
    def output_statusdata(cls,adminid):
        try:
            statuses=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                statuses = Status.query.all()
            else:
                statuses = Status.query.filter_by(AdminId=adminid).all()
            statusdata =[]
            for status in statuses:
                statusdata.append({
                    'time':datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                    "statusid":status.StatusId,
                    "adminid":status.AdminId,
                    "dename":status.DeName,
                    "deid":status.DeId,
                    "TotalYearSale":status.TotalYearSale,
                    "TotalYearProfit":status.TotalYearProfit,
                    "TotalYearLoss":status.TotalYearLoss,
                    "TotalYearCost":status.TotalYearCost,
                    "TotalYearBaked":status.TotalYearBaked,
                    "TotalYearAccepted":status.TotalYearAccepted,
                    "TotalYearSendOut":status.TotalYearSendOut,
                    "TotalYearDelivered":status.TotalYearDelivered,
                })
            return statusdata
        except Exception as e:
            logging.error(f"Error:occurred in output_statusdataoutput_statusdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False


class dbAsset:

    totalbakeryassetvalue = 0
    totalbranchassetvalue = 0
    totaldeliveryassetvalue = 0
    totalcompanyassetvalue = 0

    def __init__(self,adminid,ownerdename,ownerid,assetname,numberofasset,assettype,
                 assetvalue,location,assetstatus):
        self.adminid= adminid
        self.ownerdename = ownerdename
        if ownerdename == "branch":
            branch = Branch.query.filter_by(BranchId=ownerid).first()
            if branch:
                self.ownerid=ownerid
            else:
                logging.error(f"Error:Branch not found for from ownerid {ownerid}")
                raise ValueError(f"Error:Branch not found for from ownerid {ownerid}")
        elif ownerdename == "delivery":
            delivery = Delivery.query.filter_by(DeliveryId=ownerid).first()
            if delivery:
                self.ownerid=ownerid
            else:
                logging.error(f"Error:delivery not found for from ownerid {ownerid}")
                raise ValueError(f"Error:delivery not found for from ownerid {ownerid}")
        elif ownerdename == "bakery":
            bakery = Bakery.query.filter_by(BakeryId=ownerid).first()
            if bakery:
                self.ownerid=ownerid
            else:
                logging.error(f"Error:bakery not found for from ownerid {ownerid}")
                raise ValueError(f"Error:bakery not found for from ownerid {ownerid}")
        elif ownerdename == "admin":
            admin = Admin.query.filter_by(AdminId=ownerid).first()
            if admin:
                self.ownerid=ownerid
            else:
                logging.error(f"Error:admin not found for from ownerid {ownerid}")
                raise ValueError(f"Error:admin not found for from ownerid {ownerid}")
        elif ownerdename == "totaladmin":
            admin = Admin.query.filter_by(AdminId=ownerid).first()
            if admin:
                self.ownerid=ownerid
            else:
                logging.error(f"Error:admin not found for from ownerid {ownerid}")
                raise ValueError(f"Error:admin not found for from ownerid {ownerid}")
        self.assetname = assetname
        self.numberofasset = numberofasset
        self.assettype = assettype
        self.assetvalue = assetvalue
        self.location = location
        self.assetstatus = assetstatus
        if numberofasset != 0:
            self.totalenteredassetvalue= numberofasset * assetvalue

    #insert asset data also set totalbranchassetvalue,totaldeliveryassetvalue,totalbakeryassetvalue
    def insert_assetdata(self):
        try:
            assets = Asset.query.filter_by(OwnerDeName=self.ownerdename,OwnerId=self.ownerid).all()
            for asset in assets:
                if self.ownerdename == "branch":
                    self.totalbranchassetvalue += asset.AssetValue
                elif self.ownerdename == "delivery":
                    self.totaldeliveryassetvalue += asset.AssetValue
                elif self.ownerdename == "bakery":
                    self.totalbakeryassetvalue += asset.AssetValue
                else:
                    raise ValueError(f"ownerdename {self.ownerdename} does not match any department")
                
            assetdata = Asset(AdminId=self.adminid,OwnerDeName=self.ownerdename,OwnerId=self.ownerid,AssetName=self.assetname,
                              NumberOfAsset=self.numberofasset,AssetType=self.assettype,AssetValue=self.assetvalue,
                              TotalEnteredAssetValue=self.totalenteredassetvalue,Location=self.location,AssetStatus=self.assetstatus,
                              TotalBakeryAssetValue=self.totalbakeryassetvalue,TotalDeliveryAssetValue=self.totaldeliveryassetvalue,
                              TotalBranchAssetValue=self.totalbranchassetvalue,TotalCompanyAssetValue=self.totalcompanyassetvalue)
            db.session.add(assetdata)
            db.session.commit()
            return "successful",True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_assetdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #updating asset data
    @classmethod
    def update_assetdata(cls,id,co_name,value):
        try:
            asset = Asset.query.filter_by(AssetId=id).first()

            if asset:
                if hasattr(asset,co_name):
                    setattr(asset,co_name,value)
                    db.session.commit()
                    return f"asset data with id {id} has been updated",True
                else:
                        logging.error(f"Error:occurred in update_assetdata,asset Column {co_name} Not Found")
                        return f'Error: asset Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_assetdata,asset With This ID {id} Not Found")
                return f'Error: asset With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_assetdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deleting asset data
    @classmethod
    def delete_assetdata(cls,id):
        try:
            asset = Asset.query.filter_by(AssetId=id).first()
            if asset:
                db.session.delete(asset)
                db.session.commit()
                return f"asset with id {id} has been deleted",True
            else:
                logging.error(f"Error:occurred in delete_assetdata,asset With This ID {id} Not Found")
                return f'Error: asset With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_assetdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #outputing asset data
    @classmethod
    def output_assetdata(cls,adminid):
        try:
            assets=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                assets = Asset.query.all()
            else:
                assets = Asset.query.filter_by(AdminId=adminid).all() 
            assetdata = []
            for asset in assets:
                assetdata.append({
                    "time":datetime.now().strftime("%d/%m/%y  %H:%M:%S"),
                    "assetid":asset.AssetId,
                    "adminad":asset.AdminId,
                    "ownerdename":asset.OwnerDeName,
                    "ownerid":asset.OwnerId,
                    "assetname":asset.AssetName,
                    "owneddate":asset.OwnedDate,
                    "numberofasset":asset.NumberOfAsset,
                    "assettype":asset.AssetType,
                    "assetvalue":asset.AssetValue,
                    "totalenteredassetvalue":asset.TotalEnteredAssetValue,
                    "location":asset.Location,
                    "assetstatus":asset.AssetStatus,
                    "totalbakeryassetvalue ":asset.TotalBakeryAssetValue,
                    "totaldeliveryassetvalue ":asset.TotalDeliveryAssetValue,
                    "totalbranchassetvalue":asset.TotalBranchAssetValue,
                    "totalcompanyassetValue":asset.TotalCompanyAssetValue,
                })
                return assetdata
        except Exception as e:
            logging.error(f"Error:occurred in delete_assetdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

class dbApp:
    def insert_appdata(self):
        #this data will be inserted from the telegram bot
        pass

class dbAccount:
    def __init__(self,adminid,dename,deid,password,phonenumber):
        self.adminid = adminid
        self.dename=dename
        if dename == "branch":
            account = Account.query.filter_by(DeName="branch",DeId=deid).first()
            if not account:
                branch = Branch.query.filter_by(BranchId=deid).first()
                if branch:
                    self.deid=deid
                    self.employeeid=branch.ControllerId
                    self.role="user"
                else:
                    logging.error(f"Error:Branch not found for from deid {deid}")
                    raise ValueError(f"Error:Branch not found for from deid {deid}")
            else:
                logging.error(f"Error:Account already exist for deid {deid}")
                raise ValueError(f"Error:Account already exist for deid {deid}")
        if dename == "delivery":
            account = Account.query.filter_by(DeName="delivery",DeId=deid).first()
            if not account:
                delivery = Delivery.query.filter_by(DeliveryId=deid).first()
                if delivery:
                    self.deid=deid
                    self.employeeid=delivery.DriverId
                    self.role="user"
                else:
                    logging.error(f"Error:Delivery not found for from deid {deid}")
                    raise ValueError(f"Error:Delivery not found for from deid {deid}")
            else:
                logging.error(f"Error:Account already exist for deid {deid}")
                raise ValueError(f"Error:Account already exist for deid {deid}")
        if dename == "bakery":
            account = Account.query.filter_by(DeName="bakery",DeId=deid).first()
            if not account:
                bakery = Bakery.query.filter_by(BakeryId=deid).first()
                if bakery:
                    self.deid=deid
                    self.employeeid=bakery.ManagerID
                    self.role="user"
                else:
                    logging.error(f"Error:Bakery not found for from deid {deid}")
                    raise ValueError(f"Error:Bakery not found for from deid {deid}")
            else:
                logging.error(f"Error:Account already exist for deid {deid}")
                raise ValueError(f"Error:Account already exist for deid {deid}")
        if dename == "admin":
            account = Account.query.filter_by(DeName="admin",DeId=deid).first()
            if not account:
                admin = Admin.query.filter_by(AdminId=deid).first()
                if admin:
                    self.deid=deid
                    self.employeeid=admin.ControlerId
                    self.role="admin"
                else:
                    logging.error(f"Error:Admin not found for from deid {deid}")
                    raise ValueError(f"Error:Admin not found for from deid {deid}")
            else:
                logging.error(f"Error:Account already exist for deid {deid}")
                raise ValueError(f"Error:Account already exist for deid {deid}")
        if dename == "totaladmin":
            account = Account.query.filter_by(DeName="totaladmin",DeId=deid).first()
            if not account:
                admin = Admin.query.filter_by(AdminId=deid).first()
                if admin:
                    self.deid=deid
                    self.employeeid=admin.ControlerId
                    self.role="totaladmin"
                else:
                    logging.error(f"Error:Admin not found for from deid {deid}")
                    raise ValueError(f"Error:Admin not found for from deid {deid}")
            else:
                logging.error(f"Error:Account already exist for deid {deid}")
                raise ValueError(f"Error:Account already exist for deid {deid}")
        self.password=password
        self.phonenumber=phonenumber

    #inserting acceount data
    def insert_accountdata(self):
        try:
            salt = bcrypt.gensalt()
            hashedpassword = bcrypt.hashpw(str(self.password).encode('utf-8'),salt)
            accountdata = Account(AdminId=self.adminid,DeName=self.dename,DeId=self.deid,EmployeeId=self.employeeid,
                                   PasswordHash=hashedpassword,PhoneNumber=self.phonenumber)
            db.session.add(accountdata)
            db.session.commit()
            if self.dename == "branch":
                dbBranch.update_branchdata(id=self.deid,co_name="AccountId",value=accountdata.AccountId)
            if self.dename == "bakery":
                dbBakery.update_bakerydata(id=self.deid,co_name="AccountId",value=accountdata.AccountId)
            if self.dename == "delivery":
                dbDelivery.update_deliverydata(id=self.deid,co_name="AccountId",value=accountdata.AccountId)
            if self.dename == "admin":
                dbAdmin.update_admindata(id=self.deid,co_name="AccountId",value=accountdata.AccountId,creatorid=self.adminid)
            if self.dename == "totaladmin":
                dbAdmin.update_admindata(id=self.deid,co_name="AccountId",value=accountdata.AccountId,creatorid=self.adminid)
            return "Account data inserted successfully", True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_accounddata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #updating account data
    @classmethod
    def update_accountdata(cls,id,co_name,value):
        try:
            account = Account.query.filter_by(AccountId=id).first()
            if account:
                if hasattr(account,co_name):
                    account.UpdatedDate=datetime.now()
                    if co_name == "PasswordHash":
                        salt = bcrypt.gensalt()
                        hashedpassword = bcrypt.hashpw(value.encode('utf-8'),salt)
                        setattr(account,co_name,hashedpassword)
                        db.session.commit()
                    elif co_name == "Status":
                        if value in ["inactive", "suspended"]:
                            salt = bcrypt.gensalt()
                            pss = "######"
                            hashedpassword = bcrypt.hashpw(pss.encode('utf-8'),salt)
                            account.PasswordHash = hashedpassword
                            setattr(account,co_name,value)
                            db.session.commit()
                        else:
                            setattr(account, co_name, value)
                            db.session.commit()
                    else:
                        setattr(account,co_name,value)
                        db.session.commit()
                    return f"account data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_accountdata,account Column {co_name} Not Found")
                    return f'Error: account Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_accountdata,account With This ID {id} Not Found")
                return f'Error: account With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_accountdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deleteing accrout data 
    @classmethod
    def delete_accountdata(cls,id):
        try:
            account = Account.query.filter_by(AccountId=id).first()
            if account:
                db.session.delete(account)
                db.session.commit()
                if account.DeName == "branch":
                    dbBranch.update_branchdata(id=account.DeId,co_name="AccountId",value=None)
                if account.DeName == "bakery":
                    dbBakery.update_bakerydata(id=account.DeId,co_name="AccountId",value=None)
                if account.DeName == "delivery":
                    dbDelivery.update_deliverydata(id=account.DeId,co_name="AccountId",value=None)
                if account.DeName == "admin":
                    dbAdmin.update_admindata(id=account.DeId,co_name="AccountId",value=None)
                if account.DeName == "totaladmin":
                    dbAdmin.update_admindata(id=account.DeId,co_name="AccountId",value=None)
                return f"account with id {id} has been deleted",True
            else:
                logging.error(f"Error:occurred in delete_accountdata,account With This ID {id} Not Found")
                return f'Error: account With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_accountdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #outputing account data
    @classmethod
    def output_accountdata(cls,adminid):
        try:
            accounts=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for miki AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                accounts = Account.query.all()
            else:
                accounts = Account.query.filter_by(AdminId=adminid).all()
            accoutndata=[]
            for account in accounts:
                accoutndata.append({
                    'accountid': account.AccountId,
                    'dename': account.DeName,
                    'deid':account.DeId,
                    'employeeid': account.EmployeeId,
                    'createddate': account.CreatedDate,
                    'updateddate': account.UpdatedDate,
                    'passwordhash':account.PasswordHash,
                    'status':account.Status,
                    'phonenumber':account.PhoneNumber,
                    'role':account.Role
                })
            return accoutndata
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in output_accountdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #checking loging  info
    @classmethod
    def checker(cls, dename, deid, password):
        account = Account.query.filter_by(DeName=dename,DeId=deid).first()
        if not account:
            print(dename,deid)
            print("dename not found")
            return {'boll':False,
                "mss":"deid or password incorrect"}
    
        stored_password_hash = account.PasswordHash.encode('utf-8') if isinstance(account.PasswordHash, str) else account.PasswordHash
        if bcrypt.checkpw(password, stored_password_hash):
                return {'boll':True,
                    "mss":None}
        else:
            print("deid or password incorrect")
            return {'boll':False,
                    "mss":"deid or password incorrect"}
                    

class dbCost:
    def __init__(self,adminid,dename,deid,costtype,costprice,costproductname,amount,usenote):
        self.adminid = adminid
        self.dename=dename
        if dename == "branch":
            branch = Branch.query.filter_by(BranchId=deid).first()
            if branch:
                self.deid=deid
            else:
                logging.error(f"Error:Branch not found for from deid {deid}")
                raise ValueError(f"Error:Branch not found for from deid {deid}")
        elif dename == "delivery":
            delivery = Delivery.query.filter_by(DeliveryId=deid).first()
            if delivery:
                self.deid=deid
            else:
                logging.error(f"Error:delivery not found for from deid {deid}")
                raise ValueError(f"Error:delivery not found for from deid {deid}")
        elif dename == "bakery":
            bakery = Bakery.query.filter_by(BakeryId=deid).first()
            if bakery:
                self.deid=deid
            else:
                logging.error(f"Error:bakery not found for from deid {deid}")
                raise ValueError(f"Error:bakery not found for from deid {deid}")
        elif dename == "admin":
            admin = Admin.query.filter_by(AdminId=deid).first()
            if admin:
                self.deid=deid
            else:
                logging.error(f"Error:admin not found for from deid {deid}")
                raise ValueError(f"Error:admin not found for from deid {deid}")
        elif dename == "totaladmin":
            admin = Admin.query.filter_by(AdminId=deid).first()
            if admin:
                self.deid=deid
            else:
                logging.error(f"Error:admin not found for from deid {deid}")
                raise ValueError(f"Error:admin not found for from deid {deid}")
        self.costtype=costtype
        self.costprice=costprice
        self.costproductname=costproductname
        self.amount=amount
        self.usenote=usenote
    
    #inserting cost data
    def insert_costdata(self):
        try:
            costdata=Cost(AdminId=self.adminid,DeName=self.dename,DeId=self.deid,CostType=self.costtype,
                          CostPrice=self.costprice,CostProductName=self.costproductname,Amount=self.amount,UseNote=self.usenote)
            db.session.add(costdata)
            db.session.commit()
            return 'successful', True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_costdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #updateing cost data
    @classmethod
    def update_costdata(cls,id,co_name,value):
        try:
            cost=Cost.query.filter_by(CostId=id).first()
            if cost:
                if hasattr(cost,co_name):
                    setattr(cost,co_name,value)
                    return f"cost data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_costdata,cost Column {co_name} Not Found")
                    return f'Error: cost Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_costdata,cost With This ID {id} Not Found")
                return f'Error: cost With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_costdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deleting cost data
    @classmethod
    def delete_costdata(cls,id):
        try:
            cost = Cost.query.filter_by(CostId=id).first()
            if cost:
                db.session.delete(cost)
                db.session.commit()
                return f"cost with id {id} has been deleted",True
            else:
                logging.error(f"Error:occurred in delete_costdata,cost With This ID {id} Not Found")
                return f'Error: cost With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_costdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #outputing cost data
    @classmethod
    def output_costdata(cls,adminid):
        try:
            costs=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                costs = Cost.query.all()
            else:
                costs = Cost.query.filter_by(AdminId=adminid).all()
            costdata=[]
            for cost in costs:
                costdata.append({
                    'costid': cost.CostId,
                    'purchaseddate': cost.PurchasedDate,
                    'dename': cost.DeName,
                    'deid': cost.DeId,
                    'costtype': cost.CostType,
                    'costprice': cost.CostPrice,
                    'costproductname': cost. CostProductName,
                    'amount': cost.Amount,
                    'usenote ': cost.UseNote,
                })
            return costdata
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in output_costdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

class dbOrder:
    def __init__(self,adminid,ordereddename,ordereddeid,productname,orderedproductamount,productprice,
                 customerinfo,pickupdateandtime,paymentstatus,orderedproductdetails,
                 orderstatus,deliverydetails):
        self.adminid=adminid
        self.ordereddename=ordereddename
        if ordereddename == "branch":
            branch = Branch.query.filter_by(BranchId=ordereddeid).first()
            if branch:
                self.ordereddeid=ordereddeid
            else:
                logging.error(f"Error:Branch not found for from deid {ordereddeid}")
                raise ValueError(f"Error:Branch not found for from deid {ordereddeid}")
        elif ordereddename == "delivery":
            delivery = Delivery.query.filter_by(DeliveryId=ordereddeid).first()
            if delivery:
                self.ordereddeid=ordereddeid
            else:
                logging.error(f"Error:delivery not found for from deid {ordereddeid}")
                raise ValueError(f"Error:delivery not found for from deid {ordereddeid}")
        elif ordereddename == "bakery":
            bakery = Bakery.query.filter_by(BakeryId=ordereddeid).first()
            if bakery:
                self.ordereddeid=ordereddeid
            else:
                logging.error(f"Error:bakery not found for from deid {ordereddeid}")
                raise ValueError(f"Error:bakery not found for from deid {ordereddeid}")
        elif ordereddename == "admin":
            admin = Admin.query.filter_by(AdminId=ordereddeid).first()
            if admin:
                self.ordereddeid=ordereddeid
            else:
                logging.error(f"Error:admin not found for from deid {ordereddeid}")
                raise ValueError(f"Error:admin not found for from deid {ordereddeid}")
        elif ordereddename == "totaladmin":
            admin = Admin.query.filter_by(AdminId=ordereddeid).first()
            if admin:
                self.ordereddeid=ordereddeid
            else:
                logging.error(f"Error:admin not found for from deid {ordereddeid}")
                raise ValueError(f"Error:admin not found for from deid {ordereddeid}")
        self.productname=productname
        self.orderedproductamount=orderedproductamount
        self.productprice=productprice
        self.customerinfo=customerinfo
        self.pickupdateandtime=pickupdateandtime
        self.paymentstatus=paymentstatus
        self.orderedproductdetails=orderedproductdetails
        self.orderstatus=orderstatus
        self.deliverydetails=deliverydetails
    
    #inserting order data
    def insert_orderdata(self):
        try:
            orderdata=Order(AdminId=self.adminid,OrderedDeName=self.ordereddename,OrderedDeId=self.ordereddeid, PrductName=self.productname,
                            OrderedProductAmount=self.orderedproductamount,ProductPrice=self.productprice,CustomerInfo=self.customerinfo,
                            PickUpDateAndTime=self.pickupdateandtime,PaymentStatus=self.paymentstatus,OrderedProductDetails=self.orderedproductdetails,
                            OrderStatus=self.orderstatus,DeliveryDetails=self.deliverydetails)
            db.session.add(orderdata)
            db.session.commit()
            return "successful",True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_orderdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #updateing order data
    @classmethod
    def update_orderdata(cls,id,co_name,value):
        try:
            order=Order.query.filter_by(OrderId=id).first()
            if order:
                if hasattr(order,co_name):
                    setattr(order,co_name,value)
                    return f"order data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_orderdata,order Column {co_name} Not Found")
                    return f'Error: order Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_orderdata,order With This ID {id} Not Found")
                return f'Error: order With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_orderdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deleting order data
    @classmethod
    def delete_orderdata(cls,id):
        try:
            order = Order.query.filter_by(CostId=id).first()
            if order:
                db.session.delete(order)
                db.session.commit()
                return f"order with id {id} has been deleted",True
            else:
                logging.error(f"Error:occurred in delete_orderdata,order With This ID {id} Not Found")
                return f'Error: order With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_orderdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #outputing order data
    @classmethod
    def output_orderdata(cls,adminid):
        try:
            orders=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                orders = Order.query.all()
            else:
                orders = Order.query.filter_by(AdminId=adminid).all()
            orderdata=[]
            for order in orders:
                orderdata.append({
                    'orderid': order.OrderId,
                    'adminid':order.AdminId,
                    'orderdate': order.OrderDate,
                    'ordereddename': order.OrderedDeName,
                    'ordereddeid': order.OrderedDeId,
                    'prductname': order.PrductName,
                    'productprice': order.ProductPrice,
                    'customerinfo': order.CustomerInfo,
                    'pickupdateandtime': order.PickUpDateAndTime,
                    'paymentstatus ': order.PaymentStatus,
                    'orderedproductamount': order.OrderedProductAmount,
                    'orderedproductdetails ': order.OrderedProductDetails ,
                    'orderstatus': order.OrderStatus,
                    'deliverydetails': order.DeliveryDetails,
                })
            return orderdata
        except Exception as e:
            logging.error(f"Error:occurred in output_orderdata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False


class dbConnection:
    def __init__(self,adminid,startingtime,fromdename,fromdeid,conversation,
                 conversationtype,todename,todeid):
        self.adminid = adminid
        self.startingtime=startingtime
        self.fromdename=fromdename
        if fromdename == "branch":
            branch = Branch.query.filter_by(BranchId=fromdeid).first()
            if branch:
                self.fromdeid=fromdeid
            else:
                logging.error(f"Error:Branch not found for from deid {fromdeid}")
                raise ValueError(f"Error:Branch not found for from deid {fromdeid}")
        elif fromdename == "delivery":
            delivery = Delivery.query.filter_by(DeliveryId=fromdeid).first()
            if delivery:
                self.fromdeid=fromdeid
            else:
                logging.error(f"Error:delivery not found for from deid {fromdeid}")
                raise ValueError(f"Error:delivery not found for from deid {fromdeid}")
        elif fromdename == "bakery":
            bakery = Bakery.query.filter_by(BakeryId=fromdeid).first()
            if bakery:
                self.fromdeid=fromdeid
            else:
                logging.error(f"Error:bakery not found for from deid {fromdeid}")
                raise ValueError(f"Error:bakery not found for from deid {fromdeid}")
        elif fromdename == "admin":
            admin = Admin.query.filter_by(AdminId=fromdeid).first()
            if admin:
                self.fromdeid=fromdeid
            else:
                logging.error(f"Error:admin not found for from deid {fromdeid}")
                raise ValueError(f"Error:admin not found for from deid {fromdeid}")
        elif fromdename == "totaladmin":
            admin = Admin.query.filter_by(AdminId=fromdeid).first()
            if admin:
                self.fromdeid=fromdeid
            else:
                logging.error(f"Error:admin not found for from deid {fromdeid}")
                raise ValueError(f"Error:admin not found for from deid {fromdeid}")
        self.conversation=conversation
        self.conversationtype=conversationtype
        self.todename=todename
        if todename == "branch":
            branch = Branch.query.filter_by(BranchId=todeid).first()
            if branch:
                self.todeid=todeid
            else:
                logging.error(f"Branch not found for from todeid {todeid}")
                raise ValueError(f"Branch not found for from todeid {todeid}")
        elif todename == "delivery":
            delivery = Delivery.query.filter_by(DeliveryId=todeid).first()
            if delivery:
                self.todeid=todeid
            else:
                logging.error(f"delivery not found for from todeid {todeid}")
                raise ValueError(f"delivery not found for from todeid {todeid}")
        elif todename == "bakery":
            bakery = Bakery.query.filter_by(BakeryId=todeid).first()
            if bakery:
                self.todeid=todeid
            else:
                logging.error(f"bakery not found for from todeid {todeid}")
                raise ValueError(f"bakery not found for from todeid {todeid}")
        elif todename == "admin":
            admin = Admin.query.filter_by(AdminId=todeid).first()
            if admin:
                self.todeid=todeid
            else:
                logging.error(f"admin not found for from todeid {todeid}")
                raise ValueError(f"admin not found for from todeid {todeid}")
        elif todename == "totaladmin":
            admin = Admin.query.filter_by(AdminId=todeid).first()
            if admin:
                self.todeid=todeid
            else:
                logging.error(f"admin not found for from todeid {todeid}")
                raise ValueError(f"admin not found for from todeid {todeid}")

    #inserting connection data
    def insert_connectiondata(self):
        try:
            connectiondata=Connection(AdminId=self.adminid,StartingTime=self.startingtime,
                                      FromeDeName=self.fromdename,FromeDeId=self.fromdeid,Conversation=self.conversation,
                                      ConversationType=self.conversationtype,ToDeName=self.todename,ToDeId=self.todeid)
            db.session.add(connectiondata)
            db.session.commit()
            return 'successful', True
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_connectiondata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #updateing connection data
    @classmethod
    def update_connectiondata(cls,id,co_name,value):
        try:
            connection=Connection.query.filter_by(CoId=id).first()
            if connection:
                if hasattr(connection,co_name):
                    setattr(connection,co_name,value)
                    return f"connection data with id {id} has been updated",True
                else:
                    logging.error(f"Error:occurred in update_connectiondata,connection Column {co_name} Not Found")
                    return f'Error: connection Column "{co_name}" Not Found',False
            else:
                logging.error(f"Error:occurred in update_connectiondata,connection With This ID {id} Not Found")
                return f'Error: connection With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_connectiondata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #deleting connection data
    @classmethod
    def delete_connectiondata(cls,id):
        try:
            connection = Connection.query.filter_by(CoId=id).first()
            if connection:
                db.session.delete(connection)
                db.session.commit()
                return f"order with id {id} has been deleted",True
            else:
                logging.error(f"Error:occurred in delete_connectiondata,order With This ID {id} Not Found")
                return f'Error: connection With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_connectiondata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False

    #outputing connection data
    @classmethod
    def output_connectiondata(cls,adminid):
        try:
            connections=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for AdminId {adminid}") 
                return f"Admin not found for AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                connections = Connection.query.all()
            else:
                connections = Connection.query.filter_by(AdminId=adminid).all()
            connectiondata=[]
            for connection in connections:
                connectiondata.append({
                    'coid': connection .CoId,
                    'adminid':connection .AdminId,
                    'date': connection .Date,
                    'startingtime': connection .StartingTime,
                    'endingtime': connection .EndingTime,
                    'fromedename': connection .FromeDeName,
                    'fromedeid': connection .FromeDeId,
                    'conversation': connection .Conversation,
                    'conversationtype': connection .ConversationType,
                    'todename': connection .ToDeName,
                    'todeid': connection .ToDeId
                })
            return connectiondata
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in output_connectiondata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False 

class dbAdmin:
    def __init__(self,adminname,admintype,controlerid,createradminid):
        self.adminname=adminname
        self.admintype=admintype
        employee = Employee.query.filter_by(EmployeeId=controlerid).first()
        if employee:
            if employee.WorkingPositionName == None:
                self.controlerid=controlerid
            else:
                logging.error(f"Error:Employee occupied for controlers_id {controlerid}")
                raise ValueError(f"Error:Employee occupied for controlers_id {controlerid}")
        else:
            logging.error(f"Error:Employe not found for controler id {controlerid}")
            raise ValueError(f"Error:Employe not found for controler id {controlerid}")
        self.createradminid=createradminid
    
    #inserting admin data
    def insert_admindata(self,creatorid):
        try:
            admin = Admin.query.filter_by(AdminId=creatorid).first()
            if admin.AdminType == "totaladmin":
                admindata = Admin( CreateAdmin=self.createradminid,AdminType=self.admintype,
                                AdminName=self.adminname,ControlerId=self.controlerid)
                db.session.add(admindata)
                db.session.commit()
                if self.admintype == 'admin':
                    dbEmployee.update_employeedata(id=self.controlerid,co_name='WorkingPosition',value="admin")
                elif self.admintype == 'totaladmin':
                    dbEmployee.update_employeedata(id=self.controlerid,co_name='WorkingPosition',value="totaladmin")
                dbEmployee.update_employeedata(id=self.controlerid,co_name='WorkingPositionName',value=admindata.AdminName)
                dbEmployee.update_employeedata(id=self.controlerid,co_name='Role',value="controller")           
                return "successful",True
            else:
                return "only totaladmin can create admin",False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in insert_admindata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #updating admin data
    @classmethod
    def update_admindata(cls,id,co_name,value,creatorid):
        try:
            admin=Admin.query.filter_by(AdminId=id).first()
            if admin:
                creatoradmin = Admin.query.filter_by(AdminId=creatorid).first()
                if creatoradmin.AdminType == "totaladmin":
                    if hasattr(admin,co_name):
                        setattr(admin,co_name,value)
                        if co_name == "ControlerId":
                            employee2 = Employee.query.filter_by(EmployeeId=value).first()
                            if employee2.WorkingPositionName == None:
                                employee1 = Employee.query.filter_by(EmployeeId=admin.ControlerId).first()
                                dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='WorkingPositionName',value=None)
                                dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='WorkingPosition',value=None)
                                dbEmployee.update_employeedata(id=employee1.EmployeeId,co_name='Role',value=None)
                            
                                dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='WorkingPositionName',value=admin.AdminName)
                                dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='WorkingPosition',value="admin")
                                dbEmployee.update_employeedata(id=employee2.EmployeeId,co_name='Role',value="controller")
                                db.session.commit()
                                return f"Admin data with id {id} has been updated",True
                            else:
                                return f"Error:Employee occupied:Admin data with id {id} has not been updated",False
                        else:
                            db.session.commit()
                            return f"Admin data with id {id} has been updated",True
                    else:
                        logging.error(f"Error:occurred in update_admindata,admin Column {co_name} Not Found")
                        return f'Error: admin Column "{co_name}" Not Found',False
                else:
                    return "only totaladmin can update admin",False
            else:
                logging.error(f"Error:occurred in update_admindata,admin With This ID {id} Not Found")
                return f'Error: admin With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in update_admindata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #deleting admin data
    @classmethod
    def delete_admindata(cls,id,creatorid):
        try:
            admin = Admin.query.filter_by(AdminId=id).first()
            if admin:
                creatoradmin = Admin.query.filter_by(AdminId=creatorid).first()
                if creatoradmin.AdminType == "totaladmin":
                    db.session.delete(admin)
                    db.session.commit()
                    employee = Employee.query.filter_by(EmployeeId=admin.ControlerId).first()
                    account = Account.query.filter_by(DeId=admin.AdminId).first()
                    dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='WorkingPositionName',value=None)
                    dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='WorkingPosition',value=None)
                    dbEmployee.update_employeedata(id=employee.EmployeeId,co_name='Role',value=None)
                    if not account == None:
                        dbAccount.delete_accountdata(id=account.AccountId)
                    return f"admin with id {id} has been deleted",True
                else:
                   return "only totaladmin can delete admin",False 
            else:
                logging.error(f"Error:occurred in delete_admindata,admin With This ID {id} Not Found")
                return f'Error: admin With This ID {id} Not Found',False
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error:occurred in delete_admindata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False
    
    #outputing admin data
    @classmethod
    def output_admindata(cls,adminid):
        try:
            admins=None
            admin=Admin.query.filter_by(AdminId=adminid).first()
            if not admin: 
                logging.error(f"Admin not found for  AdminId {adminid}") 
                return f"Admin not found for  AdminId {adminid}", False
            if admin.AdminType == "totaladmin":
                admins = Admin.query.all()
            else:
                admins = Admin.query.filter_by(CreateAdmin=adminid).all()
            admindata=[]
            for admin in admins:
                admindata.append({
                    'admintype': admin.AdminType,
                    'createadminid':admin.CreateAdmin,
                    'adminid':admin.AdminId,
                    'adminname': admin.AdminName,
                    'createddate':admin.CretedDate,
                    'controlerid': admin.ControlerId,
                })
            return admindata
        except Exception as e:
            logging.error(f"Error:occurred in output_admindata,Error:{e} HAS BEEN FOUND")
            return f"Error:{e} HAS BEEN FOUND",False


#we will add all Product_BDB_Transaction_Sale from dbTransaction by useing   this columns in Transaction table  BakeryId = db.relationship('Bakery', secondary=Product_BDB_Transaction_Sale, backref='bakery')
#    DeliveryId = db.relationship('Delivery', secondary=Product_BDB_Transaction_Sale, backref='delivery')
 #   BranchId = db.relationship('Branch', secondary=Product_BDB_Transaction_Sale, backref='branch')
  #  ProductId = db.relationship('Products', secondary=Product_BDB_Transaction_Sale, backref='product')



#threading to products sale
#def run_scheduled_tasks():

 #   branch = dbBranch('BranchName', 'Location', 1, 10, 100000, 10000, 1000, 8)
  #  delivery = dbDelivery(0, 1, 1, 10, 100000, 10000, 1000, 8)
   # threading.Thread(target=branch.setproducts).start()
    #threading.Thread(target=branch.setsale).start()
    #threading.Thread(target=delivery.set_totalproducts).start()
#run_scheduled_tasks()
