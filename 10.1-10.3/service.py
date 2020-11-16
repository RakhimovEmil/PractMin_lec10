:x
from flask import jsonify, json
import redis 
import mongo
from repository import Rediska, Mango
import logging
import logging.config

class Service:
	def __init__(self):
		redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
		mongo_client = pymongo.MongoClient(host='0.0.0.0', port=27017)
		self.redis=Rediska(redis_client)
		self.mongo=Mango(mongo_client)

	def get(self,filename):
		logging.basicConfig(level=logging.DEBUG)
		logging.debug('get for key %s', filename)
		if self.redis.exists(filename):
			return self.redis.get(filename)
		else:
			logging.warning('no data in cache for key %s', filename)
		if self.mongo.exists(filename):
			lol=json.loads(json_util.dumps(self.mongo.get(filename)))
			self.redis.put(filename,lol)
			return lol
		else:
			logging.error('no data in database for key %s', filename)
		return

	def put(self, filename, value):
		self.mongo.put(filename, value)

	def delete(self, filename):
		if self.redis.exists(filename):                                                   	self.redis.delete(filename)       
		if self.mongo.exists(filename):
			self.mongo.delete(filename)      
