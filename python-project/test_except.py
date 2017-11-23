import unittest

class MyTest(unittest.TestCase):

    def test_split(self):
        s = 'hello world'
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(1)

if __name__ == '__main__':
    unittest.main()
