import pymongo

#Conexion con MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["PickOut"]

usuarios = mydb["usuarios"]
roles = mydb["roles"]