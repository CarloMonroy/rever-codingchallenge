import asyncio
import aiohttp
import json
import time

start_time = time.time()

uri = "https://jsonplaceholder.typicode.com/todos/{}"
todo_ids = list(range(1, 51))


def write_json_file(json_data):
    """
    should save json data into a json file
    """
    with open('json-data.json', 'a') as file:
        file.write(json.dumps(json_data))


async def get_todos(session, url):
    async with session.get(url) as resp:
        data = await resp.json()
        return data


async def main():

    async with aiohttp.ClientSession() as session:
        tasks = []
        for id in todo_ids:
            url = f"https://jsonplaceholder.typicode.com/todos/{id}"
            tasks.append(asyncio.ensure_future(get_todos(session, url)))

        todos_list = await asyncio.gather(*tasks)
        for todo in todos_list:
            write_json_file(todo)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

##write_json_file()
