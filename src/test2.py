import unittest
from mycode import my_function

class Test2(unittest.TestCase):

    def test_my_function_type(self):
        self.assertTrue(isinstance(my_function(), int))

if __name__ == '__main__':
    unittest.main()
