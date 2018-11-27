from . import encodings


@encodings.R
@encodings.opcode(0x0D)
def MOV(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1]
