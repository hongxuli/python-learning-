import pymongo


# client = MongoClient('mongodb://localhot:27017/')
client = pymongo.MongoClient(host='localhost', port=27017)

# db = client['test']
db = client.test

collection = db.students 

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170102',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

collection.insert_many([student1, student2])
results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)


