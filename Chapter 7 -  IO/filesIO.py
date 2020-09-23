with open('dummyFile2', 'w') as f:
    # Do operations on file inside 'with'
    # for line in f:
    #     print(line, end='')
    print(f.write('This is a test again\n'))

with open('dummyFile') as f:
    read_data = f.readlines()
    print(f.tell())
    f.seek(3,0)
    read_data2 = f.read()

print(read_data)
print(read_data2)

with open('dummyFile3', 'w') as f:
    value = ('the answer', 42)
    s = str(value)
    f.write(s)

# print(f.closed)
