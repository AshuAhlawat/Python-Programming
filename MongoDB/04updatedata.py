import pymongo
from pymongo.operations import ReplaceOne

myclient=pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.ew0bu.mongodb.net/DB1?retryWrites=true&w=majority")
mydb=myclient["DB1"]
coll1=mydb["collection1"]

query={
    "_id":'102'
}

updateDB={
    "$set":{"reg":12016043}
}

coll1.update_one(query,updateDB)

replaceDB={
    "_id":'101',
    "name":'gaurav',
    "edu":"aaji ghanta",
    "reg":12014197
}

# coll1.replace_one(query,replaceDB)