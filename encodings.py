class encoding(object):
    """
    A DIF instruction encoding.

    An encoding of a DTrace DIF instruction has a name and a list of operand
    names. TODO: get fancier with bitwidths, etc.
    """

    def __init__(self, name, operands):
        self.name = name
        self.operands = operands

    def __call__(self, f):
        f.encoding = self
        return f

    def bit_widths(self):
        return (width for (name, width) in self.operands)

    def operand_names(self):
        return (name for (name, width) in self.operands)


def opcode(value):
    """
    Decorate a function with its opcode.
    """

    def decorate(func):
        func.opcode = value
        return func

    return decorate


#
# DTrace has three encodings: B (branch), R (register) and W (wide, maybe?).
#
B = encoding('B', [('label', 24)])
R = encoding('R', [('rs1', 8), ('rs2', 8), ('rd', 8)])
W = encoding('W', [('imm', 16), ('rd', 8)])

# Er... and encoding four our of three is...
Index = encoding('Index', [('rd', 8), ('index', 16)])
