import random

if __name__ == '__main__':

    inputNumber = input("Please enter digit from 0 to 500:\n")

    if inputNumber.isnumeric():
        start = int(inputNumber)
        if start >= 0 and start <= 500:
            end = 501
            result = 0
            for digit in range(start, end):
                result = result + digit

            print(result)
            exit(0)

    print("Incorrect input, try again!")
