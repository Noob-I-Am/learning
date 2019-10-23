"""
多线程
"""

# python3线程 常用模块 有 _thread 和 threading
import time, threading, _thread


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s: %s' % (threadName, time.ctime(time.time())))

# 使用_thread
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2,))
#     _thread.start_new_thread(print_time("Thread-2", 4,))
# except:
#     print_time('Error occured')




def loop():
    print('thread %s is running... ' % threading.currentThread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


## 使用 threading

# print('thread %s is running... ' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended. ' % threading.current_thread().name)


# 自定义Thread类

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
