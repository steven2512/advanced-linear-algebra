def gcd(num1: int, num2: int):
    dividend = num1 if num1 > num2 else num2
    divisor = num1 if num1 < num2 else num2
    remainder = dividend % divisor
    while remainder > 0: 
        if remainder == 0:
            break
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
        

    return divisor