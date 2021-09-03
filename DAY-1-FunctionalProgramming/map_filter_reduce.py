data = [
    {
        "name": "pawel",
        "age": 36,
        "city": "krakow",
        "hobbies": ["python", "programming", "drugs"]
    },
    {
        "name": "lukasz",
        "age": 36,
        "city": "krakow",
        "hobbies": ["bike", "hitch-hike", "moto"]
    },
    {
        "name": "krzysztof",
        "age": "22",
        "city": "krakow",
        "hobbies": ["cooking", "python", "machine_learning"]
    },
    {
        "name": "Kasia",
        "age": 32,
        "city": "wroclaw",
        "hobbies": ["music", "books", "django"]
    },
    {
        "name": "Norbert",
        "age": "21",
        "city": "Krakow",
        "hobbies": ["football", "games", "technology"]
    },
    {
        "name": "tomasz",
        "age": 22,
        "city": "krakow",
        "hobbies": ["esport", "microcontrollers", "programming"]
    },
    {
        "name": "Mateusz",
        "age": 28,
        "city": "krakow",
        "hobbies": ["python", "films", "music"]
    },
    {
        'name': 'Mariusz',
        'age': '36',
        'city': 'krakow',
        'hobbies': ['python', 'books', 'netflix']
    },
    {
        "name": "marcin",
        "age": 33,
        "city": "krakow",
        "hobbies": ["python", "alcohol", "football"]
    },
    {
        "name": "Andrzej",
        "age": 29,
        "city": "Wroclaw",
        "hobbies": ["chess", "finance", "history"]
    },
    {
        "name": "Liza",
        "age": 21,
        "city": "Lodz",
        "hobbies": ["poledance", "snowboarding", "bike"]
    }
]

# assign function declaration to variable is FUNCTION EXPRESSION
is_palindrome = lambda x: x.lower() == x.lower()[::-1]
print('Is palindrom?', is_palindrome('kajak'))

print('Average age: ')
print(sum(map(lambda x: int(x['age']), data)) / len(data))

print('Average age of people from Cracow: ')
people_from_krakow = list(filter(lambda x: x['city'].lower() == 'krakow', data))
print(sum(map(lambda x: int(x['age']), people_from_krakow)) / len(people_from_krakow))

from functools import reduce


def test(current_elm, accumulator):
    print(current_elm, accumulator)
    print('*' * 30)
    return current_elm + accumulator


x = reduce(lambda current_elm, accumulator: current_elm + accumulator, [1, 2, 3])
x = reduce(test, [1, 2, 3], 0)
print(x)

age = reduce(lambda acc, ce: (int(ce['age']) if ce['city'].lower() != 'krakow' else 0) + acc, data, 0)
print(age)

# UNIQUE HOBBIES
hobbies = reduce(lambda acc, ce: set(ce['hobbies']) | acc, data, set())
print(hobbies)


# FIRST 2 CHARS FROM EACH KEY-VALUE PAIR OF THE DICT:
def test(accumulator, current_element):
    temp = []
    for value in current_element.values():
        if isinstance(value, list):
            for hobby in value:
                temp.append(hobby[:2])
        else:
            temp.append(str(value)[:2])
    accumulator.append(''.join(temp))
    return accumulator


x = reduce(test, data, [])
print(x)
