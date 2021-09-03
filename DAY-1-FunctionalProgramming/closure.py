# Design Pattern - FACTORY
# CLOSURE - func object that allows access to variables outside local scope

def power_n(n):
    def inner(x):
        return x ** n
    return inner


power_2 = power_n(2)
power_3 = power_n(3)
print(power_2(10))
print(power_3(10))


def sentence(name):
    age = 32  # not used in inner function

    def inner(city):  # closure
        return f'My name is {name} and live in {city}'

    return inner


print(sentence('Ala')('Wroclaw'))

full_sentence = sentence('Ala')  # - global scope

print(full_sentence.__closure__)
print(full_sentence.__closure__[0].cell_contents)
print(full_sentence('Krakow'))  # - object inner !!!

# PERSISTENCE: GENERATORS, CLASSES, GLOBAL VARIABLES
# GLOBAL VARIABLES ARE IN GLOBAL EXECUTION SCOPE, ARE CLEANED ONLY AFTER PROGRAM EXECUTION
