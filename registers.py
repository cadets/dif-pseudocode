from . import encodings


#
# Register move.
#
# Copy the value from rs1 into rd.
#
@encodings.R
@encodings.opcode(0x0D)
def MOV(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1]
