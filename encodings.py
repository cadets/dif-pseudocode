class encoding(object):
    """
    A DIF instruction encoding.

    An encoding of a DTrace DIF instruction has a name and a list of operand
    names. TODO: get fancier with bitwidths, etc.
    """

    def __init__(self, name, operand_names):
        self.name = name
        self.operand_names = operand_names

    def __call__(self, f):
        f.encoding = self
        return f


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
B = encoding('B', ['label'])
R = encoding('R', ['rs1', 'rs2', 'rd'])
W = encoding('W', ['imm', 'rd'])

# Er... and encoding four our of three is...
Index = encoding('Index', ['rd', 'index'])
