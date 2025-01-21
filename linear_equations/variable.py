class Variable:
    """Represents standard Mathematical Variables used in equations"""
    def __init__(self, symbol: str, exponent = 1):
        self.symbol = symbol
        self.exponent = exponent
    def get_symbol(self):
        return self.symbol
    def get_exponent(self):
        return self.exponent
    def set_value(self, value):
        self.value = value
    def __str__(self):
        return f"{self.symbol}{'^'+str(self.exponent) if self.exponent != 1 else ''}" if self.exponent!=0 else ''

