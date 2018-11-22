#
# LDGS: encoding W
#
def ldgs(state, imm, rd):
    state.registers[rd] = state.variables.globals[imm]

