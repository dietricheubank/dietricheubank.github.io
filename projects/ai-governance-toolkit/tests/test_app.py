import unittest
from app import UseCase, assess

class GovernanceTests(unittest.TestCase):
    def test_low_flag(self):
        self.assertFalse(assess(UseCase("Synthetic FAQ classifier"))["review_required"])
    def test_multiple_flags(self):
        result = assess(UseCase("Hypothetical agent", sensitive_data=True, external_actions=True, human_review=False))
        self.assertEqual(len(result["review_areas"]), 3)
        self.assertTrue(result["review_required"])
    def test_name(self):
        with self.assertRaises(ValueError):
            assess(UseCase(" "))

if __name__ == "__main__":
    unittest.main()
