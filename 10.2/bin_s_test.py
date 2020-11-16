import unittest
from main import binary_s

class bin_sTestCase(unittest.TestCase):
	def test(self):
		d = [1,2,3,4,5,6,7,8,9]
		self.assertEqual(binary_s(2, d), 1)
		self.assertEqual(binary_s(3, d), 2)
		self.assertEqual(binary_s(4, d), 3)
		self.assertEqual(binary_s(5, d), 4)
		self.assertEqual(binary_s(6, d), 5)

if __name__ = '__main__':
	unittest.main()
