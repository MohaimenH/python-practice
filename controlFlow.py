name = input("Please enter your name: ")

if (len(name) < 1):
    print("Please enter a name!")
elif (len(name) > 20):
        print("Name too long!")
else:
    print(name)

myList = input("Please enter an array seperated by spaces: ")
myList = myList.split()

stop = False

while (stop == False):
    index = input("Please enter the index you want to delete (or N if you want to stop): ")

    if (index == "N"):
        stop = True
        break
    else:
        del myList[int(index)]
        print(myList)

print(myList)
print("Thanks for using the application " + name + "!")