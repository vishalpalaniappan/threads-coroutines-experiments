import asyncio
import threading

def test():
    task = asyncio.current_task()
    print("TESTING:", task.get_name())

async def task1():
    task = asyncio.current_task()
    print(f"Starting task {asyncio.current_task().get_name()}")
    test()
    await asyncio.sleep(3)
    print(f"Finished task {asyncio.current_task().get_name()}")
    test()

async def task2():
    print(f"Starting task {asyncio.current_task().get_name()}")
    test()
    await asyncio.sleep(2)
    print(f"Finished task {asyncio.current_task().get_name()}")
    test()

async def task3():
    print(f"Starting task {asyncio.current_task().get_name()}")
    test()
    await asyncio.sleep(7)
    print(f"Finished task {asyncio.current_task().get_name()}")
    test()

async def main():
    await asyncio.gather(task1(), task2(), task3())
    
    b = 2


def asdf():
    asyncio.run(main())

asdf()

print('asdf')