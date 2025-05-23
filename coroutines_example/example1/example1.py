import asyncio

async def task1():
    print("Starting task 1")
    await asyncio.sleep(3)
    print("Finished task 1")

async def task2():
    print("Starting task 2")
    await asyncio.sleep(2)
    print("Finished task 2")

async def task3():
    print("Starting task 3")
    await asyncio.sleep(7)
    print("Finished task 3")

async def main():
    await asyncio.gather(task1(), task2(), task3())

asyncio.run(main())