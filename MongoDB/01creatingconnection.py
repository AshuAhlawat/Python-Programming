import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://Dingo:1234@cluster0.ew0bu.mongodb.net/DB1?retryWrites=true&w=majority")
mydb = myclient["DB1"]
var1 = mydb["collection1"]
print(var1)
dbs = myclient.list_database_names() 
print(dbs)
