from . import encodings


@encodings.W
def LDGS(state, imm, rd):
    state.registers[rd] = state.variables.globals[imm]


@encodings.R
def LDUB(state, rs1, rs2, rd):
    assert rs1 == 0

    addr = state.registers[rs1]
    state.registers[rd] = state.mem.load(addr, 1)
