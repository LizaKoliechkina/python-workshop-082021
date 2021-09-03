# PROTOCOLS -> DUNDER METHODS
# a + b -> __add__
# len(a) -> __len__
# a in [a, b, c] -> __contains__
# for state -> __iter__
# with statement -> __enter__, __exit__
# a == b -> __eq__
# f'' -> __format__
# sized -> __len__
# iterator -> __iter__, __next__
# context manager -> __enter__, __exit__
# data descriptor -> __get__, __set__, __delete__
# hashable -> __hash__

from collections.abc import Iterator, Iterable


class Fib:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib


fibbo = Fib(0, 1)

for i in range(5):
    print(next(fibbo))

print(isinstance(fibbo, Iterator))  # protocol Iterator is true, requirements of the protocol are met
print(isinstance(fibbo, Iterable))


from time import perf_counter, sleep


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, exc_type, exc_val, exc_tb):  # exception type, value and traceback (exception location)
        self.end = perf_counter()


with Timer() as t:
    sleep(4)

print(t())
