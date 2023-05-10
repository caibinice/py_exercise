import multiprocessing as mp
import threading as td


# def job(a, d):
#     for _ in range(20):
#         print(a, d)
#
#
# if __name__ == '__main__':
#     t1 = mp.Process(target=job, args=(1, 2))
#     p1 = mp.Process(target=job, args=(3, 4))
#     t1.start()
#     p1.start()
#     t1.join()
#     p1.join()


def job(q, id):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)  # queue
    print("pid:", id)


if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q, 1))
    p2 = mp.Process(target=job, args=(q, 2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)
