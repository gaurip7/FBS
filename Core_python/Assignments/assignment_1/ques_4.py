#Write a program to enter P, T, R and calculate simple Interest.

principal_amount = int(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
period_of_time = int(input("Enter the period of time: "))
simple_interest = (principal_amount * rate_of_interest * period_of_time) / 100
print("The simple interest is: ",simple_interest)





