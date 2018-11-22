#
# DTrace has three encodings: B (branch), R (register) and W (wide, maybe?).
#
b = ['label']
r = ['rs1', 'rs2', 'rd']
w = ['imm', 'rd']

# And more (unnamed) encodings?
index = ['rd', 'index']
