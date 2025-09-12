import asyncio
import httpx

async def fetch(url, client):
    response = await client.get(url)
    return url, response.text

async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        res = {}
        for url in urls:
            fetched_url, content = await fetch(url, client)
            res[fetched_url] = content
        
        return res

