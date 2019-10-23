"""
烫手的山芋: 约瑟夫环 , 数到第num个
"""

from data_structure.Queue import Queue

def hotPotato(nameList, num):
    queue = Queue()
    for name in nameList:
        queue.enqueue(name)
    while queue.size() > 1:
        for i in range(1, num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()



print(hotPotato(['sam', 'shell', 'bob'],2))

