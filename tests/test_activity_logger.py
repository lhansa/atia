import unittest
import csv
import os
from atia.process_monitor import ActivityLogger

class TestActivityLogger(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_activity_log.csv"
        self.logger = ActivityLogger(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_csv_creation(self):
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['timestamp', 'app', 'event'])

    def test_log_activity(self):
        self.logger.log_activity("TestApp", "start")
        self.logger.log_activity("TestApp", "end")
        
        with open(self.test_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            rows = list(reader)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0][1:], ["TestApp", "start"])
            self.assertEqual(rows[1][1:], ["TestApp", "end"])

if __name__ == "__main__":
    unittest.main()