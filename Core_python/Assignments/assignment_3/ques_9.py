#  Input 5 subject marks from user and display grade(eg.First class,Second class ..)

# Program to calculate grade from 5 subject marks

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))
total = m1 + m2 + m3 + m4 + m5
average = total / 5
print("Average Marks =", average)
if average >= 60:
    print("Grade: First Class")
elif average >= 50:
    print("Grade: Second Class")
elif average >= 40:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")