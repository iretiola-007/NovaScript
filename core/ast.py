class ProgramNode:
    def __init__(self, statements):
        self.statements = statements


class VariableNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PrintNode:
    def __init__(self, value):
        self.value = value


class NumberNode:
    def __init__(self, value):
        self.value = value


class StringNode:
    def __init__(self, value):
        self.value = value


class VarAccessNode:
    def __init__(self, name):
        self.name = name


class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right