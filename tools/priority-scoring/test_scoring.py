import unittest

from scoring import evaluate


class ScoringTests(unittest.TestCase):
    def test_weighted_score(self):
        result = evaluate((5, 4, 3, 4, 2))
        self.assertAlmostEqual(result.score, 3.9)
        self.assertEqual(result.priority, "High")

    def test_priority_bands(self):
        for x, expected in [(5, "Critical"), (4, "High"), (3, "Medium"), (1, "Low")]:
            self.assertEqual(evaluate((x,) * 5).priority, expected)

    def test_invalid_ratings(self):
        for ratings in [(0, 2, 3, 4, 5), (2, 3), (1, 2, 3, 4, 6)]:
            with self.assertRaises(ValueError):
                evaluate(ratings)

    def test_invalid_weights(self):
        with self.assertRaises(ValueError):
            evaluate((3,) * 5, weights=(50, 25, 20, 15, 10))


if __name__ == "__main__":
    unittest.main()
