a = set(["apple","banana","banana","onions"])

print(a)

b = set("queue")

print(b)

shoppingCart = {"yoghurt","rice","onions","rice","bread"}

print(shoppingCart)

print("yoghurt" in shoppingCart)

print(a-shoppingCart) #Elements in A but not in B
print(a & shoppingCart) #Elements in A and B
print(a | shoppingCart) #Elements in A or B
print(a ^ shoppingCart) #Elements in A or B but not both (XOR)