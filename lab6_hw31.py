# Alyona Karmazin
# 3/12/19
# this program asks for time and displays greetings

time = int(input("Enter hour (in 24 hour time): "))

if time < 12:
    print("Good Morning")
elif 17 > time > 12:
    print("Good Afternoon")
else:
    print("Good Evening")

