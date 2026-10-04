try:
    age = int("abc")
    print(age)
except ValueError:
    print("Invalid age: please enter a number")
