import threading
import queue
import time
import random
import asyncio


def testFunc():
    print("test function thread 3")
    a = 1

class Thread3(threading.Thread):
    def __init__(self, id, queue):
        super().__init__(daemon=True)
        self.id = id
        self.queue = queue
        self.start()

    def __del__(self):
        print("Closed Thread", self.id)

    def test(self):
        task = asyncio.current_task()
        print("TESTING:", task.get_name())

    async def task1(self):
        task = asyncio.current_task()
        print(f"Starting task {asyncio.current_task().get_name()}")
        self.test()
        await asyncio.sleep(3)
        print(f"Finished task {asyncio.current_task().get_name()}")
        i = "Task 1 finished"
        self.queue.put(f"Thread {self.id} - message {i}")
        self.test()

    async def task2(self):
        print(f"Starting task {asyncio.current_task().get_name()}")
        self.test()
        await asyncio.sleep(2)
        print(f"Finished task {asyncio.current_task().get_name()}")
        i = "Task 2 finished"
        self.queue.put(f"Thread {self.id} - message {i}")
        self.test()

    async def task3(self):
        print(f"Starting task {asyncio.current_task().get_name()}")
        self.test()
        await asyncio.sleep(7)
        print(f"Finished task {asyncio.current_task().get_name()}")
        i = "Task 3 finished"
        self.queue.put(f"Thread {self.id} - message {i}")
        self.test()

    async def main(self):
        await asyncio.gather(self.task1(), self.task2(), self.task3())        

    def run(self):
        print("THREAD2:", threading.get_ident())
        for i in range(5):
            time.sleep(random.uniform(0.5, 1.5))
            testFunc()
            self.queue.put(f"Thread {self.id} - message {i}")
        self.queue.put(f"Thread {self.id} - DONE")