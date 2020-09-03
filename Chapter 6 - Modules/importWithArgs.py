def printer(*args):

    if (len(args) == 0):
        print("No input")
    else:
        print(args)

#To call directly from console and use the arguments:
#__name__ == "__main__" is true whenever the program is run.

if (__name__ == "__main__"):
    import sys
    print("I ran!")
    # print(sys.argv[1])
    