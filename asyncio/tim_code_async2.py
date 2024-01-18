import asyncio
import time

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {"data": [1, 2, 3, 4]}

async def print_nums():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25) #for each iteration


async def main():
    start = time.time()
    tasks = [fetch_data(),print_nums()]

    batch = asyncio.gather(*tasks)
    task1,task2 = await batch
    end = time.time()
    print(task1)
    print(f"task1 completed in {end - start}")
    # print(task2) it returns None so
    task2
    print(f"task2 completed in {end - start}")

if __name__ == "__main__":
    asyncio.run(main())





