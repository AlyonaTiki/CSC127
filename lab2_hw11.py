#Alyona Karmazin
#2/13/19
#this program asks user to input DNA string, then count the length, then give a dectimal number od % C and G in DNA

message = input("Please enter a DNA string: ")
print(len(message))
C = message.count("C")
G = message.count("G")
content = ((C+G)*100)/len(message)/100
print("GC-content is ", content)
