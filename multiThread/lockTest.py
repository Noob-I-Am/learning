import threading as thread
import time


lock = thread.Lock()
def doSth():
    print(' in doSth func ')

def begin(threadName):
    t1 = time.time()
    print(threadName, '开始获取锁', t1)
    lock.acquire()
    t2 = time.time()
    print(threadName, '获取锁完毕', t2)
    print(threadName, '用时', t2 - t1)

    try:
        doSth()
    finally:
        lock.release()

if __name__ == '__main__':
    myThread1 = thread.Thread(target=begin, args=('myThread',))
    myThread1.start()
    myThread1.join()
    print('main thread ends')