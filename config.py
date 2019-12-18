import telebot
import pymongo
import dns
from telebot import TeleBot
from pymongo import MongoClient
client = MongoClient('mongodb+srv://please:works@cluster0-ffmk7.mongodb.net/test?retryWrites=true&w=majority')
bot = TeleBot('953656997:AAFIiRaovdh1gEwc1hckyTpB2hPiy9-BrnQ')
coll_users = client.db.users
coll_targets = client.db.targets
coll_to_do = client.db.to_do