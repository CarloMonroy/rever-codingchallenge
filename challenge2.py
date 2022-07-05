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
    todo_list = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for id in todo_ids:
            url = f"https://jsonplaceholder.typicode.com/todos/{id}"
            tasks.append(asyncio.ensure_future(get_todos(session, url)))
        todos_list = await asyncio.gather(*tasks)
        for todo in todos_list:
            write_json_file(todo)
            todo_list.append(todo)
    return todo_list


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

## time spent for all requests --- 0.23920941352844238 seconds ---
