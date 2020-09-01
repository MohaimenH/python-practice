words = ["apple", "ball", "cat", "dog"]

print(len(words))

wordsLength = [len(x) for x in words]

print(wordsLength)

def printFirstLetter(arg):
    return arg[0]

firstLetters = [printFirstLetter(x) for x in words]

print(firstLetters)

#Using functions is useful in these cases.

del words[0:2]

print(words)
