def arithSeq(a: int, d: int, n: int = 5) -> int: #n=5 is the default value
    "Print an arithmetic sequence of length 'n', starting at 'a', with common difference 'd'."

    last = a + (n-1) * d
    for x in range (a, last+1, d):
        print(x)

start = 3
diff = 3
length = 5

arithSeq(start, diff, length)

# print(arithSeq.__annotations__)