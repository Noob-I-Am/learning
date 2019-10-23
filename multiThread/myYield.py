
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from [i for i in range(5)]
    print("Hello again!")

g = hello()

for i in g:
    print(i)