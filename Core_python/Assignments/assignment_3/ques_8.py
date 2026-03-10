#  Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random

# Correct credentials
correct_userid = "gauri"
correct_password = "1234"

# User input
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Verify login
if userid == correct_userid and password == correct_password:
    
    # Generate 4 digit random number
    captcha = random.randint(1000, 9999)
    print("Enter this number to verify:", captcha)

    user_captcha = int(input("Enter the number: "))

    if user_captcha == captcha:
        print("Verification Successful")
    else:
        print("Verification Failed")

else:
    print("Invalid User ID or Password")