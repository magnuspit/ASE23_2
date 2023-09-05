import unittest
from mycode import my_function

class Test1(unittest.TestCase):

    def test_my_function(self):
        self.assertEqual(my_function(), 6)

if __name__ == '__main__':
    unittest.main()
