# Advanced Scientific Calculator - Core Mathematical Logic Engine

This project implements the core mathematical logic engine for an advanced scientific calculator with high precision and comprehensive function support.

## Features

- Safe expression evaluation using SymPy
- Over 20 scientific functions (trigonometric, logarithmic, etc.)
- High precision calculations
- Support for mathematical constants (π, e)
- Implicit multiplication support
- Comprehensive error handling

## Installation

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

```python
from math_engine import MathEngine

# Create an instance
engine = MathEngine()

# Evaluate expressions
result = engine.evaluate_expression("sin(pi/2) + cos(0)")
print(result)  # Outputs: 2.0000000000
```

## Documentation

See `docs/technical_spec.md` for detailed technical specifications.

## Testing

Run the demo script to see the engine in action:
```
python demo.py
```

## Requirements

- Python 3.6+
- SymPy 1.12