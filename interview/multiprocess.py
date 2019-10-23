"""
多进程
"""

from multiprocessing import Process, Pool
import os, time, random


def run_proc(name):
    print('Run child process %s %s.' % (name, os.getpid()))


# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc('test'))
#     print('Child process will start')
#     p.start()
#     p.join()
#     print('Child process end')


# 启动大量子进程，可以使用进程池创建子进程
def long_time_task(name):
    print('Run task %s (%s) ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))


# if __name__ == '__main__':
#     print('Parent process %s.', os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done')
#     p.close()
#     p.join()
#     print('All subprocesses done')


# 使用子进程

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
