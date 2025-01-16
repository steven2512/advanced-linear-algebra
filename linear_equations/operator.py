class Operator:
    
    def __init__(self, operator: str):
        if self.operator not in ['+', '-', '*', '/']:
            raise ValueError("Not a valid Mathematical Operator")
        self.operator = operator

    def __str__(self):
        if self.operator == '+':
            return 'Addition'
        elif self.operator == '-':
            return 'Subtraction'
        elif self.operator == '*':
            return 'Multiplication'
        elif self.operator == '/':
            return 'Division'