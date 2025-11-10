import asyncio
from init.prepare_database import init_db


async def main():
    tasks = [
        asyncio.create_task(init_db())
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
