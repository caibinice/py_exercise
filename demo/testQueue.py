import threading
import time
from queue import Queue


#  传入线程id，保证计算顺序
def job(l, q, id):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put((id, l))


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q, i))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    results.sort(key=lambda x: x[0])
    results = [r[1] for r in results]
    print(results)


if __name__ == '__main__':
    multithreading()
