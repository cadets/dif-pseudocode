def SETX(state, rd, index):
    state.registers[rd] = state.tables.integers[index]
