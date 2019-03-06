#Alyona Karmazin
#2/27/19
#this program asks user to input words, then prints a sentence using words from input

noun = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")

sentence = ("If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN.")
sentence = sentence.replace("NOUN", noun)
sentence = sentence.replace("VERB1", verb1)
sentence = sentence.replace("VERB2", verb2)

print(sentence)