#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

temp = int(input("Enter the temperature in Celcius: "))
Faranite = temp * (9 /5) + 32
Celcius = ((Faranite - 32) / 9) * 5
print("Conversion of temp(Celcius) into Faranite: ",Faranite)
print("Conversion of temp(faranite) into Celcius: ",Celcius)