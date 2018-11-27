from . import encodings


@encodings.Index
def SETX(state, rd, index):
    state.registers[rd] = state.tables.integers[index]
