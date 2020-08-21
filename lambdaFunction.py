x = 20

def adder(x):
    return lambda n: x + n

twoAdder = adder(x)

print(twoAdder(10))