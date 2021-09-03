def pipeline(number):  # generator factory
    numbers = (i for i in range(number))
    squared = (x ** 2 for x in numbers)
    abstract = (-i for i in squared)
    result = (n + 1 for n in abstract)
    return result


pipe = pipeline(10)
print(next(pipe))
print(next(pipe))
print(next(pipe))
print(next(pipe))
print(next(pipe))

from itertools import accumulate

print(list(accumulate([2, 3, 5, 6])))
