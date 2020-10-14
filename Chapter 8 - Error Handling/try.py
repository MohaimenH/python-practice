try:
    x = int(input("Enter a number: "))
    print(f"The number is {x}")
    # raise RuntimeError # We can raise errors if we want.
except (ValueError, RuntimeError):
    print("Oops, thats not a number.")
else:
    print("Else is reached if try is executed.")
finally:
    print("Finally statement") # It is executed as part of try, and before any return/continue/break statement.