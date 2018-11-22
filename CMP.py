#
# CMP: encoding R
#
def cmp(state, rs1, rs2, rd):
    x = state.registers[rs1]
    y = state.registers[rs2]

    state.ccr = x - y
    state.ccn = (state.ccr < 0)
    state.ccz = (state.ccr == 0)
    state.ccv = False

