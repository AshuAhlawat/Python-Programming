import pymongo

username=input("enter id here:")
password = str(input("enter pass here: "))
myclient = pymongo.MongoClient(
    "mongodb+srv://"+username+":"+password+"@cluster0.ew0bu.mongodb.net/")
mydb = myclient["DB1"]
coll = mydb["collection1"]


demo = {
    "_id": "102",
    "name": "ashu",
    "edu": "B-tech CSE",
    "reg": 12016043
}
demo1 = {
    "_id": "101",
    "name": "Gaurav",
    "edu": "B-tech CSE",
    "reg": 12017777
}
demo2={
    "_id":"106",
    "name":"Buff",
    "edu":"B-Tech Cse",
    "reg":"nahi pata"
}
coll.insert_many([demo2])
# pymongo.DB1.collection1.insert_one()/insert_many([])

