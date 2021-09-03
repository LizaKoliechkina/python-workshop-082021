from collections import defaultdict

a = defaultdict(lambda: 17)
print(a)
print(a['b'])


def return_five():
    return 5


five = defaultdict(return_five)
print(five['5'])
print(five['five'])

