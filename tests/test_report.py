import unittest

from features import reports


class TestReports(unittest.TestCase):
    def test_average_rooms_returns_average(self):
        data = {"history": [5, 6, 4]}
        self.assertEqual(reports.average_rooms(data), 5.0)

    def test_average_rooms_empty_history(self):
        data = {"history": []}
        self.assertEqual(reports.average_rooms(data), 0.0)


if __name__ == "__main__":
    unittest.main()
