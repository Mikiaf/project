from config import db
from datetime import datetime



# product BDB relationships m to m relationship
Product_BDB_Transaction_Sale = db.Table('product_bdb_transaction_sale',
        db.Column('Product_id', db.Integer, db.ForeignKey('products.ProductId')),
        db.Column('Bakery_id', db.Integer, db.ForeignKey('bakery.BakeryId')),
        db.Column('Delivery_id', db.Integer, db.ForeignKey('delivery.DeliveryId')),
        db.Column('Branch_id', db.Integer, db.ForeignKey('branch.BranchId')),
        db.Column('Transaction_id', db.Integer, db.ForeignKey('transaction.TransId')),
        db.Column('Sale_id', db.Integer, db.ForeignKey('sale.SaleId')),
        db.Column('Time',db.Date, default=datetime.utcnow)
)

# branch db.table
class Branch(db.Model):
    BranchId = db.Column(db.Integer, primary_key = True)
    BranchName = db.Column(db.String(100))
    BranchImage = db.Column(db.LargeBinary)
    Location = db.Column(db.String(200))
    ControllerId = db.Column(db.Integer)
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
    BakeryName = db.Column(db.String(100))
    ManagerID = db.Column(db.Integer)
    BakeryStartedDate = db.Column(db.Date, default=datetime.utcnow)
    TotalWorkingHours = db.Column(db.Integer)
    Location = db.Column(db.String(200))
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
    DriverID = db.Column(db.Integer)
    VehiclePlateNo = db.Column(db.String(50))
    VehicleType = db.Column(db.String(100))
    WorkingBakeryId = db.Column(db.Integer, db.ForeignKey('bakery.BakeryId'))
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
           'DriverID': self.DriverID,
           'VehiclePlateNo': self.VehiclePlateNo,
           'VehicleType': self.VehicleType,
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
    EmployeeId = db.Column(db.Integer, primary_key=True)
    EmployeeFname = db.Column(db.String(50))
    EmployeeLname = db.Column(db.String(50))
    StartingDate = db.Column(db.Date, default=datetime.utcnow)
    WorkingPosition = db.Column(db.String(100))
    WorkingPositionId = db.Column(db.Integer)
    Accounts = db.relationship('Account', primaryjoin='Account.EmployeeId == Employee.EmployeeId',backref='employee')
    TotalWorkingHours = db.Column(db.Integer)
    Salary = db.Column(db.Integer, db.ForeignKey('salary.SalaryId'))
    TotalPaidSalary = db.Column(db.Integer)
    DayWorkingHours = db.Column(db.Integer)
    DayWorkingHourGoal = db.Column(db.Integer)

    def to_json(self):
        return {
          'EmployeeId': self.EmployeeId,
          'EmployeeFname': self.EmployeeFname,
          'EmployeeLname': self.EmployeeLname,
          'StartingDate': self.StartingDate,
          'WorkingPosition': self.WorkingPosition,
          'WorkingPositionId': self.WorkingPositionId,
          'TotalWorkingHours': self.TotalWorkingHours,
          'Salary': self.Salary,
          'TotalPaidSalary': self.TotalPaidSalary,
          'DayWorkingHours': self.DayWorkingHours,
          'DayWorkingHourGoal': self.DayWorkingHourGoal
        }

# products db.table
class Products(db.Model):
    ProductId = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(100))
    BakeryId = db.relationship('Bakery', secondary=Product_BDB_Transaction_Sale, backref='bakedproducts')
    DeliveryId = db.relationship('Delivery', secondary=Product_BDB_Transaction_Sale, backref='deliveredproducts')
    BranchId = db.relationship('Branch', secondary=Product_BDB_Transaction_Sale, backref='saledproducts')
    TransId = db.relationship('Transaction', secondary=Product_BDB_Transaction_Sale, backref='transproducts')
    SaleId = db.relationship('Sale', secondary=Product_BDB_Transaction_Sale, backref='saledproducts')
    TotalBakedProducts = db.Column(db.Integer)
    TotalDeliveredProducts = db.Column(db.Integer)
    TimeOfBakery = db.Column(db.Date, default=datetime.utcnow)
    TotalProductsSendOut = db.Column(db.Integer)
    ProductsUsedForBakery = db.Column(db.String(2000))
    ProductValueInMoney = db.Column(db.Integer)
    MoneyUsedToBakeTheProduct = db.Column(db.Integer)

    def to_json(self):
        return {
            'ProductId': self.ProductId,
            'ProductName': self.ProductName,
            'BakeryId': self.BakeryId,
            'DeliveryId': self.DeliveryId,
            'BranchId': self.BranchId,
            'TotalBakedProducts': self.TotalBakedProducts,
            'TotalDeliveredProducts': self.TotalDeliveredProducts,
            'TimeOfBakery': self.TimeOfBakery,
            'TotalProductsSendOut': self.TotalProductsSendOut,
            'ProductsUsedForBakery': self.ProductsUsedForBakery,
            'ProductValueInMoney': self.ProductValueInMoney,
            'MoneyUsedToBakeTheProduct': self.MoneyUsedToBakeTheProduct,
        }

#transaction db.table
class Transaction(db.Model):
    TransId = db.Column(db.Integer, primary_key=True)
    TransTime = db.Column(db.Date, default=datetime.utcnow)
    TransType = db.Column(db.String(100))
    TransProductId = db.Column(db.Integer)
    BakeryId= db.Column(db.Integer)
    DeliveryId= db.Column(db.Integer)
    BranchId = db.Column(db.Integer)
    ProductQuantity = db.Column(db.Integer)
    TransGoal = db.Column(db.String(100))
    TransValueInMoney = db.Column(db.Integer)

    def to_json(self):
        return{
            'TransId':self.TransId,
            'TransTime':self.TransTime,
            'TransType':self.TransType,
            'TransProductId':self.TransProductId,
            'BakeryId':self.BakeryId,
            'DeliveryId':self.DeliveryId,
            'BranchId':self.BranchId,
            'ProductQuantity':self.ProductQuantity,
            'TransGoal':self.TransGoal,
            'TransValueInMoney':self. TransValueInMoney,
        }


#sale db.table
class Sale(db.Model):
    SaleId = db.Column(db.Integer, primary_key=True)
    SaleTime = db.Column(db.Date, default=datetime.utcnow)
    ProductId = db.Column(db.Integer)
    BakeryId = db.Column(db.Integer)
    TotalBakedInMoney = db.Column(db.Integer)
    SaleBranchId = db.Column(db.Integer)
    TotalSaledMoney = db.Column(db.Integer)
    ProductValue = db.Column(db.Integer)
    TransactionId = db.Column(db.Integer)


    def to_json(self):
        return{
           'SaleId' :self.SaleId,
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
    SalaryId = db.Column(db.Integer, primary_key=True)
    EmployeeId = db.relationship('Employee', backref='salary')
    WorkingPosition = db.Column(db.String(100))
    MonthSalary = db.Column(db.Integer)
    TotalPaidSalaryForEmployee = db.Column(db.Integer)
    TotalPaidSalaryForAllEmployees = db.Column(db.Integer)

    def to_json(self):
        return {
            'SalaryId': self.SalaryId,
            'EmployeeId': self.EmployeeId,
            'WorkingPosition': self.WorkingPosition,
            'MonthSalary': self.MonthSalary,
            'TotalPaidSalaryForEmployee': self.TotalPaidSalaryForEmployee,
            'TotalPaidSalaryForAllEmployees': self.TotalPaidSalaryForAllEmployees
        }


#status db.table
class Status(db.Model):
    StatusId = db.Column(db.Integer, primary_key=True)
    DeName = db.Column(db.String(50))
    DeId = db.Column(db.Integer)
    TotalYearSale = db.Column(db.Integer)
    TotalYearProfit = db.Column(db.Integer)
    TotalYearLose = db.Column(db.Integer)
    TotalYearCost = db.Column(db.Integer)
    TotalYearAccepted = db.Column(db.Integer)
    TotalYearSendOut = db.Column(db.Integer)
    TotalYearDelivered = db.Column(db.Integer)

    def to_json(self):
        return {
            'StatusId': self.StatusId,
            'DeName': self.DeName,
            'DeId': self.DeId,
            'TotalYearSale': self.TotalYearSale,
            'TotalYearProfit': self.TotalYearProfit,
            'TotalYearLose': self.TotalYearLose,
            'TotalYearCost': self.TotalYearCost,
            'TotalYearAccepted': self.TotalYearAccepted,
            'TotalYearSendOut': self.TotalYearSendOut,
            'TotalYearDelivered': self.TotalYearDelivered,
        }

    
#asset db.table
class Asset(db.Model):
    AssetId = db.Column(db.Integer, primary_key=True)
    AssetName = db.Column(db.String(100))
    OwnedDate = db.Column(db.Date, default=datetime.utcnow)
    AssetType = db.Column(db.String(100))
    AssetValue = db.Column(db.Integer)
    Location = db.Column(db.String(100))
    AssetStatus = db.Column(db.String(100))
    NumberOfAsset = db.Column(db.Integer)
    TotalBakeryAssetValue = db.Column(db.Integer)
    TotalDeliveryAssetValue = db.Column(db.Integer)
    TotalBranchssetValue = db.Column(db.Integer)
    TotalCompanyAssetValue = db.Column(db.Integer)

    def to_json(self):
        return{
            'AssetId':self.AssetId,
            'AssetName':self.AssetName,
            'OwnedDate':self.OwnedDate,
            'AssetType':self.AssetType,
            'AssetValue':self.AssetValue,
            'Location':self.Location,
            'AssetStatus':self.AssetStatus,
            'NumberOfAsset':self.NumberOfAsset,
            'TotalBakeryAssetValue':self.TotalBakeryAssetValue,
            'TotalDeliveryAssetValue':self.TotalDeliveryAssetValue,
            'TotalBranchssetValue':self.TotalBranchssetValue,
            'TotalCompanyAssetValue':self.TotalCompanyAssetValue,
        }

#app db.table
class App(db.Model):
    AppId = db.Column(db.Integer, primary_key=True)
    AppType = db.Column(db.String(100))
    TotalNumberOfUsers = db.Column(db.Integer)
    TotalAppUsedTime = db.Column(db.Integer)


    def to_json(self):
        return{
            'AppId':self.AppId,
            'AppType':self.AppType,
            'TotalNumberOfUsers':self.TotalNumberOfUsers,
            'TotalAppUsedTime':self.TotalAppUsedTime,
        }

#account db.table
class Account(db.Model):
    __tablename__ = 'account'
    AccountId = db.Column(db.Integer, primary_key=True)
    AppId = db.Column(db.Integer)
    EmployeeId = db.Column(db.Integer, db.ForeignKey('employee.EmployeeId'))
    CreatedDate = db.Column(db.Date, default=datetime.utcnow)
    LoggedTime = db.Column(db.Date, default=datetime.utcnow)
    UsedTime = db.Column(db.Integer)

    def to_json(self):
        return {
            'AccountId': self.AccountId,
            'AppId': self.AppId,
            'EmployeeId': self.EmployeeId,
            'CreatedDate': self.CreatedDate,
            'LoggedTime': self.LoggedTime,
            'UsedTime': self.UsedTime,
        }


db.create_all()