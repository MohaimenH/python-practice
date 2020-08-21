def wordJoin(*args, seperator='/'):
    result = seperator.join(args)
    print(result)

wordJoin("Hello","World", seperator=" ")