def setx(state, rd, index):
    state.registers[rd] = state.tables.integers[index]
