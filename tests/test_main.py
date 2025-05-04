import unittest
from app import main
import os

class TestReport(unittest.TestCase):
    def test_generate_report(self):
        result = main.generate_report()
        self.assertTrue(os.path.exists("report.html"))
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
