# pip install libs if necessary
import csv
import datetime 
import json
from pymongo import MongoClient
import bson

def jsonReader(the_json):
    with open(the_json) as json_data:
        the_dict = json.load(json_data)
    return the_dict

# start run
if __name__ == '__main__':

	username = '###'
	password = '###'
	client = MongoClient('mongodb://%s:%s@###/?authSource=admin&readPreference=primary&replicaSet=rs0' % (username, password))
	db = client["meta"]

	pathJSON = '###.json' # enter relative path to json here

	paths = jsonReader(pathJSON)

	bulk = db.assets.initialize_unordered_bulk_op()

	for dic in paths:
		some_id = ObjectId(dic["#"])
		some_field = dic["#"]
			
		bulk.find({"_id": asset_id}).update({"$set":{"some_field": some_field, "updated_at": datetime.datetime.now()}})
		print 'updated some id: ' + str(some_id) + ' with some field ' + some_field
	t = bulk.execute()
	print(t)