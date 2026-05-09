"""
Demo Script for Math Engine
"""

from math_engine import MathEngine

def main():
    # Create an instance of the MathEngine
    engine = MathEngine()
    
    print("Math Engine Demo")
    print("=" * 30)
    
    # Test basic arithmetic
    print("Basic Arithmetic:")
    print("2 + 3 =", engine.evaluate_expression("2 + 3"))
    print("10 - 4 =", engine.evaluate_expression("10 - 4"))
    print("3 * 4 =", engine.evaluate_expression("3 * 4"))
    print("15 / 3 =", engine.evaluate_expression("15 / 3"))
    
    print("\nConstants:")
    print("pi =", engine.evaluate_expression("pi"))
    print("e =", engine.evaluate_expression("e"))
    
    print("\nTrigonometric Functions:")
    print("sin(0) =", engine.evaluate_expression("sin(0)"))
    print("sin(pi/2) =", engine.evaluate_expression("sin(pi/2)"))
    print("cos(0) =", engine.evaluate_expression("cos(0)"))
    print("cos(pi) =", engine.evaluate_expression("cos(pi)"))
    
    print("\nLogarithms:")
    print("ln(e) =", engine.evaluate_expression("ln(e)"))
    print("log(100) =", engine.evaluate_expression("log(100)"))
    
    print("\nComplex Expressions:")
    print("sin(pi/4) + cos(pi/4) =", engine.evaluate_expression("sin(pi/4) + cos(pi/4)"))
    print("sqrt(16) + 2^3 =", engine.evaluate_expression("sqrt(16) + 2**3"))
    
    print("\nAvailable Scientific Functions:")
    for func in engine.scientific_functions_demo():
        print("-", func)

if __name__ == "__main__":
    main()