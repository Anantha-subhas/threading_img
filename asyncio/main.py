import time
import asyncio


async def brewCoffee():
    print("start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCoffee()")
    return "coffee ready"


async def toastBagel():
    print("start toastBagel")
    await asyncio.sleep(2)
    print("end toastBagel()")
    return "bagel toasted"


async def main():
    start_time = time.time()
    # batch of co-routines
    batch = asyncio.gather(brewCoffee(), toastBagel())  # co-routine objects

    result_coffee, result_bagel = await batch

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"result of brewCoffee: {result_coffee}")
    print(f"result of toastBagel: {result_bagel}")
    print(f"total execution time: {elapsed_time:.2f}")


if __name__ == "__main__":
    asyncio.run(main())
