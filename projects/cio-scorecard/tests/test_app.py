import unittest
from app import Metric, summarize, render, SAMPLE

class ScorecardTests(unittest.TestCase):
    def test_target_direction(self):
        self.assertTrue(Metric("availability", 99.9, 99.5).on_target)
        self.assertFalse(Metric("time", 3, 2, direction="down").on_target)
    def test_summary(self):
        result = summarize(SAMPLE)
        self.assertEqual(result["total"], 3)
        self.assertEqual(result["on_target"], 1)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            Metric("bad", 1, 2, "sideways")
    def test_report(self):
        self.assertIn("CIO SCORECARD", render(SAMPLE))

if __name__ == "__main__":
    unittest.main()
