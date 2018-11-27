#
# AND: encoding R
#
@encodings.R
def AND(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] & state.registers[rs2]

