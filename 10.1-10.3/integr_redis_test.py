import unittest
import redis
import os
from repository import Rediska

class RedisTestCase(unittest.TestCase):
	def setUp(self):
    		redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    		self.cache = RedisRepository(redis_client)
    		os.system('docker run --rm --detach --name emils-rediska-test --publish 6379:6379 redis')

	def test_get_returns_value_from_cache(self):
        	self.cache.put("key", "value")
        	value = self.cache.get("key")
        	self.assertEqual(value, "value")

	def tearDown(self):
        	os.system('docker stop emils-rediska-test')

if __name__ == '__main__':
        unittest.main()
