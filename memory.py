from . import encodings


#
# Load a user defined variable.
#
# The ldgs instruction has two modes of operation and is intended to be used
# only for scalar values. The first mode of operation is when the value provided
# in var is less than DIF_VAR_OTHER_UBASE. This will cause DTrace to look up a
# pre-defined scalar variable such as curthread, while the second mode of
# operation will result in looking up a user defined variable in a DIF program.
# The result of this instruction will be put into the register rd.  Unlike the
# ldga instruction, the var field is 16 bits long, as opposed to 8 bits due to
# the fact that the variable that is being loaded is a scalar and does not
# require indexing operations.
#
# Unlike the ldga instruction, the var field is 16 bits long, as opposed to 8
# bits due to the fact that the variable that is being loaded is a scalar and
# does not require indexing operations.
#
@encodings.W
@encodings.opcode(0x29)
def LDGS(state, imm, rd):
    state.registers[rd] = state.variables.globals[imm]


#
# Load Unsigned Byte.
#
# Load the value pointed to by rs1 into rd. This is an unsigned instruction
# and will not perform sign extension.
#
@encodings.R
@encodings.opcode(0x1F)
def LDUB(state, rs1, rs2, rd):
    assert rs1 == 0

    addr = state.registers[rs1]
    state.registers[rd] = state.mem.load(addr, 1)
