questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
answers2 = ['V2', ', sir', ', navy blue to be specific']

for q, a, a2 in zip(questions, answers, answers2):
    print('What is your {0}?  It is {1} {2}.'.format(q, a, a2))