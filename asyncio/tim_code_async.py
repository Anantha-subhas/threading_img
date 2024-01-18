import asyncio
import time
"""
Async Event-Loop 
is a design pattern that waits for and dispatches events or message in a program
"""
async def main():
    start_time = time.time()
    print("tim")
    # await foo("subhas")#co-routine
    #          (or)
    task = asyncio.create_task(foo("subhas"))
    task2 = asyncio.create_task(foo2("subhas"))
    await task #goes to foo() then it executes the followings
    await task2
    await asyncio.sleep(1)
    print("middle")
    end_time = time.time()
    print(f"finished: {end_time - start_time:.2f}")

async def foo(text):
    print(text)
    await asyncio.sleep(5)
    print("co-routine1 End")
async def foo2(text):
    print(text)
    await asyncio.sleep(5)
    print("co-routine2 End")
asyncio.run(main())