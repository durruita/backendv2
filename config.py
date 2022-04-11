from http import client
import pymongo
import certifi


mongo_url = ""

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

db = client.get_database("StoreCH26")