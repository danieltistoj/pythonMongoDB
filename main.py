import pymongo
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
try:
    cliente = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    cliente.server_info()
    print("Coneccion a mongo exitosa")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)
