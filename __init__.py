"""
Top-level description of the DIF instruction set
"""

from . import arithmetic, memory, registers, tables
from . import encodings

#
# Mapping of instruction opcodes (text) to a pseudocode function and an encoding
#
instructions = {
    'CMP': (arithmetic.cmp, encodings.r),
    'LDGS': (memory.ldgs, encodings.w),
    'LDUB': (memory.ldub, encodings.r),
    'MOV': (registers.mov, encodings.r),
    'SETX': (tables.setx, encodings.index),
}
