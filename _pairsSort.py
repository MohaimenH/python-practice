#This example is from the tutorial

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1]) #Takes in the input of a pair and returns the value of its second index - thus sorting in alphbetical order.
print(pairs)
