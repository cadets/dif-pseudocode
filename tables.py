from . import encodings


#
# Retrieve an integer from the integer table.
#
# Look up an integer value stored in the DIF integer table and place it
# into rd. This instruction performs no bounds checking.
#
@encodings.Index
@encodings.opcode(0x25)
def SETX(state, rd, index):
    state.registers[rd] = state.tables.integers[index]
