from pymongo import MongoClient
import certifi
#Conexion a mongo local. Configuracion de base de datos de manera local
MONGO_URI = "mongodb://localhost"
PORT = 27017

#Conexion a mongo remota
MONGO_URI= "mongodb+srv://Ciclo4GrupoJ1:Palaciodejusticia1@cluster0.qjks82d.mongodb.net/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConnection():
    try:
        #conexion local 
        #client=MongoClient(MONGO_URI,port= PORT)
        #Conexion remota
        client=MongoClient(MONGO_URI,tlsCAFile=ca)
        db = client["Ciclo4_GrupoJ1_db"]
    except:
        print("Error en conexion con la Database")
    return db


