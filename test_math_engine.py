"""
Test Suite for Math Engine
"""

import unittest
from math_engine import MathEngine

class TestMathEngine(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.engine = MathEngine()
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        self.assertEqual(self.engine.evaluate_expression("2 + 3"), "5.0000000000")
        self.assertEqual(self.engine.evaluate_expression("10 - 4"), "6.0000000000")
        self.assertEqual(self.engine.evaluate_expression("3 * 4"), "12.0000000000")
        self.assertEqual(self.engine.evaluate_expression("15 / 3"), "5.0000000000")
    
    def test_implicit_multiplication(self):
        """Test implicit multiplication."""
        self.assertEqual(self.engine.evaluate_expression("2(3 + 4)"), "14.0000000000")
        self.assertEqual(self.engine.evaluate_expression("3x"), "Error evaluating expression: undefined variable: x")
    
    def test_powers_and_roots(self):
        """Test power and root functions."""
        self.assertEqual(self.engine.evaluate_expression("2**3"), "8.0000000000")
        self.assertEqual(self.engine.evaluate_expression("sqrt(16)"), "4.0000000000")
    
    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        # sin(0) = 0
        self.assertEqual(self.engine.evaluate_expression("sin(0)"), "0.0000000000")
        # sin(pi/2) = 1
        self.assertEqual(self.engine.evaluate_expression("sin(pi/2)"), "1.0000000000")
        # cos(0) = 1
        self.assertEqual(self.engine.evaluate_expression("cos(0)"), "1.0000000000")
    
    def test_logarithms(self):
        """Test logarithmic functions."""
        # ln(e) = 1
        self.assertEqual(self.engine.evaluate_expression("ln(e)"), "1.0000000000")
        # log10(100) = 2
        self.assertEqual(self.engine.evaluate_expression("log(100)"), "2.0000000000")
    
    def test_constants(self):
        """Test mathematical constants."""
        self.assertEqual(self.engine.evaluate_expression("pi"), "3.1415926536")
        self.assertEqual(self.engine.evaluate_expression("e"), "2.7182818285")
    
    def test_complex_expressions(self):
        """Test complex expressions."""
        result = self.engine.evaluate_expression("sin(pi/4) + cos(pi/4)")
        # Should be approximately sqrt(2) = 1.414...
        self.assertEqual(result, "1.4142135624")
    
    def test_precision_setting(self):
        """Test precision setting."""
        self.engine.set_precision(5)
        self.assertEqual(self.engine.evaluate_expression("pi"), "3.14159")

if __name__ == '__main__':
    unittest.main()