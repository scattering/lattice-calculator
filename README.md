# lattice-calculator

[![PyPI version](https://badge.fury.io/py/icp-lattice-calculator.svg)](https://pypi.org/project/icp-lattice-calculator/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Performs lattice calculations for crystallography and neutron scattering, primarily for triple-axis spectrometers.

## Installation

```bash
pip install icp-lattice-calculator
```

## Usage

```python
from lattice_calculator import Lattice, modvec, scalar, Orientation
import numpy as np

# Define a cubic lattice
lattice = Lattice(
    a=5.0, b=5.0, c=5.0,
    alpha=90, beta=90, gamma=90,
    orient1=np.array([[1, 0, 0]]),
    orient2=np.array([[0, 1, 0]])
)

# Calculate Q magnitude
q_mag = modvec(1, 0, 0, 'r', lattice)
```

## Features

- Crystal lattice definitions with arbitrary unit cells
- Orientation matrix calculations
- Conversion between reciprocal and real space
- Vector operations (modvec, scalar, angle calculations)
- Integration with [rescalculator](https://github.com/scattering/rescalculator) for TAS resolution

## License

MIT
