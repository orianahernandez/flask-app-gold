from pymongo import MongoClient

MONGO_URI="mongodb+srv://admin:admin@cluster0-kz6dm.mongodb.net/test?retryWrites=true&w=majority"

#CRUD (create,read,update,delete)
def db_connect(MONGO_URI,db_name,col_mame):
    client=MongoClient(MONGO_URI)
#creamos una base de datos llamada  mi app:
    database=client['db_name']
    collection= database['col_name']
    return collection 

def db_insert_user(collection,user):
	return collection.insert_one(user)

def db_find_all(collection,query={}):
	return collection.find(query)


if __name__ == '__main__':
    print("MongoClient imported successfully!")
    

    #creamos una coleccion llamada users:
    #users= database['users']
    #creamos usuario demo:
    #usuario demo={
     #"user": "oriana hernandez",
     #mail": "orijoa@gmail.com"
    #}
    #users.insert_one(usuario_demo)
