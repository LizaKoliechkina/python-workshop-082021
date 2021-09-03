def upper(fn, name: str):
    return fn(name.title())


# Decorator: first argument is a function fn, inner/second argument is a set of arguments for processed function
def upper_2(fn):
    def inner(name: str):
        return fn(name.title())

    return inner


def provide_name(fn):
    def inner():
        data = 'Liza'
        return fn(data)
    return inner


# @upper_2
@provide_name
def get_name(name):
    return f'Hello, {name}'


@upper_2
def get_nick(nick):
    return f'Hello, {nick}'


# print(upper(get_name, 'ala'))
# print(get_nick('ala'))

print(get_name())
# print(get_name('ala'))
