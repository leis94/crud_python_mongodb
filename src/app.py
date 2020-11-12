from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://admin:admin123#@cluster0.p49qk.mongodb.net/flask_mongodb?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/tasks', methods=['POST'])
def create_task():
    print(request)
    return 'Received'


if __name__== "__main__":
    app.run(debug=True)