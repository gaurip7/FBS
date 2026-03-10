# Write a program to input any alphabet and check whether it is vowel or consonant.

# vowel = ['a','e','i','o','u','A','E','I','O','U']

ch = input("Enter a character: ")
if len(ch) != 1:
    print("Please enter only one character")
elif ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")