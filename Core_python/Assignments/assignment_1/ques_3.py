#Write a program to find quotient and remainder of two numbers.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
if num2 == 0:
    print("Division is not possible as the number is zero")
else:
    quotient = num1 / num2
    remainder = num1 % num2
    print("The Quotient is: ", quotient)
    print("The remainder is: ", remainder)