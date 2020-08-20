def arguments(first, second=2, third=3):
    print(first)
    print(second)
    print(third)

arguments(10,third=30, second=20)

def argumentsStrict(first, /, second=2, *, third=3): # Before /, positional only. After *, keyword only. In between is both.
    print(first)
    print(second)
    print(third)

argumentsStrict(10, third=30, second=20)

