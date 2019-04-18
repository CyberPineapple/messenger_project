import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        resp = await session.get('http://localhost:8080/')
        assert 400 == resp.status

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
