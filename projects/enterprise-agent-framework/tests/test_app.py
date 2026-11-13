import unittest
from app import example_agent

class AgentTests(unittest.TestCase):
    def test_allowlist(self):
        a = example_agent()
        self.assertEqual(a.execute("shell", {"command": "anything"}), "DENIED_UNKNOWN_TOOL")
        self.assertEqual(len(a.audit), 1)
    def test_approval(self):
        a = example_agent()
        self.assertEqual(a.execute("restart_mock", {"service": "demo"}), "AWAITING_APPROVAL")
        self.assertEqual(a.execute("restart_mock", {"service": "demo"}, approved=True), "SIMULATED_RESTART:demo")
    def test_read_only(self):
        self.assertEqual(example_agent().execute("read_status", {"service": "demo"}), "DEMO:demo:DEGRADED")

if __name__ == "__main__":
    unittest.main()
