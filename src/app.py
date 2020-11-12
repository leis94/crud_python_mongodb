from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://admin:admin123#@cluster0.p49qk.mongodb.net/flask_mongodb?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/tasks', methods=['POST'])
def create_task():
    title = request.json['title']
    description = request.json['description']

    if title and description:
        id = mongo.db.tasks.insert_one(
            {
                'title': title,
                'description': description
            }
        )
        response = {
            'id': str(id),
            'title': title,
            'description': description
        }
        return response
    else:
        return not found()


@app.errorhandler(404)
def not_found(error=None):
    #Handle errors
    response = jsonify ({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__== "__main__":
    app.run(debug=True)