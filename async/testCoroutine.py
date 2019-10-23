
"""
测试协程
"""


import asyncio


async def smart_fib(n):
    print('smart begin')
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = 3
        await asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('back to smart')
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1
    print('smart ended')

@asyncio.coroutine
def stupid_fib(n):
    print('stupid begin')
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = 1
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('back to stupid')
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1
    print('stupid ended')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        smart_fib(10),
        stupid_fib(10),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()