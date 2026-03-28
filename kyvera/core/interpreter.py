from .ast import NumberNode, StringNode, BinOpNode, VarAccessNode


class Interpreter:
    def __init__(self, language=None):
        self.variables = {}
        # Language pack for booleans
        self.language = language or {"TRUE": "True", "FALSE": "False"}

    def interpret(self, program_node):
        for statement in program_node.statements:
            self.visit(statement)

    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node):
        raise Exception(f"No visit method for {type(node).__name__}")

    def visit_PrintNode(self, node):
        value = self.evaluate(node.expression)
        print(value)

    def visit_VariableNode(self, node):
        value = self.evaluate(node.value)
        self.variables[node.name] = value

    def visit_IfNode(self, node):
        condition = self.evaluate(node.condition)

        if condition:
            for stmt in node.body:
                self.visit(stmt)
        elif node.else_body:
            for stmt in node.else_body:
                self.visit(stmt)

    def evaluate(self, node):

        # Numbers
        if isinstance(node, NumberNode):
            return node.value

        # Strings
        if isinstance(node, StringNode):
            return node.value

        # Variable access
        if isinstance(node, VarAccessNode):
            if node.name in self.variables:
                return self.variables[node.name]
            else:
                raise Exception(f"Undefined variable '{node.name}'")

        # Binary operations
        if isinstance(node, BinOpNode):
            left = self.evaluate(node.left) if node.left else None
            right = self.evaluate(node.right)

            if node.operator == "+":
                return str(left) + str(right)
            elif node.operator == "-":
                return left - right
            elif node.operator == "*":
                return left * right
            elif node.operator == "/":
                return left / right
            elif node.operator == ">":
                return left > right
            elif node.operator == "<":
                return left < right
            elif node.operator == "==":
                return left == right
            elif node.operator == "!=":
                return left != right
            elif node.operator == ">=":
                return left >= right
            elif node.operator == "<=":
                return left <= right
            elif node.operator == "and":
                return left and right
            elif node.operator == "or":
                return left or right

        # Booleans: map to current language
        if isinstance(node, bool):
            return self.language["TRUE"] if node else self.language["FALSE"]

        raise Exception(f"Cannot evaluate node: {type(node).__name__}")