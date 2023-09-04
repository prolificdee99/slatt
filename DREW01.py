Time_Leaving=int(input("Enter the time you left home :"))
Time_arriving=int(input("Enter the time you arrived at home:"))
if Time_Leaving >= 6 and Time_arriving <=6:
    print("You arrived at time and so therefore you are obedient")
elif Time_Leaving >=7 and Time_arriving <=7:
    print("Not bad but try harder","")
else:
    print("You are too stubborn")