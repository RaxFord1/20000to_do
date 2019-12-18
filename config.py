import pymongo
import dns
from pymongo import MongoClient
client = MongoClient('mongodb+srv://please:works@cluster0-ffmk7.mongodb.net/test?retryWrites=true&w=majority')
coll_users = client.db.users
coll_targets = client.db.targets
coll_to_do = client.db.to_do
