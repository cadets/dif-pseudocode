#
# LDGS: encoding W
#
@encodings.W
def LDGS(state, imm, rd):
    state.registers[rd] = state.variables.globals[imm]

