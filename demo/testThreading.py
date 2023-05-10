import threading




def thread_job():
    print('This is a thread of %s' % threading.current_thread())
    print("enumerate in job:" + str(threading.enumerate()))


def main():
    thread = threading.Thread(target=thread_job, )  # 定义线程
    thread.start()  # 让线程开始工作


if __name__ == '__main__':
    main()
    print("count:" + str(threading.active_count()))

    print("enumerate in main:" + str(threading.enumerate()))

    print('This is a thread of %s' % threading.current_thread())

