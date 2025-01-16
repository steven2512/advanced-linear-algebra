class Variable:
    """Represents standard Mathematical Variables used in equations"""
    def __init__(self, symbol):
        self.value = None
        self.symbol = symbol
    def set_value(self, value):
        self.value = value
    def __str__(self):
        print(f"Variable/Unknown {self.symbol} = {self.value}")
