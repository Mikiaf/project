from config import db
from sqlalchemy import text
from sqlalchemy.types import Enum
from datetime import datetime




# product BDB relationships m to m relationship
Product_BDB_Transaction_Sale = db.Table('product_bdb_transaction_sale',
        db.Column('Product_id', db.Integer, db.ForeignKey('products.ProductId')),
        db.Column('Bakery_id', db.Integer, db.ForeignKey('bakery.BakeryId')),
        db.Column('Delivery_id', db.Integer, db.ForeignKey('delivery.DeliveryId')),
        db.Column('Branch_id', db.Integer, db.ForeignKey('branch.BranchId')),
        db.Column('Transaction_id', db.Integer, db.ForeignKey('transaction.TransId')),
        #db.Column('BDTransaction_id', db.Integer, db.ForeignKey('transaction.TransId')),
        #db.Column('DBTransaction_id', db.Integer, db.ForeignKey('transaction.TransId')),
        #db.Column('Sale_id', db.Integer, db.ForeignKey('sale.SaleId')),
        db.Column('Time',db.Date, default=datetime.utcnow)
)

# branch db.table
class Branch(db.Model):
    BranchId = db.Column(db.Integer, primary_key = True)
    AdminId = db.Column(db.Integer,nullable=False)
    BrnachType = db.Column(db.String(50),nullable=False)#need to be created on the database
    BranchName = db.Column(db.String(100),unique=True,nullable=False)
    BranchImage = db.Column(db.String(255))
    Location = db.Column(db.String(200),nullable=False)
    ControllerId = db.Column(db.Integer,unique=True,nullable=False)
    AccountId = db.Column(db.Integer,unique=True,default=None)
    TotalWorkers = db.Column(db.Integer)
    BranchStartingDate = db.Column(db.Date, default=datetime.utcnow)
    TotalAcceptedProducts = db.Column(db.Integer)
    BranchTotalSaleInMoney = db.Column(db.Integer)
    BranchYearSaleGoalInMoney = db.Column(db.Integer)
    BranchMonthSaleGoalInMoney = db.Column(db.Integer)
    BranchDaySaleGoalInMoney = db.Column(db.Integer)
    BranchDayWorikingHoureGoal = db.Column(db.Integer)

    def to_json(self):
        return{
            'Branchid': self.BranchId,
            'AdminId':self.AdminId,
            'BranchName': self.BranchName,
            'Location':self.Location,
            'ControllerId':self.ControllerId,
            'TotalWorkers':self.TotalWorkers,
            'BranchStartingDate':self.BranchStartingDate,
            'TotalAcceptedProducts':self.TotalAcceptedProducts,
            'BranchTotalSaleInMoney':self.BranchTotalSaleInMoney,
            'BranchYearSaleGoalInMoney':self.BranchYearSaleGoalInMoney,
            'BranchMonthSaleGoalInMoney':self.BranchMonthSaleGoalInMoney,
            'BranchDaySaleGoalInMoney':self.BranchDaySaleGoalInMoney,
            'BranchDayWorikingHoureGoal':self.BranchDayWorikingHoureGoal
        }

# bakery db.tbale
class Bakery(db.Model):
    BakeryId = db.Column(db.Integer, primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    BakeryName = db.Column(db.String(100),unique=True,nullable=False)
    BakeryType = db.Column(db.String(50),nullable=False)
    BakeryImage = db.Column(db.String(255))
    ManagerID = db.Column(db.Integer,unique=True,nullable=False)
    BakeryStartedDate = db.Column(db.Date, default=datetime.utcnow)
    TotalWorkingHours = db.Column(db.Integer)
    Location = db.Column(db.String(200),nullable=False)
    AccountId = db.Column(db.Integer,unique=True,default=None)
    TotalWorkers = db.Column(db.Integer)
    TotalBakedProducts = db.Column(db.Integer)
    TotalSendOutProducts = db.Column(db.Integer)
    TotalDayToBakeProductsGoal = db.Column(db.Integer)
    TotalMonthToBakeProductsGoal = db.Column(db.Integer)
    TotalYearToBakeProductsGoal = db.Column(db.Integer)
    TotalDayToSendOutProductsGoal = db.Column(db.Integer)
    TotalMonthToSendOutProductsGoal = db.Column(db.Integer)
    TotalYearToSendOutProductsGoal = db.Column(db.Integer)
    deliveries = db.relationship('Delivery', primaryjoin="Bakery.BakeryId == Delivery.WorkingBakeryId",backref='bakery', lazy=True)

    def to_json(self):
        return {
            'BakeryId': self.BakeryId,
            ' AdminId':self. AdminId,
            'BakeryName': self.BakeryName,
            'ManagerID': self.ManagerID,
            'BakeryStartedDate': self.BakeryStartedDate,
            'TotalWorkingHours': self.TotalWorkingHours,
            'Location': self.Location,
            'TotalWorkers': self.TotalWorkers,
            'TotalBakedProducts': self.TotalBakedProducts,
            'TotalSendOutProducts': self.TotalSendOutProducts,
            'TotalDayToBakeProductsGoal': self.TotalDayToBakeProductsGoal,
            'TotalMonthToBakeProductsGoal': self.TotalMonthToBakeProductsGoal,
            'TotalYearToBakeProductsGoal': self.TotalYearToBakeProductsGoal,
            'TotalDayToSendOutProductsGoal': self.TotalDayToSendOutProductsGoal,
            'TotalMonthToSendOutProductsGoal': self.TotalMonthToSendOutProductsGoal,
            'TotalYearToSendOutProductsGoal': self.TotalYearToSendOutProductsGoal,
        }

# delivery db.tbale
class Delivery(db.Model):
    DeliveryId = db.Column(db.Integer, primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    DriverId = db.Column(db.Integer,unique=True,nullable=False)
    VicalPlateNo = db.Column(db.String(50),unique=True,nullable=False)
    VicalType = db.Column(db.String(100))
    VicalImage = db.Column(db.String(255))
    WorkingBakeryId = db.Column(db.Integer, db.ForeignKey('bakery.BakeryId'))
    AccountId = db.Column(db.Integer,unique=True,default=None)
    TotalWorkingHours = db.Column(db.Integer)
    TotalAcceptedProducts = db.Column(db.Integer)
    TotalDeliveredProducts = db.Column(db.Integer)
    TotalBranchesDelivered = db.Column(db.Integer)
    DeliveryStartingDate = db.Column(db.Date, default=datetime.utcnow)
    TotalWorkers = db.Column(db.Integer)
    TotalDayAcceptedProductsGoal = db.Column(db.Integer)
    TotalMonthAcceptedProductsGoal = db.Column(db.Integer)
    TotalYearAcceptedProductsGoal = db.Column(db.Integer)
    TotalDayDeliveredProductsGoal = db.Column(db.Integer)
    TotalMonthDeliveredProductsGoal = db.Column(db.Integer)
    TotalYearDeliveredProductsGoal = db.Column(db.Integer)

    def to_json(self):
        return {
           'DeliveryId': self.DeliveryId,
           'AdminId':self.AdminId,
           'DriverID': self.DriverId,
           'VicalPlateNo': self.VicalPlateNo,
           'VicalType': self.VicalType,
           'WorkingBakeryId': self.WorkingBakeryId,
           'TotalWorkingHours': self.TotalWorkingHours,
           'TotalAcceptedProducts': self.TotalAcceptedProducts,
           'TotalDeliveredProducts': self.TotalDeliveredProducts,
           'TotalBranchesDelivered': self.TotalBranchesDelivered,
           'DeliveryStartingDate': self.DeliveryStartingDate,
           'TotalWorkers': self.TotalWorkers,
           'TotalDayAcceptedProductsGoal': self.TotalDayAcceptedProductsGoal,
           'TotalMonthAcceptedProductsGoal': self.TotalMonthAcceptedProductsGoal,
           'TotalYearAcceptedProductsGoal': self.TotalYearAcceptedProductsGoal,
           'TotalDayDeliveredProductsGoal': self.TotalDayDeliveredProductsGoal,
           'TotalMonthDeliveredProductsGoal': self.TotalMonthDeliveredProductsGoal,
           'TotalYearDeliveredProductsGoal': self.TotalYearDeliveredProductsGoal,
        }

# employee db.table
class Employee(db.Model):
    #we need to update the input info in the frontend for ENUM column it need to be opition
    EmployeeId = db.Column(db.Integer, primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    EmployeeFname = db.Column(db.String(50),nullable=False)
    EmployeeMname = db.Column(db.String(50),nullable=False)
    EmployeeLname = db.Column(db.String(50),nullable=False)
    EmployeeImage = db.Column(db.String(255))
    StartingDate = db.Column(db.Date, default=datetime.utcnow)
    WorkingPosition = db.Column(Enum('branch', 'delivery', 'bakery','admin','totaladmin',name="dename"),default=None)
    WorkingPositionName = db.Column(db.String(200),unique=True,default=None)
    Accounts = db.relationship('Account', primaryjoin='Account.EmployeeId == Employee.EmployeeId',backref='employee')
    TotalWorkingHours = db.Column(db.Integer)
    Role = db.Column(Enum('controller', 'manager','driver','under', name='employee_roles'), default=None)
    UnderId = db.Column(db.Integer,default=None)
    Salary = db.Column(db.String(255))
    TotalPaidSalaryForEmployee = db.Column(db.Integer)
    DayWorkingHourGoal = db.Column(db.Integer)

    def to_json(self):
        return {
          'EmployeeId': self.EmployeeId,
          'AdminId':self.AdminId,
          'EmployeeFname': self.EmployeeFname,
          'EmployeeMname': self.EmployeeMname,
          'EmployeeLname': self.EmployeeLname,
          'StartingDate': self.StartingDate,
          'WorkingPosition': self.WorkingPosition,
          'WorkingPositionName': self.WorkingPositionName,
          'TotalWorkingHours': self.TotalWorkingHours,
          'Salary': self.Salary,
          'TotalPaidSalaryForEmployee': self.TotalPaidSalaryForEmployee,
          'DayWorkingHourGoal': self.DayWorkingHourGoal
        }

# products db.table
class Products(db.Model):
    ProductId = db.Column(db.Integer, primary_key=True)
    #we take adminid from the bakery.AdminId in the bakery table
    AdminId = db.Column(db.Integer,nullable=False)
    ProductName = db.Column(db.String(100),nullable=False)
    BakeryId = db.Column(db.Integer,nullable=False)
    TotalBakedProducts = db.Column(db.Integer,nullable=False)
    TotalBakedProductValue = db.Column(db.Integer,nullable=False)
    TimeOfBakery = db.Column(db.Date, default=datetime.utcnow)
    
    #calulated with in the product method
    TotalProductsSendOut = db.Column(db.Integer,nullable=False)
    TotalProductleft = db.Column(db.Integer)
    TotalProductsSendOutValue = db.Column(db.Integer,nullable=False)
    ProductsUsedForBakery = db.Column(db.String(2000))
    OneProductValue = db.Column(db.Integer,nullable=False)
    MoneyUsedToBakeTheProduct = db.Column(db.Integer,nullable=False)

    def to_json(self):
        return {
            'ProductId': self.ProductId,
            'AdminId':self.AdminId,
            'ProductName': self.ProductName,
            'TotalBakedProducts': self.TotalBakedProducts,
            'BakeryId': self.BakeryId,
            'TimeOfBakery': self.TimeOfBakery,
            'TotalProductsSendOut': self.TotalProductsSendOut,
            'TotalProductleft':self.TotalProductleft,
            'TotalProductsSendOutValue': self.TotalProductsSendOutValue,
            'ProductsUsedForBakery': self.ProductsUsedForBakery,
            'TotalBakedProductValueInMoney': self.TotalBakedProductValue,
            'OneProductValue ':self.OneProductValue,
            'MoneyUsedToBakeTheProduct': self.MoneyUsedToBakeTheProduct,
        }

#transaction db.table
class Transaction(db.Model):
    #this transaction table will filed with the tg.app of bakery delivery branch
    TransId = db.Column(db.Integer, primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)#this will be taken from bakery
    BakeryId = db.relationship('Bakery', secondary=Product_BDB_Transaction_Sale, backref='bakery')#the starter of the transaction included from the bakery
    DeliveryId = db.relationship('Delivery', secondary=Product_BDB_Transaction_Sale, backref='delivery')#this will be included when the delivery conform on tg.bot
    BranchId = db.relationship('Branch', secondary=Product_BDB_Transaction_Sale, backref='branch')#this will be included when the branch conform on tg.bot
    ProductId = db.relationship('Products', secondary=Product_BDB_Transaction_Sale, backref='product')#this will be included form the bakery
    TransStage = db.Column(db.String(100))
    TransStartingTime = db.Column(db.Date)
    TransEndingTime = db.Column(db.Date)
    AcceptedProductQuantity = db.Column(db.Integer,nullable=False)
    DeliveredProductQuantity = db.Column(db.Integer,nullable=False)
    TransGoal = db.Column(db.String(100))
    OneProductValue=db.Column(db.Integer,nullable=False)
    TotalAcceptedProductValueInMoney = db.Column(db.Integer)
    TotalDeliveredProductValueInMoney = db.Column(db.Integer)

    def to_json(self):
        return{
            'TransId':self.TransId,
            'AdminId':self.AdminId,
            'TransStage':self.TransStage,
            'TransStartingTime':self.TransStartingTime,
            'TransEndingTime':self.TransEndingTime,
            'AcceptedProductQuantity':self.AcceptedProductQuantity,
            'DeliveredProductQuantity':self.DeliveredProductQuantity,
            'OneProductValue':self.OneProductValue,
            'TotalAcceptedProductValueInMoney':self.TotalAcceptedProductValueInMoney,
            'TotalDeliveredProductValueInMoney':self.TotalDeliveredProductValueInMoney,
            'TransGoal':self.TransGoal,
        }


#sale db.table
class Sale(db.Model):
    #sale table will be filed with tg.app of branch
    SaleId = db.Column(db.Integer, primary_key=True)
    AdminId =  db.Column(db.Integer,nullable=False)
    SaleTime = db.Column(db.Date, default=datetime.utcnow)
    ProductId = db.Column(db.Integer,nullable=False)
    BakeryId = db.Column(db.Integer,nullable=False)
    #TotalBakedInMoney = db.Column(db.Integer)
    SaleBranchId = db.Column(db.Integer,nullable=False)
    TotalProductQuantitySold = db.Column(db.Integer,nullable=False)
    TotalSaledMoney = db.Column(db.Integer,nullable=False)
    OneProductValue = db.Column(db.Integer,nullable=False)
    #ti enter for transaction table
    TransactionId = db.Column(db.Integer,nullable=False)


    def to_json(self):
        return{
           'SaleId' :self.SaleId,
           'AdminId':self.AdminId,
           'SaleTime' :self.SaleTime,
           'ProductId' :self.ProductId,
           'SaleBranchId' :self.SaleBranchId,
           'BakeryId' :self.BakeryId,
           'TotalBakedInMoney' :self.TotalBakedInMoney,
           'TotalSaledMoney' :self.TotalSaledMoney,
           'ProductValue' :self.ProductValue,
           'TransactionId' :self.TransactionId,
        }


#salary db.table
class Salary(db.Model):
    #filed by admin and auto calculated
    SalaryId = db.Column(db.Integer, primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    PayDate = db.Column(db.Date,default=datetime.utcnow)
    EmployeeId = db.Column(db.Integer,nullable=False)
    PayedSalary = db.Column(db.Integer)
    MonthSalary = db.Column(db.Integer)
    TotalPaidSalaryForEmployee = db.Column(db.Integer)
    TotalPaidSalaryForAllEmployees = db.Column(db.Integer)

    def to_json(self):
        return {
            'SalaryId': self.SalaryId,
            'AdminId':self.AdminId,
            'EmployeeId': self.EmployeeId,
            'MonthSalary': self.MonthSalary,
            'TotalPaidSalaryForEmployee': self.TotalPaidSalaryForEmployee,
            'TotalPaidSalaryForAllEmployees': self.TotalPaidSalaryForAllEmployees
        }


#status db.table
class Status(db.Model):
    #auto calculated
    Date = db.Column(db.Date,default=datetime.utcnow)
    StatusId = db.Column(db.Integer, primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    DeName = db.Column(Enum('branch', 'delivery', 'bakery',name="dename"),nullable=False, default='bakery')
    DeId = db.Column(db.Integer,nullable=False)
    TotalYearSale = db.Column(db.Integer,default=0)
    TotalYearProfit = db.Column(db.Integer,default=0)
    TotalYearLoss = db.Column(db.Integer,default=0)
    TotalYearCost = db.Column(db.Integer,default=0)
    TotalYearBaked = db.Column(db.Integer,default=0)
    TotalYearAccepted = db.Column(db.Integer,default=0)
    TotalYearSendOut = db.Column(db.Integer,default=0)
    TotalYearDelivered = db.Column(db.Integer,default=0)

    def to_json(self):
        return {
            'Date':self.Date,
            'StatusId': self.StatusId,
            'AdminId':self. AdminId,
            'DeName': self.DeName,
            'DeId': self.DeId,
            'TotalYearSale': self.TotalYearSale,
            'TotalYearProfit': self.TotalYearProfit,
            'TotalYearLoss': self.TotalYearLoss,
            'TotalYearCost': self.TotalYearCost,
            'TotalYearAccepted': self.TotalYearAccepted,
            'TotalYearSendOut': self.TotalYearSendOut,
            'TotalYearDelivered': self.TotalYearDelivered,
        }

    
#asset db.table
class Asset(db.Model):
    #auto calculated
    #we need select in the react code for this column
    AssetId = db.Column(db.Integer, primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    OwnerDeName = db.Column(Enum('branch', 'delivery', 'bakery',name="dename"),nullable=False, default='bakery')
    OwnerId =db.Column(db.Integer,nullable=False)
    AssetName = db.Column(db.String(100),nullable=False)
    OwnedDate = db.Column(db.Date, default=datetime.utcnow)
    NumberOfAsset = db.Column(db.Integer)
    AssetType = db.Column(db.String(100))
    AssetValue = db.Column(db.Integer,nullable=False)
    TotalEnteredAssetValue = db.Column(db.Integer)
    Location = db.Column(db.String(100))
    AssetStatus = db.Column(db.String(100))
    TotalBakeryAssetValue = db.Column(db.Integer,default=0)
    TotalDeliveryAssetValue = db.Column(db.Integer,default=0)
    TotalBranchAssetValue = db.Column(db.Integer,default=0)
    TotalCompanyAssetValue = db.Column(db.Integer)

    def to_json(self):
        return{
            'AssetId':self.AssetId,
            'AdminId':self.AdminId,
            'AssetName':self.AssetName,
            'OwnedDate':self.OwnedDate,
            'AssetType':self.AssetType,
            'AssetValue':self.AssetValue,
            'Location':self.Location,
            'AssetStatus':self.AssetStatus,
            'NumberOfAsset':self.NumberOfAsset,
            'TotalBakeryAssetValue':self.TotalBakeryAssetValue,
            'TotalDeliveryAssetValue':self.TotalDeliveryAssetValue,
            'TotalBranchAssetValue':self.TotalBranchAssetValue,
            'TotalCompanyAssetValue':self.TotalCompanyAssetValue,
        }

#app db.table
class App(db.Model):
    AppId = db.Column(db.Integer, primary_key=True)
    UserDeName = db.Column(db.String(100))
    TotalNumberOfUsers = db.Column(db.Integer)
    TotalUsedTime = db.Column(db.Integer)
    TotalAppNumberOfUsers = db.Column(db.Integer)
    TotalAppUsedTime = db.Column(db.Integer)


    def to_json(self):
        return{
            'AppId':self.AppId,
            'UserDeName':self. UserDeName,
            'TotalNumberOfUsers':self.TotalNumberOfUsers,
            "TotalUsedTime":self.TotalUsedTime,
            "TotalAppNumberOfUsers ":self.TotalAppNumberOfUsers ,
            'TotalAppUsedTime':self.TotalAppUsedTime,
        }

#account db.table
class Account(db.Model):
    __tablename__ = 'account'
    AccountId = db.Column(db.Integer, primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    DeName = db.Column(Enum('branch', 'delivery', 'bakery','admin','totaladmin',name="dename"),nullable=False, default='admin')
    DeId= db.Column(db.Integer,nullable=False)
    EmployeeId = db.Column(db.Integer, db.ForeignKey('employee.EmployeeId'),nullable=False)
    CreatedDate = db.Column(db.Date, default=datetime.utcnow)
    UpdatedDate = db.Column(db.Date,default=None)
    PasswordHash = db.Column(db.String(255),nullable=False)
    Status=db.Column(Enum('active', 'inactive', 'suspended',name="account_status"),nullable=False, default='active')
    PhoneNumber = db.Column(db.String(50))

    #we will use this to access separate info form the database dename,admin,totaldamin
    Role = db.Column(Enum('user', 'admin','totaladmin', name='user_roles'), nullable=False, default='user')

    def to_json(self):
        return {
            'AccountId': self.AccountId,
            ' AdminId':self. AdminId,
            'DeName': self.DeName,
            'DeId':self.DeId,
            'EmployeeId': self.EmployeeId,
            'CreatedDate': self.CreatedDate,
            'UpdatedDate': self.UpdatedDate,
            'PasswordHash':self.PasswordHash,
            'Status':self.Status,
            'PhoneNumber':self.PhoneNumber,
            'Role':self.Role
        }

#cost db.table
class Cost(db.Model):
    CostId = db.Column(db.Integer,primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    PurchasedDate = db.Column(db.Date,default=datetime.utcnow)
    DeName = db.Column(Enum('branch', 'delivery', 'bakery','admin','totaladmin',name="dename"),nullable=False, default='branch')
    DeId = db.Column(db.Integer,nullable=False)
    CostType = db.Column(db.String(100))
    CostPrice = db.Column(db.Integer)
    CostProductName = db.Column(db.String(100))
    Amount = db.Column(db.Integer)
    UseNote = db.Column(db.String(1000))

    def to_json(self):
        return {
            'CostId': self.CostId,
            'AdminId':self.AdminId,
            'PurchasedDate': self.PurchasedDate,
            'DeName': self.DeName,
            'DeId': self.DeId,
            'CostType': self.CostType,
            'CostPrice': self.CostPrice,
            ' CostProductName': self. CostProductName,
            'Amount': self.Amount,
            'UseNote ': self.UseNote,
        }

#order db.table
class Order(db.Model):
    OrderId = db.Column(db.Integer,primary_key=True)
    AdminId = db.Column(db.Integer,nullable=False)
    OrderDate = db.Column(db.Date,default=datetime.utcnow)
    OrderedDeName = db.Column(Enum('branch', 'delivery', 'bakery','admin','totaladmin',name="dename"),nullable=False, default='branch')
    OrderedDeId = db.Column(db.Integer,nullable=False)
    PrductName = db.Column(db.Integer)
    OrderedProductAmount = db.Column(db.Integer)
    ProductPrice = db.Column(db.Integer)
    CustomerInfo = db.Column(db.String(700))
    PickUpDateAndTime = db.Column(db.Date,default=None)
    PaymentStatus = db.Column(Enum('paid', 'halfpaid', 'unpaid',name="paymentstatus"),nullable=False, default='unpaid')
    OrderedProductDetails = db.Column(db.String(1000))
    OrderStatus = db.Column(Enum('inprogress', 'finshed',name="orederstatus"),nullable=False, default='inprogress')
    DeliveryDetails = db.Column(Enum('pickup', 'deliver',name="deliverystatus"),nullable=False, default='pickup')

    def to_json(self):
        return {
            'OrderId': self.OrderId,
            'AdminId':self.AdminId,
            'OrderDate': self.OrderDate,
            'OrderedDeName': self.OrderedDeName,
            'OrderedDeId': self.OrderedDeId,
            'PrductName': self.PrductName,
            'ProductPrice': self.ProductPrice,
            'CustomerInfo': self.CustomerInfo,
            'PickUpDateAndTime': self.PickUpDateAndTime,
            'PaymentStatus ': self.PaymentStatus,
            'OrderedProductAmount': self.OrderedProductAmount,
            'OrderedProductDetails ': self.OrderedProductDetails ,
            'OrderStatus': self.OrderStatus,
            'DeliveryDetails': self.DeliveryDetails,
        }


#connection db.table
class Connection(db.Model):
    CoId=db.Column(db.Integer,primary_key=True)
    AdminId=db.Column(db.Integer,nullable=False)
    Date=db.Column(db.Date,default=datetime.utcnow)
    StartingTime=db.Column(db.Date,default=None)
    EndingTime=db.Column(db.Date,default=None)
    FromeDeName=db.Column(Enum('branch', 'delivery', 'bakery','admin','totaladmin',name="fromdename"),nullable=False, default='branch')
    FromeDeId=db.Column(db.Integer,nullable=False)
    Conversation=db.Column(db.String(1000))
    ConversationType=db.Column(Enum('delivery', 'fixreport',name="conversationtype"),nullable=False, default='delivery')
    ToDeName=db.Column(Enum('branch', 'delivery', 'bakery','admin','totaladmin',name="todename"),nullable=False, default='branch')
    ToDeId=db.Column(db.Integer,nullable=False)

    def to_json(self):
        return {
            'CoId': self.CoId,
            'AdminId':self.AdminId,
            'Date': self.Date,
            'StartingTime': self.StartingTime,
            'EndingTime': self.EndingTime,
            'FromeDeName': self.FromeDeName,
            'FromeDeId': self.FromeDeId,
            'Conversation': self.Conversation,
            'ConversationType': self.ConversationType,
            'ToDeName': self.ToDeName,
            'ToDeId': self.ToDeId
        }



class Admin(db.Model):
    AdminId = db.Column(db.Integer,primary_key=True)
    CreateAdmin =db.Column(db.Integer,nullable=False)
    AdminType = db.Column(Enum('admin','totaladmin',name="type"),nullable=False, default='admin')
    AdminName = db.Column(db.String(50),unique=True)
    ControlerId = db.Column(db.Integer,unique=True,nullable=False)
    AccountId = db.Column(db.Integer,unique=True,default=None)
    CretedDate = db.Column(db.Date,default=datetime.utcnow)

    def to_json(self):
            return {
                'AdminType':self.AdminType,
                'AdminId':self.AdminId,
                'AdminName': self.AdminName,
                'ControlerId': self. ControlerId,
                'CretedDate': self.CretedDate,
            }

db.create_all()