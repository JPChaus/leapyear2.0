import unittest

class TestCase(unittest.TestCase):
    def test_divFour(self):
        self. assertEqual(leapyear.calcLeapYear(2000), "2000 is a Leap Year.")

if __name__ == '__main__':
    unittest.main()