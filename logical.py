def AND(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] & state.registers[rs2]


def OR(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] | state.registers[rs2]


def XOR(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] ^ state.registers[rs2]
