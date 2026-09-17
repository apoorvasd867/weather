degree=int(input("Enter the Degree:"))
if degree <=20:
    print("Cold weather")
elif degree >35 and degree <=55:
    print("Normal weather")
else :
    print("Hot! weather")
    fahrenheit=((degree*1.8)+32)
    print("The Fahrenheit value is",fahrenheit,"F")