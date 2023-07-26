
import random

if __name__ == '__main__':

    amount = 30

    digits = []

    for i in range(amount):
        digits.append(random.randint(1,10))
    print("Array with 30 random numbers from 1 to 10:")
    print(digits)

    for i, digit in enumerate(digits):
        if (digit == 7):
            digits[i] = 3
    print("Array updated:")
    print(digits)
