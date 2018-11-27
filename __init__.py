"""
Top-level description of the DIF instruction set
"""

import importlib
import inspect

#
# Mapping of instruction opcodes (text) to a pseudocode function and an encoding
#
instructions = {}

for category in ['arithmetic', 'logical', 'memory', 'registers', 'tables']:
    m = importlib.import_module('.' + category, 'instructions')
    fns = [
        (n, f) for (n, f) in inspect.getmembers(m) if inspect.isfunction(f)
    ]

    instructions.update(dict(fns))
