from number_theory.lcm import gcd

def lcm(num1: int, num2: int):
    return abs(num1 * num2) / gcd(num1, num2)