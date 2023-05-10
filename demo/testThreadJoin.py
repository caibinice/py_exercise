import threading
import time


def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)  # 任务间隔0.1s
    print("T1 finish\n")


# added_thread = threading.Thread(target=thread_job, name='T1')
# # added_thread.start()
# # print("all done\n")
#
# added_thread.start()
# added_thread.join()
# print("all done\n")

def T1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")


def T2_job():
    print("T2 start\n")
    print("T2 finish\n")


thread_1 = threading.Thread(target=T1_job, name='T1')
thread_2 = threading.Thread(target=T2_job, name='T2')
#  V型排布，耗时长的线程先执行，最后join
thread_1.start()  # start T1
thread_2.start()  # start T2
thread_2.join()  # join for T2
thread_1.join()  # join for T1
print("all done\n")
