# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

# equilateral --> all sides are equal
# isosceles   --> any two sides are equal
# scalene     --> all sides are different

s1 = int(input("Enter the side 1: "))
s2 = int(input("Enter the side 2: "))
s3 = int(input("Enter the side 3: "))
if (s1 > 0 and s2 > 0 and s3 > 0):
    if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):       
        if s1 == s2 and s2 == s3:
            print("It is an Equilateral Traingle")
        elif (s1 == s2 or s1 == s3 or s2 == s3):
            print("It is an Isosceles Traingle")
        else:
            print("Is is a Scalene Traingle")
    else:
        print("Not a valid triangle")
else:
    print("Triangle sides must be positive numbers")