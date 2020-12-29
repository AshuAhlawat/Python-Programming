import pymongo
import pandas as pd

myclient = pymongo.MongoClient(
    "mongodb+srv://Dingo:1234@cluster0.ew0bu.mongodb.net/DB1?retryWrites=true&w=majority")
mydb = myclient["DB1"]
coll1 = mydb["collection1"]
coll2 = mydb["collection2"]

# id is either 101 or 102 or registration number is less than 12017777 and the name ashu must not be in the list
query = {

    "$or": [
        {"_id": {"$in": ['101', '102']}},
        {"reg": {"$lt": 12017777}}
    ],
    "name": {"$regex": "^a"},
    "reg": {"$nin": [12016043]}
}

data = coll1.find(query)
print(pd.DataFrame(data).to_string())
