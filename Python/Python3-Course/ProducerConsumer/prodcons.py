import threading
from random import randint
from time import sleep
from MyBuffer import MyBuffer 

BUFF_SIZE = 10
NUM_LOOPS = 10
buf = None
#mutex = threading.Semaphore()
over_flow = threading.BoundedSemaphore(BUFF_SIZE)
#under_flow = threading.BoundedSemaphore(1)
    

        
def producer():
    i = 0
    while i < NUM_LOOPS:
        stime = randint(1, 20)
        sleep(1)
        try:
            over_flow.release()
            value = randint(1, 100)
            buf.insertBuffer(value)
        except:
            print("producer full")
        i += 1

def consumer():
    i = 0
    while i < NUM_LOOPS:
        stime = randint(1, 10)
        sleep(1)
        over_flow.acquire(blocking = False)
        buf.removeBuffer()
        i += 1
            
def startThreads():
    prodT = []
    consT = []
    for i in range(NUM_LOOPS):
        t = threading.Thread(target = producer)
        c = threading.Thread(target = consumer)
        prodT.append(t)
        consT.append(c)
    for i in range(NUM_LOOPS):
        prodT[i].start()
        consT[i].start()
        
    sleep(1)
    for i in range(NUM_LOOPS):
        prodT[i].join()
        consT[i].join()

buf = MyBuffer(10)
for i in range(BUFF_SIZE):
    value = randint(1, 100)
    buf.insertBuffer(value)
print(buf)
startThreads()
