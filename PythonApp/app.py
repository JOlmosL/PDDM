#from flask import Flask
#
#app = Flask(__name__)
#
#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"
#
#-------------------------------------
#from flask import Flask
#
#app = Flask(__name__)
#
#@app.route("/hello/<name>", methods = ['GET'])  
##Provides a command to the method that we are going to be using. In this case it says: In this route you are going to use method GET
#def hello_world(name):
#    return "<p>Hello, World!</p>" + name
#
#-------------------------------------
#from flask import Flask, jsonify
#
#app = Flask(__name__)
#
##Create a Model.
##Static Locla Model
#
#tasks = [
#    {'task_name': 'task 1', 'owner': 'Patricio'},
#    {'task_name': 'task 2', 'owner': 'Pedro'}
#]
#
#@app.route("/", methods = ['GET'])  
#def hello_world():
#    return jsonify({'tasks': tasks})#convert a JSON into a string that can be returned and printed in the browser
#
#
#-------------------------------------
#from flask import Flask, jsonify, request
#
#app = Flask(__name__)
#
##Create a Model.
##Static Locla Model
#
#tasks = [
#    {'task_name': 'task 1', 'owner': 'Patricio'},
#    {'task_name': 'task 2', 'owner': 'Pedro'}
#]
#
#@app.route('/', methods=['GET'])
#def get_hello():
#    return "Hello to the Flask Todo App"
#
#@app.route("/tasks", methods = ['GET'])  
#def get_all_tasks():
#    return jsonify({'tasks': tasks})
#
# POST Method to add info to the array 
#@app.route('/', methods=['POST'])
#def madd_new_task():
#    if not request is None:
#        new_task = {
#            'task_name': request.json['task_name'],
#            'owner': request.json['owner'],
#        }
#        tasks.append(new_task)
#        print("sucess, ")
#
#    else:
#        return "Error, Request is Empty"
#    
#    return request.json
#
#-------------------------------------
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#Create a Model.
#Static Locla Model

tasks = [
    
]


###### DataBase Functionality ######
## Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)    #Object from Alchemy

#Create a new database using SQL
#Create a new table using SQL. Create Table...
#cursor.
#Open a session Connection to the Database  using this cursor
#Execute the SQL queries we need
#Close the session or connection. ALWAYS CLOSE IT
#Create a class that will be the model
# Create a table through a model
#Translate our Database results into the Python Object Model

#This is our Model Alquemy will translate this
class Task(db.Model): #This is only an Entity
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(250), nullable=False)
    owner = db.Column(db.String(250), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False)


if not os.path.isfile('sqlite:///todo.db'): #If this file does not exists...
    db.create_all()

@app.route('/', methods=['GET'])
def get_hello():
    return "Hello to the Flask Todo App"

@app.route("/tasks", methods = ['GET'])  
def get_all_tasks():
    all_tasks = db.session.query(Task).all()   #Creating a new session  and get from Task all the tables
    for task in all_tasks:
        temp_task = {
            'task_name':    task.task_name,
            'owner':        task.owner,
            'complete':     task.complete
        }
        tasks.append(temp_task)

    return jsonify({'tasks': tasks})

# POST Method to add info to the array
@app.route('/tasks', methods=['POST'])
def add_new_tasks():
    if not request is None: 
        new_task = Task(
            task_name = request.json['task_name'],
            owner = request.json['owner']
        )

        db.session.add(new_task)
        db.session.commit()

        #tasks.append(new_task)
        return "Sucess. "
    else: 
        return "Error, Request is empty"
    return request.json


    #Remember doing-> venv\Scripts\activate | flask run