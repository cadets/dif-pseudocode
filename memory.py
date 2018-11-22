def ldgs(state, imm, rd):
    state.registers[rd] = state.variables.globals[imm]


def ldub(state, rs1, rs2, rd):
    assert rs1 == 0

    addr = state.registers[rs1]
    state.registers[rd] = state.mem.load(addr, 1)