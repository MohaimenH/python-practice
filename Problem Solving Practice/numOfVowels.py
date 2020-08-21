import re

##Using Regex

numOfInput = int(input())

numberOfVowels = ""

for i in range(numOfInput):
    inputStr = input()
    counter = re.findall("[aeiouy]", inputStr)
    numberOfVowels += str(len(counter)) + " "

print(numberOfVowels)   


##Without Regex

# numOfInput = int(input())

# numberOfVowels = ""
# counter = 0

# for i in range(numOfInput):
#     inputStr = input()
#     for j in range(len(inputStr)):
#         if (inputStr[j] == "a" or inputStr[j] == "e" or inputStr[j] == "i" or inputStr[j] == "o" or inputStr[j] == "u" or inputStr[j] == "y"):
#             counter += 1
#     numberOfVowels += str(counter) + " "
#     counter = 0

# print(numberOfVowels)   