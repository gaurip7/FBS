# Write a program to enter P, T, R and calculate Compound Interest.

principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
period_of_time = float(input("Enter the period of time: "))
final_amount = principal_amount * (1 + rate_of_interest / 100) ** period_of_time
compound_interest = final_amount - principal_amount
print("The final amount is: ", final_amount)
print("Compound Interest is: ", compound_interest)
