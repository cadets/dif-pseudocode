def mov(state, rs1, rs2, rd):
    state.registers[rd] = state.registers[rs1]
