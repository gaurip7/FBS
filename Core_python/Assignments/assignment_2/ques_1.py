#Convert the time entered in hh,min and sec into seconds.

hour = int(input("Enter the hour: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))
Total_second = (hour * 3600) + (minutes * 60) + seconds
print("Time Converted into seconds: ",Total_second)
