# range() takes no keyword arguments
# for item in range(start=1, stop=5):
#     print(item)

import operator


def my_range(start, stop=None, step=1, /):
    start_temp = 0 if stop is None else start
    stop_temp = start if stop is None else stop

    if step == 0:
        raise ValueError('Invalid step')

    if stop_temp > start_temp and step < 0:
        return

    op = operator.gt if step < 0 else operator.lt

    while op(start_temp, stop_temp):
        yield start_temp
        start_temp += step

    # while (stop_temp - start_temp) * step > 0:
    #     yield start_temp
    #     start_temp += step


for item in my_range(10, 5, -2):
    print(item)
