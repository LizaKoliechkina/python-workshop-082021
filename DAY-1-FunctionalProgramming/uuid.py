def generate_uuid():
    idx = 0

    def inner():
        nonlocal idx  # search not in local scope
        result = idx + 1  # RHS
        idx += 1  # LHS
        return result

    return inner


# uuid = generate_uuid()
# print(uuid())
# print(uuid())
# print(uuid())


def generate_uuid_2():
    idx = 0
    while True:
        yield idx
        idx += 1


uuid = generate_uuid_2()
print(next(uuid))
print(next(uuid))
print(next(uuid))


def tmp_gen():
    if False:
        yield 8
    return 'Elo'


tmp = tmp_gen()
print(next(tmp))

print(list((x ** 2 for x in range(1000))))
