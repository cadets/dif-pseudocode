def ADD(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] + state.registers[rs2]


def CMP(state, rs1, rs2, rd):
    x = state.registers[rs1]
    y = state.registers[rs2]

    state.ccr = x - y
    state.ccn = (state.ccr < 0)
    state.ccz = (state.ccr == 0)
    state.ccv = False


def MUL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] * state.registers[rs2]


def SLL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] << state.registers[rs2]


def SRL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] >> state.registers[rs2]


def SUB(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] - state.registers[rs2]
