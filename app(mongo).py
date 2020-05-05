from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import  jsonify,request
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Users"
mongo = PyMongo(app)

@app.route('/users')
def users():
    users = mongo.db.users.find()
    resp = dumps(users)
    return resp


if __name__ == "__main__":
    app.run(debug = True)
