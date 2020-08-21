def unpack_range(args):
    """The * operator on function arguments unpacks lists into individual elements or collects them all into a list.
    
    This is similar to the spread and rest operator (...) in JavaScript"""
    print(list(range(*args)))

unpackRange([1,10])

print(unpackRange.__doc__)