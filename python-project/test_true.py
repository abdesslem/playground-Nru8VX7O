import unittest

class MyTest(unittest.TestCase):

    def test_true(self):
        self.assertTrue('FOo'.isupper())

    def test_in(self):
	self.assertIn('1', ['2',7,'a','1'])

if __name__ == '__main__':
    unittest.main()
