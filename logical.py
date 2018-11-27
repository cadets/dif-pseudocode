from . import encodings


#
# Bitwise AND
#
@encodings.R
@encodings.opcode(0x03)
def AND(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] & state.registers[rs2]


#
# Bitwise OR
#
@encodings.R
@encodings.opcode(0x01)
def OR(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] | state.registers[rs2]


#
# Bitwise exclusive OR
#
@encodings.R
@encodings.opcode(0x02)
def XOR(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1] ^ state.registers[rs2]
