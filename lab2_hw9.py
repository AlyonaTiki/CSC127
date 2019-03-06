#Alyona Karmazin
#2/13/19
#this program asks user to input message, then prints it with encryption by shifting letters to right 13 times

message = input("Please enter a word: ")
print("your word in code is")
for c in message:
    if ord(c)<110:
        print(chr(ord(c)+13), end='')
    else:
        print(chr(ord(c) - 13), end='')