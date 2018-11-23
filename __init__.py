"""
Top-level description of the DIF instruction set
"""

from . import arithmetic, logical, memory, registers, tables
from .encodings import encodings

#
# Mapping of instruction opcodes (text) to a pseudocode function and an encoding
#
instructions = {
    'ADD': (arithmetic.ADD, 'R'),
    'AND': (logical.AND, 'R'),
    'CMP': (arithmetic.CMP, 'R'),
    'LDGS': (memory.LDGS, 'W'),
    'LDUB': (memory.LDUB, 'R'),
    'MOV': (registers.MOV, 'R'),
    'MUL': (arithmetic.MUL, 'R'),
    'OR': (logical.OR, 'R'),
    'SETX': (tables.SETX, 'Index'),
    'SLL': (arithmetic.SLL, 'R'),
    'SRL': (arithmetic.SRL, 'R'),
    'SUB': (arithmetic.SUB, 'R'),
    'XOR': (logical.XOR, 'R'),
}
