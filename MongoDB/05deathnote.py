import pymongo

myclient=pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.ew0bu.mongodb.net/")
mydb=myclient["DB1"]
coll1=mydb["collection1"]

query = {
    "name":'Dingo'
}

coll1.delete_one(query)