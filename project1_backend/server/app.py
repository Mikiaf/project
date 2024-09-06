from flask import Flask,jsonify
from config import db
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/cobakery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/helloworld')
def helloworld():
    return "hello world"

@app.route('/dataoutput')
def dataoutput():
        from dbmethods import dbBranch
        branch = dbBranch()
        return jsonify(branch.output_branchdata())
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
        app.run(debug=True)