numbers = input()
numbers = numbers.split()
for x in range(len(numbers)):
    numbers[x] = int(numbers[x])
numbers.sort()
print(str(numbers[299]) + " " + str(numbers[0]))
