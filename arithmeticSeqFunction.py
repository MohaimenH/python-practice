def arithSeq(a, d, n=5): #n=5 is the default value
    "Print an arithmetic sequence of length 'n', starting at 'a', with common difference 'd'."

    last = a + (n-1) * d
    for x in range (a, last+1, d):
        print(x)

arithSeq(3, 3, 10)