from . import encodings


@encodings.R
def MOV(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1]
