import threading
import queue
import time
import random

class Thread1(threading.Thread):
    def __init__(self, id, queue):
        super().__init__(daemon=True)
        self.id = id
        self.queue = queue
        self.start()

    def __del__(self):
        print("Closed Thread", self.id)

    def run(self):
        for i in range(5):
            time.sleep(random.uniform(0.5, 1.5))
            self.queue.put(f"Thread {self.id} - message {i}")
        self.queue.put(f"Thread {self.id} - DONE")