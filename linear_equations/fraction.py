from number_theory.lcm import lcm

class Fraction:

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def get_decimals(self):
        return self.numerator/self.denominator
    
    def multiply_fraction(self, fraction):
        self.numerator *= fraction.get_numerator()
        self.denominator *= fraction.get_denominator()
    
    def multiply_decimals(self, decimals: float):
        self.numerator *= decimals

    def divide_fraction(self, fraction):
        self.numerator *= fraction.get_denominator()
        self.denominator *= fraction.get_numerator()
    
    def divide_decimals(self, decimals: float):
        self.denominator *= decimals

    def add_fraction(self, fraction):
        lcm = lcm(self.denominator, fraction.get_denominator())
        self.denominator = lcm
        self.numerator*= (lcm / self.denominator) + fraction.get_numerator() *  (lcm / self.denominator)
    def add_decimals(self, decimals: float):
        self.numerator += decimals * self.denominator


    

    



    def simplify(self):
        #find greatest common divisor
        pass

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    

        
    