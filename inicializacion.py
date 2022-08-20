from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__, template_folder='templates')
app.config["MONGODB_SETTINGS"] = [
{
"db": "PickOut",
"host": "localhost",
"port": 27017,
"alias": "default",}
]
db = MongoEngine()
db.init_app(app)
print(db)