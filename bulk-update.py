import csv
import datetime 
import json
from pymongo import MongoClient
import bson

def jsonReader(the_json):
    with open(the_json) as json_data:
        the_dict = json.load(json_data)
    return the_dict

if __name__ == '__main__':

	username = '###'
	password = '###'
	client = MongoClient('mongodb://%s:%s@###/?authSource=admin&readPreference=primary&replicaSet=rs0' % (username, password))
	db = client["meta"]

	pathJSON = '###.json' 

	paths = jsonReader(pathJSON)

	bulk = db.assets.initialize_unordered_bulk_op()

	for dic in paths:
		some_id = ObjectId(dic["#"])
		some_field = dic["#"]
			
		bulk.find({"_id": asset_id}).update({"$set":{"some_field": some_field, "updated_at": datetime.datetime.now()}})
	t = bulk.execute()
