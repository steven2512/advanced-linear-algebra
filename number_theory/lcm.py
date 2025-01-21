from number_theory.gcd import gcd

def lcm(num1: int, num2: int):
    return int(abs(num1 * num2) / gcd(num1, num2))

print(lcm(12,15))