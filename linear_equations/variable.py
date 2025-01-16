class Variable:
    """Represents standard Mathematical Variables used in equations"""
    def __init__(self, symbol: str):
        self.value = None
        self.symbol = symbol
    def get_symbol(self):
        return self.symbol
    def set_value(self, value):
        self.value = value
    def __str__(self):
        print(f"{self.symbol} = {self.value}")
