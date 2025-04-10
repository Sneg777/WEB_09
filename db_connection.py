import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import redis
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["HW_09"]

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
