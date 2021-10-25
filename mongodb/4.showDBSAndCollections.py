import pymongo




if __name__== "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    allDatabases = client.list_database_names()
    print(allDatabases)

    coll = client['manisha']
    print(coll.list_collection_names())
