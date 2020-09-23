import math

name = "Mohaimen"
age = 21

print(f"I am {name}, and I am {age} years old.")

test = "Hi\nNew Line"
print(str(test))
print(repr(test))

print(str(f'{math.pi:.5f}'))

print('We are the {1}. We are {0}.'.format('champions','loser'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

table2 = {'John': 4127, 'Jane': 2113, 'Jon': 8637678}

print('Jack: {0[Jack]:d}, Jane: {1[Jane]:d}'.format(table, table2))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))

