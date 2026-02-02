#Write a Program to input two angles from user and find third angle of the triangle.

first_angle = int(input("Enter the first angle value: "))
second_angle = int(input("Enter the second angle value: "))
third_angle = 180 - (first_angle + second_angle)
print("A third angle by calculating the two values is",third_angle)