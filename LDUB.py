#
# LDUB: encoding R
#
@encodings.R
def LDUB(state, rs1, rs2, rd):
    assert rs1 == 0

    addr = state.registers[rs1]
    state.registers[rd] = state.mem.load(addr, 1)

