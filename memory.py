from . import encodings


@encodings.W
@encodings.opcode(0x29)
def LDGS(state, imm, rd):
    state.registers[rd] = state.variables.globals[imm]


@encodings.R
@encodings.opcode(0x1F)
def LDUB(state, rs1, rs2, rd):
    assert rs1 == 0

    addr = state.registers[rs1]
    state.registers[rd] = state.mem.load(addr, 1)