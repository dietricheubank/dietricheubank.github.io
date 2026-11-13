import unittest
from app import Project, optimize

class OptimizerTests(unittest.TestCase):
    def test_exact_portfolio(self):
        items = [Project("A", 6, 10), Project("B", 5, 8),
                 Project("C", 4, 9, ("A",)), Project("D", 3, 4)]
        self.assertEqual(optimize(items, 10), (["A", "C"], 19, 10))
    def test_dependency(self):
        self.assertEqual(optimize([Project("A", 10, 1), Project("B", 1, 9, ("A",))], 5), ([], 0, 0))
    def test_invalid(self):
        with self.assertRaises(ValueError):
            optimize([Project("A", 1, 3), Project("A", 1, 4)], 4)

if __name__ == "__main__":
    unittest.main()
