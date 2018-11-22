#
# DTrace has three encodings: B (branch), R (register) and W (wide, maybe?).
#
encodings = {
    'B': ['label'],
    'R': ['rs1', 'rs2', 'rd'],
    'W': ['imm', 'rd'],

    # Er... and encoding four our of three is...
    'Index': ['rd', 'index'],
}
