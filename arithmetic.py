from . import encodings


@encodings.R
@encodings.opcode(0x07)
def ADD(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] + state.registers[rs2]


@encodings.R
@encodings.opcode(0x0E)
def CMP(state, rs1, rs2, rd):
    x = state.registers[rs1]
    y = state.registers[rs2]

    state.ccr = x - y
    state.ccn = (state.ccr < 0)
    state.ccz = (state.ccr == 0)
    state.ccv = False


@encodings.R
@encodings.opcode(0x08)
def MUL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] * state.registers[rs2]


@encodings.R
@encodings.opcode(0x04)
def SLL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] << state.registers[rs2]


@encodings.R
@encodings.opcode(0x05)
def SRL(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] >> state.registers[rs2]


@encodings.R
@encodings.opcode(0x06)
def SUB(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] - state.registers[rs2]
