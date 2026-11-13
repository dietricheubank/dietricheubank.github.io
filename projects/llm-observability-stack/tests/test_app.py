import unittest
from app import Metrics

class MetricsTests(unittest.TestCase):
    def test_counters(self):
        m = Metrics()
        m.record(25, 200)
        m.record(40, 503)
        self.assertEqual((m.requests, m.errors, m.total_latency_ms), (2, 1, 65))
        self.assertIn("demo_llm_errors_total 1", m.prometheus())
    def test_reject_negative_latency(self):
        with self.assertRaises(ValueError):
            Metrics().record(-1, 200)
    def test_reject_status(self):
        with self.assertRaises(ValueError):
            Metrics().record(2, 999)

if __name__ == "__main__":
    unittest.main()
