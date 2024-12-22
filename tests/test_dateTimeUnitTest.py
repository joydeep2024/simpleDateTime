import unittest
from src.customDateTime import returnDateTime

class DateTimeTestCase(unittest.TestCase):

    def test_current_datetime(self):
        result = returnDateTime()
        self.assertTrue(result != None)