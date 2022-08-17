import pymongo
from mongoengine import Document, StringField, connect

try:
     MONGOHOST = "localhost"
     MONGOPORT = "27017"
     MONGO_TIEMPO_FUERA = 1000

     MONGO_URI = "mongodb://" + MONGOHOST + ":" + MONGOPORT + "/"

     MONGO_BASEDATOS = "PickOut"
     #conexion con pymongo
     client = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
     baseDatos = client[MONGO_BASEDATOS]
     
     #conexion con mongoengine
     x = connect(MONGO_BASEDATOS)
     
     print(client)
     print(x)
except:
     print("Conexion fallida")