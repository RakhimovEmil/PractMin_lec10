import redis
import pymongo

class Rediska:
	def __init__(self, redis_client):
		self.redis_client = redis_client
	
	def get(self,key):
                return self.cache.get(key)
	
	def put(self,key,value):
                self.cache.set(key,value)	

	def delete(self,key):
		self.cache.delete(key)       
	

	def exists(self,key):
		return self.cache.exists(key)

class Mango:
	def __init__(self, mongo_client):
		self.mongo_table = mongo_client['hw9']['cache']

	def get(self,key):
                return self.mongo_table.find_one({'key':key})["value"]

	def put(self,key,value):
                self.mongo_table.insert_one({'key':key, 'value':value})

	def delete(self, key):
		self.mongo_table.delete_one({'key':key})                                          
	def exists(self,key):
		return self.mongo_table.find_one({'key':key})
