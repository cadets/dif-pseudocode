from . import encodings


@encodings.R
def ADD(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] + state.registers[rs2]


@encodings.R
def CMP(state, rs1, rs2, rd):
    x = state.registers[rs1]
    y = state.registers[rs2]

    state.ccr = x - y
    state.ccn = (state.ccr < 0)
    state.ccz = (state.ccr == 0)
    state.ccv = False


@encodings.R
def MUL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] * state.registers[rs2]


@encodings.R
def SLL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] << state.registers[rs2]


@encodings.R
def SRL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] >> state.registers[rs2]


@encodings.R
def SUB(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] - state.registers[rs2]
