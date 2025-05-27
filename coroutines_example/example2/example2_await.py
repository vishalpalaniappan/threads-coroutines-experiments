import asyncio
from functools import wraps
import contextvars
import uuid

coroutine_id = contextvars.ContextVar("coroutine_id", default=None) 

def track_coroutine(fn):
    @wraps(fn)
    async def wrapper(*args, **kwargs):
        token = None
        if coroutine_id.get() is None:
            uid = str(uuid.uuid4())
            token = coroutine_id.set(uid)
        try:
            return await fn(*args, **kwargs)
        finally:
            if token:
                coroutine_id.reset(token)
    return wrapper


@track_coroutine
async def test(value):
    print(f"{value} Call Chain Function: {coroutine_id.get()}")

@track_coroutine
async def my_coroutine(name, delay):
    print(f"{name} Coroutine: {coroutine_id.get()}")
    await asyncio.sleep(delay)
    await test(name)
    print(f"Finished {name} after {delay} seconds")

async def main():
    await asyncio.create_task(my_coroutine("Task 1", 3))
    await asyncio.create_task(my_coroutine("Task 2", 1))
    await asyncio.create_task(my_coroutine("Task 3", 2))
    print("All tasks completed.")

asyncio.run(main())