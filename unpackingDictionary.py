def whoAmI(*, firstName, lastName, grade):
    "Works similar to the * operator on function arguments, except it is a dictionary type now - with keys and values"
    print("My name is " + firstName + " " + lastName + ". " + "I study in Grade " + grade + ".")

student = {"firstName": "Mohaimen", "lastName": "Hassan", "grade": "12"}

whoAmI(**student)