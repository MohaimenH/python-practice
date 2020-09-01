personA = {'firstName': "Mohaimen", 'lastName': "Hassan", 'grade':"University"}
personB = {'firstName': "Asma"}

personB['lastName'] = "Hassan"

if (personA['lastName'] == personB['lastName']):
    print("Family members!")

print(list(personA))
print(sorted(personA))

print('firstName' in personA)
print('middleName' not in personB)