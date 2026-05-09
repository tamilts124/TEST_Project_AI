"""
Mathematical Logic Engine for Advanced Scientific Calculator
"""

import sympy as sp
from sympy import sin, cos, tan, cot, sec, csc, asin, acos, atan, sinh, cosh, tanh
from sympy import log, ln, exp, sqrt, Abs as abs, factorial, pi, E
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

class MathEngine:
    def __init__(self, precision=10):
        """
        Initialize the MathEngine with specified precision.
        
        Args:
            precision (int): Number of decimal places for floating point results
        """
        self.precision = precision
        # Define transformations for parsing expressions
        self.transformations = (standard_transformations + (implicit_multiplication_application,))
        
        # Define constants
        self.constants = {
            'pi': pi,
            'e': E
        }
    
    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression safely using SymPy.
        
        Args:
            expression (str): Mathematical expression as a string
            
        Returns:
            str: Evaluated result as a string with specified precision
        """
        try:
            # Replace constants in the expression
            for const_name, const_value in self.constants.items():
                expression = expression.replace(const_name, str(const_value))
            
            # Parse the expression with SymPy
            parsed_expr = parse_expr(expression, transformations=self.transformations)
            
            # Evaluate the expression
            result = parsed_expr.evalf(self.precision)
            
            # Format the result
            if result.is_real:
                return f"{float(result):.{self.precision}f}"
            else:
                return str(result)
                
        except Exception as e:
            return f"Error evaluating expression: {str(e)}"
    
    def set_precision(self, precision):
        """
        Set the precision for floating point results.
        
        Args:
            precision (int): Number of decimal places
        """
        self.precision = precision
    
    def scientific_functions_demo(self):
        """
        Demonstrate available scientific functions.
        """
        functions = [
            "sin(x), cos(x), tan(x)",
            "cot(x), sec(x), csc(x)",
            "asin(x), acos(x), atan(x)",
            "sinh(x), cosh(x), tanh(x)",
            "log(x) - natural logarithm",
            "ln(x) - natural logarithm",
            "exp(x) - exponential function",
            "sqrt(x) - square root",
            "abs(x) - absolute value",
            "factorial(n) - factorial"
        ]
        return functions

# Example usage:
# engine = MathEngine()
# result = engine.evaluate_expression("2*3 + sin(pi/2)")
# print(result)