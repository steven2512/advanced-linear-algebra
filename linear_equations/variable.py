class Variable:
    """Represents standard Mathematical Variables used in equations"""
    def __init__(self, symbol: str, exponent = 1):
        self.value = None
        self.symbol = symbol
        self.exponent = exponent
    def get_symbol(self):
        return self.symbol
    def get_exponent(self):
        return self.exponent
    def set_value(self, value):
        self.value = value
    def __str__(self):
        return f"{self.symbol}"

