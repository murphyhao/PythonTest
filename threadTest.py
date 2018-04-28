#coding:utf-8
import threading
import time


g_lock = threading.RLock()
g_nCnt = 0


####################################
# By func
def MethodByFunc():
    for i in range(10):
        t = threading.Thread(target=ThreadFunc, args=(i,))
        t.start()
        t.join()
    print('Main thread end!')

def ThreadFunc(arg):
    g_lock.acquire()
    global g_nCnt
    time.sleep(1)
    g_nCnt += 1
    print(g_nCnt)
    g_lock.release()
####################################


####################################
# By class
def MethodByClass():
    h1 = CMyThread("first", 1)
    h2 = CMyThread("second", 1)
    h3 = CMyThread("third", 1)

    h1.start()
    h2.start()
    h3.start()

    h1.join()
    h2.join()
    h3.join()

    print("Main thread end!")

class CMyThread(threading.Thread):
    def __init__(self, strName, nSleep):
        #super(CMyThread, self).__init__()
        threading.Thread.__init__(self)
        self.m_name = str(strName)
        self.n_nSleep = int(nSleep)

    def run(self):
        while True:
            g_lock.acquire()
            global g_nCnt
            g_nCnt += 1
            strNow = time.strftime("%H:%M:%S")
            print("%s name:%s count:%d" % (strNow, self.m_name, g_nCnt))
            time.sleep(self.n_nSleep)
            g_lock.release()
####################################


if __name__ == '__main__':
    if True:
        MethodByFunc()
    else:
        MethodByClass()