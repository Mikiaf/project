from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity,verify_jwt_in_request,get_jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import jwt
import json
from datetime import timedelta, datetime
from flask import Flask, jsonify, request, session,send_from_directory
from config import db
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/cobakery'


# Secret key for JWT encoding and decoding
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
jwt = JWTManager(app)
# Initialize the database
db.init_app(app)


def make_session_permanent():
    session.permanent = True  # Make the session permanent
    session.modified = True 


@app.route('/static/image/employees/<filename>')
def get_image(filename):
    # Ensure the path is correctly formatted
    directory_path = r'C:\Users\outis\Desktop\Oneproject\static\image\employees'
    
    return send_from_directory(directory_path, filename)




@app.route('/')
def home():
    from dbmethods import dbBranch, dbAccount, dbAdmin, dbEmployee
    account = dbAccount(adminid=1, dename="admin", deid=1, password='123', phonenumber='0967838509')
    #employee=dbEmployee(adminid=1,employeefname='mi',employeemname='af',employeelname='mm',workingposition=None,workingpositionname=None,dayworkinghourgoal=12,employeeimage=None,role=None,underid=None)
    #admin = dbAdmin(adminname="aaadmin",admintype='totaladmin',controlerid=1,createradminid=1)
    #employee.insert_employeedata()
    return jsonify(account.insert_accountdata())

@app.route('/api/login', methods=['POST'])
def login():
    try:
        from dbmethods import dbAccount
        data = request.get_json()
        dename = data['dename']
        deid = data['adminid']
        password = data['password'].encode('utf-8')

        if not (dename == 'admin' or dename == "totaladmin"):
            return jsonify({"message": "dename must be 'admin' or 'totaladmin'"}), 400

        is_valid = dbAccount.checker(dename=dename, deid=deid, password=password)
        print(is_valid)
        if is_valid['boll']:
            try:
                #token = jwt.encode({
                 #   'id': deid,
                #    'name':dename,
                 #   'exp': datetime.utcnow() + timedelta(minutes=30)
                #}, app.secret_key, algorithm="HS256")
                additional_claims = {"username": dename, "user_id": deid}
                access_token = create_access_token(identity=deid, additional_claims=additional_claims)
                response = jsonify({'login': True, 'token': access_token})
                response.set_cookie('access_token', access_token, httponly=True)
                print("Generated Token:", access_token)  # Print the token for debugging
                return response,200
            except Exception as e:
                print(e)
        else:
            return jsonify({"message": "Login unsuccessful:Check dename or deid or password"}), 400

    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), 500

@app.route('/api/insertdata', methods=['POST'])
def insertdata():
    from dbmethods import (dbBranch, dbBakery, 
    dbDelivery, dbProducts, dbEmployee, dbSalary, dbTransaction, dbAccount, 
    dbAsset, dbConnection, dbCost, dbOrder, dbSale, dbStatus, dbApp, dbAdmin,save_image)
    #data = request.get_json()
    db=request.form.get('type')
    password = request.form.get('password')
    toinsertdata = request.form.get('data')




    try:
        toinsertdata = json.loads(toinsertdata)  # Parse the JSON string into a dictionary
    except json.JSONDecodeError as e:
        return jsonify({"message": f"Error parsing JSON data: {str(e)}"}), 



    image_file = request.files.get('image')

    print(db)
    verify_jwt_in_request()
    current_user = get_jwt()
    username = current_user.get('username')
    user_id = current_user.get('user_id')

    is_valid = dbAccount.checker(dename=username, deid=user_id, password=password.encode('utf-8'))
    print(toinsertdata)
    if is_valid['boll']:
        print(is_valid['boll'])
        if db == "branch":
            image_path = save_image(image_file=image_file,filename=f"branch{toinsertdata['branchname']}.png")
            branch = dbBranch(
                adminid=user_id,branchtype=toinsertdata['branchtype'],
                branchname=toinsertdata['branchname'],location=toinsertdata['location'],
                controlers_id=toinsertdata['controlers_id'],totalworkers=toinsertdata['totalworkers'],
                branchyearsalegoal=toinsertdata['branchyearsalegoal'],branchmonthsalegoal=toinsertdata['branchmonthsalegoal'],
                branchdaysalegoal=toinsertdata['branchdaysalegoal'],branchdayworikinghouregoal=toinsertdata['branchdayworkinghourgoal'],
                branchimage=image_path
                )
            mss,valid = branch.insert_branchdata()
            if valid:
                return jsonify({"message": f"Data inserted: {mss}"}), 200
            else:
                return jsonify({"message": f"Data not inserted: {mss}"}),400
        if db == "bakery":
            image_path = save_image(image_file=image_file,filename=f"bakery{toinsertdata['bakeryname']}.png")
            bakery = dbBakery(
                adminid=user_id,bakeryname=toinsertdata['bakeryname'],
                bakerytype=toinsertdata['bakerytype'],managerid=toinsertdata['manager_id'],
                loacation=toinsertdata['location'],totalworkers=toinsertdata['totalworker'],
                totaldaytobakeproductsgoal=toinsertdata['totaldaytobakeproductsgoal'],
                totalmonthtobakeproductsgoal=toinsertdata['totalmonthtobakeproductsgoal'],
                totalyeartobakeproductsgoal=toinsertdata['totalyeartobakeproductsgoal'],
                totaldaytosendoutproductsgoal=toinsertdata['totaldaytosendoutproductsgoal'],
                totalmonthtosendoutproductsgoal=toinsertdata['totalmonthtosendoutproductsgoal'],
                totalyeartosendoutproductsgoal=toinsertdata['totalyeartosendoutproductsgoal'],
                bakeryimage=image_path
            )
            mss,valid=bakery.insert_bakerydata()
            print(mss)
            if valid:
                return jsonify({"message": f"Data inserted: {mss}"}), 200
            else:
                return jsonify({"message": f"Data not inserted: {mss}"}),400
        if db == 'delivery':
            image_path = save_image(image_file=image_file,filename=f"delivery{toinsertdata['vehicleplateno']}.png")
            delivery = dbDelivery(
                adminid=user_id,DriverId=toinsertdata['driver_id'],vicalplateNo=toinsertdata['vehicleplateno'],
                vicaltype=toinsertdata['vehicletype'],workingbakeryid=toinsertdata['workingbakery_id'],
                totalworkers=toinsertdata['totalworkers'],totaldayacceptedproductsgoal=toinsertdata['totaldayacceptedproductsgoal'],
                totalmonthacceptedproductsgoal=toinsertdata['totalmonthacceptedproductsgoal'],
                totalyearacceptedproductsgoal=toinsertdata['totalyearacceptedproductsgoal'],
                totaldaydeliverdproductsgoal=toinsertdata['totaldaydeliverdproductsgoal'],
                totalmonthdeliverdproductsgoal=toinsertdata['totalmonthdeliverdproductsgoal'],
                totalyeardeliverdproductsgoal=toinsertdata['totalyeardeliverdproductsgoal'],
                vicaimage=image_path
            )
            mss,valid=delivery.insert_deliverydata()
            print(mss)
            if valid:
                return jsonify({"message": f"Data inserted: {mss}"}), 200
            else:
                return jsonify({"message": f"Data not inserted: {mss}"}),400
        if db == "employee":
            image_path = save_image(image_file=image_file,filename=f"employee{toinsertdata['employeefname']}{toinsertdata['employeemname']}{toinsertdata['employeelname']}.png")
            employee = dbEmployee(
                adminid=user_id,employeefname=toinsertdata['employeefname'],employeelname=toinsertdata['employeelname'],
                employeemname=toinsertdata['employeemname'],workingposition=toinsertdata['workingposition'],
                workingpositionname=toinsertdata['workingpositionname'],dayworkinghourgoal=toinsertdata['dayworkinghourgoal'],
                underid=toinsertdata['underid'],role=toinsertdata['role'],
                employeeimage=image_path
            )
            print(image_path)
            mss,valid=employee.insert_employeedata()
            if valid:
                print(mss)
                return jsonify({"message": f"Data inserted: {mss}"}), 200
            else:
                print(mss)
                return jsonify({"message": f"Data not inserted: {mss}"}),400
        if db == "admin":
            admindata = dbAdmin(createradminid=user_id,adminname=toinsertdata['adminname'],
                            admintype=toinsertdata['admintype'],controlerid=toinsertdata['controlers_id'])
            mss,valid=admindata.insert_admindata(user_id)
            if valid:
                return jsonify({"message": f"Data inserted: {mss}"}), 200
            else:
                return jsonify({"message": f"Data not inserted: {mss}"}),400
        if db == "account":
            account = dbAccount(adminid=user_id,dename=toinsertdata['dename'],
                                deid=toinsertdata['de_id'],password=toinsertdata['password'],
                                phonenumber=toinsertdata['phonenumber'])
            mss,valid=account.insert_accountdata()
            if valid:
                return jsonify({"message": f"Data inserted: {mss}"}), 200
            else:
                return jsonify({"message": f"Data not inserted: {mss}"}),400
    else:
        return jsonify({"message": "Data not inserted,password wrong"}), 400






@app.route('/api/updatedata', methods=['POST'])
def updatedata():
    try:
        from dbmethods import (dbBranch, dbBakery, dbDelivery, dbProducts, dbEmployee, dbSalary, 
                                dbTransaction, dbAccount, dbAsset, dbConnection, dbCost, dbOrder, 
                                dbSale, dbStatus, dbApp, dbAdmin,save_image)
        db=request.form.get('type')
        password = request.form.get('password')
        id = request.form.get('id')
        selectedcolumn = request.form.get('selectedcolumn')
        toupdatedata = request.form.get('data')

        image_columns = {"EmployeeImage", "BranchImage", "BakeryImage", "VicalImage"}
        


        if selectedcolumn not in image_columns:
            try:
                toupdatedata = json.loads(toupdatedata)  # Parse the JSON string into a dictionary
            except json.JSONDecodeError as e:
                return jsonify({"message": f"Error parsing JSON data: {str(e)}"}), 400  # Return a 400 Bad Request status
        else:
            toupdatedata = request.files['image']
        #image_file = 
        verify_jwt_in_request()
        current_user = get_jwt()
        username = current_user.get('username')
        user_id = current_user.get('user_id')

        is_valid = dbAccount.checker(dename=username, deid=user_id, password=password.encode('utf-8'))
        if is_valid['boll']:
            if db == "employee":
                if selectedcolumn == "EmployeeImage":
                    employeedata = dbEmployee.single_outputemployeedata(id=id)
                    image_file = save_image(image_file=toupdatedata, filename=f"employee{employeedata['employeefname']}{employeedata['employeemname']}{employeedata['employeelname']}.png")
                    print(image_file)
                    mss,valid= dbEmployee.update_employeedata(id=id,co_name=selectedcolumn,value=image_file)
                mss,valid= dbEmployee.update_employeedata(id=id,co_name=selectedcolumn,value=toupdatedata)
                if valid:
                    return jsonify({"message": f"Data updated: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not updated: {mss}"}),400
            if db == "branch":
                if selectedcolumn == "BranchImage":
                    branchdata = dbBranch.single_outputbranchdata(id=id)
                    image_file = save_image(image_file=toupdatedata,filename=f"branch{branchdata['branchname']}.png")
                    mss,valid = dbBranch.update_branchdata(id=id,co_name=selectedcolumn,value=image_file)
                mss,valid = dbBranch.update_branchdata(id=id,co_name=selectedcolumn,value=toupdatedata)
                if valid:
                    return jsonify({"message": f"Data updated: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not updated: {mss}"}),400
            if db == "bakery":
                if selectedcolumn == "BakeryImage":
                    bakerydata = dbBakery.single_outputbakerydata(id=id)
                    image_file = save_image(image_file=toupdatedata,filename=f"bakery{bakerydata['bakeryname']}.png")
                    mss,valid = dbBakery.update_bakerydata(id=id,co_name=selectedcolumn,value=image_file)
                mss,valid = dbBakery.update_bakerydata(id=id,co_name=selectedcolumn,value=toupdatedata)
                if valid:
                    return jsonify({"message": f"Data updated: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not updated: {mss}"}),400
            if db == "delivery":
                if selectedcolumn == "DeliveryImage":
                    deliverydata = dbDelivery.single_outputdeliverydata(id=id)
                    image_file = save_image(image_file=toupdatedata,filename=f"delivery{deliverydata['vicalplateno']}.png")
                    mss,valid = dbDelivery.update_deliverydata(id=id,co_name=selectedcolumn,value=image_file)
                mss,valid = dbDelivery.update_deliverydata(id=id,co_name=selectedcolumn,value=toupdatedata)
                if valid:
                    return jsonify({"message": f"Data updated: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not updated: {mss}"}),400
            if db == "account":
                mss,valid = dbAccount.update_accountdata(id=id,co_name=selectedcolumn,value=toupdatedata)
                if valid:
                    return jsonify({"message": f"Data updated: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not updated: {mss}"}),400
            if db == "admin":
                mss,valid = dbAdmin.update_admindata(id=id,co_name=selectedcolumn,value=toupdatedata,creatorid=user_id)
                if valid:
                    return jsonify({"message": f"Data updated: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not updated: {mss}"}),400
        else:
            return jsonify({"message": "Data not inserted,password wrong"}), 400
    except Exception as e:
        return jsonify({'message': f'An unexpected error occurred {e}'}), 500







@app.route('/api/deletedata', methods=['POST'])
def deletedata():
    try:
        from dbmethods import (dbBranch, dbBakery, dbDelivery, dbProducts, dbEmployee, dbSalary, 
                                dbTransaction, dbAccount, dbAsset, dbConnection, dbCost, dbOrder, 
                                dbSale, dbStatus, dbApp, dbAdmin)
        
        data = request.get_json()
        db = data['db']
        password = data['password'].encode('utf-8')
        id = data['id']

        verify_jwt_in_request()
        current_user = get_jwt()
        username = current_user.get('username')
        user_id = current_user.get('user_id')

        is_valid = dbAccount.checker(dename=username, deid=user_id, password=password)
        print(id)
        if is_valid['boll']:
            if db == "employee":
                mss,valid = dbEmployee.delete_employeedata(id=id)
                if valid:
                    return jsonify({"message": f"Data deleted: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not deleted: {mss}"}),400
            if db== "branch":
                mss,valid=dbBranch.delete_branchdata(id=id)
                if valid:
                    return jsonify({"message": f"Data deleted: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not deleted: {mss}"}),400
            if db=="delivery":
                mss,valid=dbDelivery.delete_deliverdata(id=id)
                if valid:
                    return jsonify({"message": f"Data deleted: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not deleted: {mss}"}),400
            if db=="bakery":
                mss,valid=dbBakery.delete_bakerydata(id=id)
                if valid:
                    return jsonify({"message": f"Data deleted: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not deleted: {mss}"}),400
            if db=="account":
                mss,valid=dbAccount.delete_accountdata(id=id)
                if valid:
                    return jsonify({"message": f"Data deleted: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not deleted: {mss}"}),400
            if db=="admin":
                mss,valid=dbAdmin.delete_admindata(id=id,creatorid=user_id)
                if valid:
                    return jsonify({"message": f"Data deleted: {mss}"}), 200
                else:
                    return jsonify({"message": f"Data not deleted: {mss}"}),400
            
        else:
            return jsonify({"message": "Data not inserted,password wrong"}), 400
    except Exception as e:
        return jsonify({'message': f'An unexpected error occurred {e}'}), 500      


@app.route('/api/outputdata', methods=['GET'])
def output():
    from dbmethods import dbBranch, dbBakery, dbDelivery, dbProducts, dbEmployee, dbSalary, dbTransaction, dbAccount, dbAsset, dbConnection, dbCost, dbOrder, dbSale, dbStatus, dbApp, dbAdmin

    #token = request.headers.get('Authorization')
    #if not token:
     #   return jsonify({'message': 'Token is missing'}), 403
    try:
        # Extract the actual token from 'Bearer <token>' format
      #  if token.startswith("Bearer "):
         #   token = token.split(" ")[1]
       # else:
        #    return jsonify({'message': 'Invalid token format. Expected format: Bearer <token>'}), 403

        #data = jwt.decode(token, app.secret_key, algorithms=["HS256"])
        #session['admindata'] = data  # 'Set the session variable
        #admin['id'] = data['id']
        #admin['name']=data['name']
        print(request.headers.get('Authorization'))
        verify_jwt_in_request()
        current_user = get_jwt()
        username = current_user.get('username')
        user_id = current_user.get('user_id')
        print("Current User:", current_user)

        
        response_data = {
            "branchdata": dbBranch.output_branchdata(user_id),
            "branchproductdata": dbBranch.output_acceptedproductdata(user_id),
            "branchdaydata": dbBranch.day_branchstatusdata(user_id),
            "branchmonthdata": dbBranch.monthly_branchstatusdata(user_id),
            "branchyeardata": dbBranch.year_branchstatudata(user_id),
            "deliverydata": dbDelivery.output_deliverydata(user_id),
            "deliverydaydata": dbDelivery.day_deliverystatus(user_id),
            "deliverymonthdata": dbDelivery.month_deliverystatus(user_id),
            "deliveryyeardata": dbDelivery.year_deliverystatus(user_id),
            "deliveryproductdata": dbDelivery.output_productdata(user_id),
            "bakerydata": dbBakery.output_bakerydata(user_id),
            "bakerydaydata": dbBakery.day_bakerystatus(user_id),
            "bakerymonthdata": dbBakery.month_bakerystatus(user_id),
            "bakeryyeardata": dbBakery.year_bakerystatus(user_id),
            "bakeryproductdata": dbBakery.output_productdata(user_id),
            "productdata": dbProducts.output_productdata(user_id),
            "employeedata": dbEmployee.output_employeedata(user_id),
            "salarydata": dbSalary.output_salarydata(user_id),
            "transactiondata": dbTransaction.output_transactiondata(user_id),
            "accountdata": dbAccount.output_accountdata(user_id),
            "assetdata": dbAsset.output_assetdata(user_id),
            "connectiondata": dbConnection.output_connectiondata(user_id),
            "costdata": dbCost.output_costdata(user_id),
            "orderdata": dbOrder.output_orderdata(user_id),
            "saledata": dbSale.output_saledata(user_id),
            "statusdata": dbStatus.output_statusdata(user_id),
            "admindata": dbAdmin.output_admindata(user_id)
        }
        return jsonify(response_data), 200

    except ExpiredSignatureError as e:
        print("Error:", str(e))
        return jsonify({'message': 'Token has expired'}), 403
    except InvalidTokenError as e:
        print("Error:", str(e))
        return jsonify({'message': 'Invalid token'}), 403
    except Exception as e:
        return jsonify({'message': f'An unexpected error occurred {e}'}), 500

@app.route('/test')
def test():
    admin_id = session.get('adminid', "gust")
    print(f"Session adminid retrieved: {admin_id}")
    return f"The admin ID is: "

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
