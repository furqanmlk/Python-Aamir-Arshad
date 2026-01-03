import asyncio


async def fetch_user(session, user_id):
    if user_id in cache:
        return cache[user_id]
    resp = await session.get(f'https://api.example.com/users/{user_id}')
    data = await resp.json()
    cache[user_id] = data


async def main(user_ids):
    global cache
    cache = {}
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user(session, uid) for uid in user_ids]
        done, _ = await asyncio.wait(tasks)
    for task in done:
        user = task.result()
        print(user['name'])

if __name__ == '__main__':
    ids = [1, 2, 3]
    asyncio.run(main(ids))
