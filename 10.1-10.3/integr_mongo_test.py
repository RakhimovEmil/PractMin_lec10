import unittest
import pymongo
import os
from repository import Mango

class MongoTestCase(unittest.TestCase):
    def setUp(self):
        mongo_client = pymongo.MongoClient(host='0.0.0.0', port=27017)
        self.table = MongoRep(mongo_client)
        os.system('docker run --rm --detach --name emils-mongo-test  --publish 27017:27017 mongo')

    def test_get_returns_value_from_cache(self):
        self.table.put("key", "value")
        value = self.table.get("key")
        self.assertEqual(value, "value")

    def tearDown(self):
        os.system('docker stop emils-mongo-test')

if __name__ == '__main__':
	unittest.main()
