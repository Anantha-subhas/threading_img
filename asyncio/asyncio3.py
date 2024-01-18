import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    # Create a list of tasks
    tasks = [task1(), task2()]

    # Run the tasks concurrently
    await asyncio.gather(*tasks)
    """
     tasks
     (1, 2, 3, 4, 5)
     *tasks 
      1,2,3,4,5
     
    """

if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())
