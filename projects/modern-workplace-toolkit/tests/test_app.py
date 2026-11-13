import unittest
from app import validate, report

class EndpointTests(unittest.TestCase):
    def test_complete_stage(self):
        self.assertTrue(validate("secure", {"encryption": True, "patch_policy": True}).passed)
    def test_missing(self):
        self.assertIn("patch_policy", validate("secure", {"encryption": True}).missing)
    def test_unknown(self):
        with self.assertRaises(ValueError):
            validate("destroy", {})
    def test_report(self):
        self.assertIn("retire: GAPS", report({}))

if __name__ == "__main__":
    unittest.main()
