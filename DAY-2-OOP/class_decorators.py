def my_class_decorator(cls):
    cls.extra_param = 'extra parameter'
    return cls


def valid_int_number(attr_name, minimum, maximum):
    def inner(cls):
        name = f'_{attr_name}'

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            if not isinstance(value, int):
                raise TypeError('Value must be an integer.')
            if not isinstance(minimum, int) or not isinstance(maximum, int):
                raise TypeError('Minimum and Maximum must be an integer.')
            if value not in range(minimum, maximum + 1):
                raise ValueError(f'Value must be in range ({minimum}, {maximum}).')
            setattr(self, name, value)

        # add getters and setters to the class
        setattr(cls, attr_name, DataDescriptor(getter, setter))

        return cls

    return inner


class DataDescriptor:
    def __init__(self, getter, setter):
        self.setter = setter
        self.getter = getter

    def __set__(self, instance, value):
        return self.setter(instance, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.getter(instance)


# @my_class_decorator
@valid_int_number('a', minimum=1, maximum=30)
@valid_int_number('b', minimum=1, maximum=30)
@valid_int_number('c', minimum=1, maximum=30)
@valid_int_number('d', minimum=1, maximum=30)
@valid_int_number('e', minimum=1, maximum=30)
class MyClass:
    def __init__(self, a: int, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e


m = MyClass(1, 2, 3, 4, 5)
print(dir(m), '\n', vars(MyClass))
print('\n ', m.a, m.b)


class A:
    x = 2

    def __init__(self, new_x=None):
        type(self).x = new_x  # instead of A.x because if class is inherited


a = A(3)
a.x = 4
print(A.x)
