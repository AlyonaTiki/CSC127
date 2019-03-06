#Alyona Karmazin
#2/28/19
#this program count days and hours until weekend

hours = int(input("Enter hours until weekend: "))
days = hours/24
print(int(days))
leftover = hours % 24
print(leftover)