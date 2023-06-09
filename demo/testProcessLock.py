import multiprocessing as mp
import time


#  不加进程锁的情况
# def job(v, num):
#     for _ in range(5):
#         time.sleep(0.1)  # 暂停0.1秒，让输出效果更明显
#         v.value += num  # v.value获取共享变量值
#         print(v.value)
#
#
# def multicore():
#     v = mp.Value('i', 0)  # 定义共享变量
#     p1 = mp.Process(target=job, args=(v, 1))
#     p2 = mp.Process(target=job, args=(v, 3))  # 设定不同的number看如何抢夺内存
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
#
# if __name__ == '__main__':
#     multicore()
#

#  加了进程锁
def job(v, num, l):
    l.acquire()  # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num  # 获取共享内存
        print(v.value)
    l.release()  # 释放


def multicore():
    l = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享内存
    p1 = mp.Process(target=job, args=(v, 1, l))  # 需要将lock传入
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()
