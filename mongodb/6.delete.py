import pymongo




if __name__== "__main__":
    print("Welcome to PyMongo")  
    # connecting to database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # creating a new db you must have to create a collection and a document to create your database
    db = client['manisha'] # creating a db 
    collection = db['mySampleCollectionForManisha']


    # DELETE ONE 
    record = {"name":"Harry"}
    collection.delete_one(record)

    # DELETE MANY 
    record = {"name":"Manisha"}
    up = collection.delete_many(record)
    print(up.deleted_count)
