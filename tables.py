from . import encodings


@encodings.Index
@encodings.opcode(0x25)
def SETX(state, rd, index):
    state.registers[rd] = state.tables.integers[index]
