import os
import unittest
from typing import List
from parameterized import parameterized
from NeetCode.solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    @parameterized.expand([
        # Equivalence Partitioning
        ("All oranges are already rotten", [[2,2,2],[2,2,2],[2,2,2]], 0),
        ("No oranges at all", [[0,0,0],[0,0,0],[0,0,0]], 0),
        ("All oranges are fresh and cannot be rotted", [[1,1,1],[1,1,1],[1,1,1]], -1),
        ("Mixed fresh and rotten oranges that can be rotted", [[2,1,1],[1,1,0],[0,1,1]], 4),
        # Boundary Value Analysis
        ("Minimum input size", [[0]], 0),
        ("Maximum input size", [[2 for _ in range(10)] for _ in range(10)], 0),
    ])
    def test_orangesRotting(self, name, input_data, expected_result):
        with self.subTest(name=name):
            print(name)
            self.assertEqual(self.solution.orangesRotting(input_data), expected_result)

if __name__ == "__main__":
    unittest.main()
