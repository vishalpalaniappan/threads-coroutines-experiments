import threading
import queue
import time
import random
def testFunc():
    print("test function thread 2")
    a = 1

class Thread2(threading.Thread):
    def __init__(self, id, queue):
        super().__init__(daemon=True)
        self.id = id
        self.queue = queue
        self.start()

    def __del__(self):
        print("Closed Thread", self.id)

    def run(self):
        print("THREAD2:", threading.get_ident())
        for i in range(5):
            time.sleep(random.uniform(0.5, 1.5))
            testFunc()
            self.queue.put(f"Thread {self.id} - message {i}")
        self.queue.put(f"Thread {self.id} - DONE")