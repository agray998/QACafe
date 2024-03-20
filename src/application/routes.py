# TODO: Implement Routing
from application import app, db
from flask import request

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def homepage():
    ...

@app.route('employee-details', methods=['GET'])
def get_employees():
    ...