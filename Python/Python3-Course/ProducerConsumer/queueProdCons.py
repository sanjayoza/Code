import threading
from queue import Queue
from random import randint
from time import sleep

# instead of using condition or semaphore use queue for the buffer.

QSIZE = 10
NUM_THREADS = 3

def producer(queue):
    count = 0
    while True:
        sleep(1)
        value = randint(1, 100)
        print("Producer: {}" .format(value))
        queue.put(value)
        count += 1
        if count > 5:
            print("Count greater than 5")
            break
    

def consumer(queue):
    while True:
        sleep(2)
        value = queue.get()
        print("Consumer: {}" .format(value))
        if queue.empty():
            print("Queue is empty")
            break


def startThreads():
    queue = Queue(QSIZE)
    threads = []
    for i in range(NUM_THREADS):
        threads.append(threading.Thread(target=consumer, args=[queue]))
        threads.append(threading.Thread(target=producer, args=[queue]))
    
    for thread in threads:
        thread.start()
        
    sleep(2)
    
    for thead in threads:
        thread.join()
    

startThreads()