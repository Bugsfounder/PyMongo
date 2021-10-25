import pymongo




if __name__== "__main__":
    print("Welcome to PyMongo")  
    # connecting to database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # creating a new db you must have to create a collection and a document to create your database
    db = client['manisha'] # creating a db 
    collection = db['mySampleCollectionForManisha']




    # UPDATE ONE 
    prev = {"name":"Manisha"}
    nextupdated = {'$set':{"location":"Mumbai"}}
    collection.update_one(prev, nextupdated)
       
    # UPDATE MANY 
    prev = {"name":"Kaushal", "Marks":75}
    nextupdated = {'$set':{"location":"Mars"}}
    up = collection.update_many(prev, nextupdated)
    print(up.modified_count)
