"""
Top-level description of the DIF instruction set
"""

from . import arithmetic, memory, registers, tables
from .encodings import encodings

#
# Mapping of instruction opcodes (text) to a pseudocode function and an encoding
#
instructions = {
    'CMP': (arithmetic.cmp, 'R'),
    'LDGS': (memory.ldgs, 'W'),
    'LDUB': (memory.ldub, 'R'),
    'MOV': (registers.mov, 'R'),
    'SETX': (tables.setx, 'Index'),
}
