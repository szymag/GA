import unittest
from src.EvalFunction import EvalFunction
import numpy as np

class TestEvalFunction(unittest.TestCase):


    def test_to_problem_range(self):
        self.assertAlmostEqual((-100, -100), EvalFunction(['000000000000000000000000000000000000000000']).to_problem_range(), delta=0.001)
        self.assertAlmostEqual((100, 100), EvalFunction(['111111111111111111111111111111111111111111']).to_problem_range(), delta=0.001)
        self.assertAlmostEqual((100, -100), EvalFunction(['111111111111111111111000000000000000000000']).to_problem_range(), delta=0.001)
        self.assertAlmostEqual((-100, 100), EvalFunction(['000000000000000000000111111111111111111111']).to_problem_range(), delta=0.001)
        self.assertAlmostEqual((1.3675219380960186, 74.40718384131614), EvalFunction(['100000011100000000011110111110011110110111']).to_problem_range(), delta=(0.01, 0.01))

    def test_problem_function(self):
        self.assertAlmostEqual(0.501128, EvalFunction(['000000000000000000000000000000000000000000']).problem_function(), delta=0.001)
        self.assertAlmostEqual(0.501128, EvalFunction(['111111111111111111111111111111111111111111']).problem_function(), delta=0.001)
        self.assertAlmostEqual(0.501128, EvalFunction(['111111111111111111111000000000000000000000']).problem_function(), delta=0.001)
        self.assertAlmostEqual(0.501128, EvalFunction(['000000000000000000000111111111111111111111']).problem_function(), delta=0.001)
        self.assertAlmostEqual(0.495595, EvalFunction(['100000011100000000011110111110011110110111']).problem_function(), delta=0.001)


if __name__ == '__main__':
    unittest.main()