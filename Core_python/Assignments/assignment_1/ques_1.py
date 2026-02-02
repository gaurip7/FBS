 #Write a program to calculate the percentage of student based on marks of any 5 subjects.

English = int(input("Enter your English marks: "))
Maths = int(input("Enter your Maths marks: "))
Science = int(input("Enter your Science marks: "))
History = int(input("Enter your History marks: "))
Civics = int(input("Enter your Civics marks: "))
percentage = (English + Maths + Science + History + Civics) / 5
print("Your Percentage is",percentage)
