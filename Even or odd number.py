def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = 31

print(f"The Number {number} is {check_even_odd(number)}.")