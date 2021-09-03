import math
from abc import ABC, abstractmethod


class FigureAbc(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @staticmethod
    @abstractmethod
    def show_number():
        pass


class Circle(FigureAbc):
    def circumference(self):
        return 2 * math.pi * self.r

    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Rectangular(FigureAbc):
    @staticmethod
    def show_number():
        return 42

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def circumference(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __init__(self, a, b):
        self.a = a
        self.b = b


class Square(Rectangular):
    pass


class Triangle(FigureAbc):
    def circumference(self):
        return self.a + self.b + self.c

    # h = 1
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # Triangle.increase_h()

    # @classmethod
    # def increase_h(cls):
    #     cls.h += 1

    def area(self):
        # return self.a * Triangle.h / 2
        return self.a * self.b / 2


# class TriangleRectangle(Triangle):
#     def __init__(self, a, b, c, h):
#         super().__init__(a, b, c)  # Bad example! Class field h will be increased!
#         self.h = h  # Rewrites class field h!


# t = Triangle(3, 4, 5)
# c = Circle(4)
r = Rectangular(3, 4)
r.name = 'Rect'
print(r.area(), r.name)
# for n in [t, c, r]:
#     print(n.area())
