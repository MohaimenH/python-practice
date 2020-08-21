#We can convert complex loops into simple lists

evenNumbers = [x for x in range(10) if (x%2==0)] #The way this works: [*format* *loop* *condition*]. The loop and condition can be moved and multiple in number.

print(evenNumbers)

# print(x) - This statement will not work because x is not defined.

#Using lambda function is also okay but here will be a None at each else statement
# evenNums = list(map((lambda x: x if (x%2==0) else None), range(10)))
# print(evenNums)

#The above is a shorthand and more readable version of:
# evenNums = []
# for x in range(10):
#     if (x%2 == 0): evenNums.append(x)
# print(evenNums)

