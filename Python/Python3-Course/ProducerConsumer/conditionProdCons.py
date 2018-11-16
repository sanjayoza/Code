from threading import Thread, Condition, Lock
import threading
from MyBuffer import MyBuffer
from random import randint
from time import sleep

NUM_LOOPS = 5
buff = None

condition = Condition()


def producer():
    # Logic is:
    #   1. acquire the condition
    #   2. produce the item
    #   3. notify the consumer of availability
    #   4. release the condition
    for i in range(NUM_LOOPS):
        sleep(2)
        lock.acquire()
        condition.acquire()    # acquire the condition
        value = randint(1, 100)
        buff.insertBuffer(value)
        lock.release()
        condition.notify()     # notify consumer
        condition.release()    # release the condition


def consumer():
    # Logic is:
    #   1. acquire condition
    #   2. wait until condition is available for consumption
    #   3. consume the item
    #   4. release the condition
    
    for i in range(NUM_LOOPS):
        sleep(2)
        condition.acquire()
        condition.wait()      # blocks until condition available
        buff.removeBuffer()
        condition.release()
        

def startThreads():
    prodT = []
    consT = []
    for i in range(NUM_LOOPS):
        t = Thread(target = producer)
        c = Thread(target = consumer)
        prodT.append(t)
        consT.append(c)
        t.start()
        c.start()
    
    sleep(5)
    for i in range(NUM_LOOPS):
        prodT[i].join()
        consT[i].join()

buff = MyBuffer(10)
buff.insertBuffer(10)
startThreads()
