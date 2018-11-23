"""
Top-level description of the DIF instruction set
"""

from . import arithmetic, memory, registers, tables
from .encodings import encodings

#
# Mapping of instruction opcodes (text) to a pseudocode function and an encoding
#
instructions = {
    'CMP': (arithmetic.CMP, 'R'),
    'LDGS': (memory.LDGS, 'W'),
    'LDUB': (memory.LDUB, 'R'),
    'MOV': (registers.MOV, 'R'),
    'SETX': (tables.SETX, 'Index'),
}
