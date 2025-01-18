class Operator:
    
    def __init__(self, operator: str):
        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Not a valid Mathematical Operator")
        self.operator = operator

    def __str__(self):
        return self.operator