import pymongo


if __name__== "__main__":
    print("Welcome to PyMongo")  
    # connecting to database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # print(client)

    # IF YOU WANT TO CREATE A NEW DATABASE THAN YOU MUST HAVE TO CREATE AT LEAST ONE COLLECTION AND DOCUMENT
    db = client['DB_NAME'] # creating a db 
    collection = db['COLLECTION_NAME'] # creating a collection

    # CREATING A DOCUMENT TO INSERT INTO COLLECTION
    dictionary = {
        
        "name" : "Manisha",
        "marks" : 98
    }
   
   # INSERT ONE DOCUMENTS INTO COLLECTION
    collection.insert_one(dictionary)

    insertThese = [
        {"_id": 1, "name":"Manisha", "location":"Bihar", "Marks":98},
        {"_id": 2, "name":"Harry", "location":"Delhi", "Marks":100},
        {"_id": 3, "name":"Kaushal", "location":"Agra", "Marks":75},
        {"_id": 4, "name":"Mahi", "location":"Bihar", "Marks":76}
    ]

    # INSERT MANY DOCUMENTS INTO COLLECTION
    collection.insert_many(insertThese)