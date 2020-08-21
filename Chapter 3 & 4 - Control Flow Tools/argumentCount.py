def func(*args):
    print(len(args))

func(1,2,3,4,5)

def func2(**args):
    for names in args:
        print(args[names])

func2(firstName="Mohaimen", lastName="Hassan")
