import threading as thread
import time

semaphore = thread.Semaphore(2)

def func():
    if semaphore.acquire():
        for i in range(2):
            print(thread.current_thread().getName()+' get semaphore')
        time.sleep(5)
        semaphore.release()
        print(thread.current_thread().getName()+' release semaphore')

for i in range(5):
    t1 = thread.Thread(target=func)
    t1.start()