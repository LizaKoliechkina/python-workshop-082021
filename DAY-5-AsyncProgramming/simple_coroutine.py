import asyncio


async def do_first():
    print('Do 1 25%')
    await asyncio.sleep(1)
    print('Do 1 50%')
    await asyncio.sleep(1)
    print('Do 1 75%')
    await asyncio.sleep(1)  # if 0.9 then 'Do 1 100%' will print before 'Do 2 100%'
    print('Do 1 100%')


async def do_second():
    print('Do 2 50%')
    await asyncio.sleep(3)
    print('Do 2 100%')


def do_other():
    print('Do the rest')


async def main():
    await asyncio.gather(do_first(), do_second())  # do_first() - calling function, Future object is returned
    # immediately so we do not wait till the end of func but after first line (async def ...) go further

if __name__ == '__main__':
    asyncio.run(main())
    do_other()
