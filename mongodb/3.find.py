import pymongo




if __name__== "__main__":
    print("Welcome to PyMongo")  
    # connecting to database
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # IF YOU WANT TO CREATE A NEW DATABASE THAN YOU MUST HAVE TO CREATE AT LEAST ONE COLLECTION AND DOCUMENT
    db = client["manisha"] # creating a db 
    collection = db["mySampleCollectionForManisha"] # creating a collection

    # FIND ONE 
    one = collection.find_one({"name":"Manisha"})
    # print(one)

    # FIND ALL 
    allDocs = collection.find({"name":"Manisha"})
    allDocs = collection.find({"name":"Manisha"},{"name": 0, "_id":0} )
    allDocs = collection.find({"name":"Manisha"},{"name": 1} )
    allDocs = collection.find({"name":"Manisha"},{"name": 1} ).limit(3)
    allDocs = collection.find({"name":"Mahi", "Marks":{"$lte":90}} )

    # print(allDocs.count())

    print(collection.count_documents({"name":"Manisha"}))

    for docs in allDocs:
        print(docs)