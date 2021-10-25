from tkinter import *
import pymongo
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
dbName = client['myNotebook']

class Backend():
    global username
    allAvailableCollections = dbName.list_collection_names()
    userCollection = dbName['users']
    notebookCollection = dbName['notebooks']
    noteCollection = dbName['notes']
    timestamp =  datetime.datetime.utcnow()
    
    # USERS COLLECTIONS FUNCTIONS 
    # GET ALL COLLECTIONS 
    def allCollections(self):
        for collection in self.allAvailableCollections:
            print(collection)

    # CREATE A NEW USER FUNCTION 
    def createUser(self):
        userCol = self.userCollection
        newDoc = {
            "email": f"{email.get()}",
            "name": f"{username.get()}",
            "password": f"{password.get()}",
            "timestamp":{"$timestamp": self.timestamp}
        }
        isExists = userCol.count_documents({"email":f"{email.get()}"})
        if isExists == 0 and len(email.get())>5:
            userCol.insert_one(newDoc)
            print("Account Created Successfully")
        else:
            print("This email Already Exists, Email must be greater than 5 characters")

    # FIND A USER IF EXISTS 
    def findUser(self):
        userCol = self.userCollection
        newDoc = {
            "email": f"{email.get()}",
            "name": f"{username.get()}",
            "password": f"{password.get()}"
            # "timestamp":{"$timestamp":{self.timestamp}}
        }
        allDocs = userCol.find_one(newDoc)
        if userCol.find_one(newDoc):
            return True
        else:
            return False

    # UPDATE A USER 
    def updateUser(self):
        userCol = self.userCollection
        try:
            newDoc = {
                "email": f"{email.get()}",
                "name": f"{username.get()}",
                "password": f"{password.get()}"
                # "timestamp":{"$timestamp":{self.timestamp}}
            }
            allDocs = userCol.find_one()
            print(allDocs)
            # UPDATE MANY 
            prev = {"name":f"{allDocs['name']}", "email":f"{allDocs['email']}", "password":f"{allDocs['password']}" }
            nextupdated = {'$set': newDoc}
            up = userCol.update_one(prev, nextupdated)
            print(up.modified_count)
        except Exception as e:
            print(e)
            print("Something went wrong")

    # DELETE A USER 
    def deleteUser(self):
        userCol = self.userCollection
        newDoc = {
            "name": f"{username.get()}",
            "email": f"{email.get()}",
            "password": f"{password.get()}",
        }
        isExists = userCol.count_documents({"email":f"{email.get()}"})
        print(isExists)
        if isExists > 0:
            self.userCollection.delete_one(newDoc)
        else:
            print("This user not Exists")

    # NOTEBOOK FUNCTIONS ARE HERE 
    # CREATE A NEW NOTEBOOK 
    def createNotebook(self):
        pass

    # SEARCH NOTEBOOKS 
    def searchNotebooks(self):
        pass

    # SEARCH NOTEBOOK 
    def searchNotebook(self):
        pass

    # UPDATE NOTEBOOK 
    def updateNotebook(self):
        pass

    # DELETE NOTEBOOK 
    def deleteNotebook(self):
        pass


if __name__ == "__main__":
    db = Backend()
    print(db.allCollections())
    # GUI STARTS HERE
    root = Tk()
    root.title("Backend Crud Operations")  # GUI TITLE
    root.geometry("600x500")  # GUI HEIGHT WIDTH

    heading = Label(text="Welcomet to Backend", font="lucida 30 bold", pady=20)
    heading.pack()

    username  = StringVar()
    email  = StringVar()
    password  = StringVar()

    usernameEnt = Entry(textvariable=username)
    usernameEnt.pack()

    emailEnt = Entry(textvariable=email)
    emailEnt.pack()

    passwordEnt = Entry(textvariable=password)
    passwordEnt.pack()

    Button(text="Create", command=db.createUser).pack()
    Button(text="Delete", command=db.deleteUser).pack()
    Button(text="Find", command=db.findUser).pack()
    Button(text="Update", command=db.updateUser).pack()
    # GUI ENDS HERE
    root.mainloop()
