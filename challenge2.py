import asyncio
import aiohttp
import json


uri = "https://jsonplaceholder.typicode.com/todos/{}"
todo_ids = list(range(1, 51))


def write_json_file(json_data):
    """
    should save json data into a json file
    """
    with open('files/json-data.json', 'a') as file:
        file.write(json.dumps(json_data))


async def get_todos(session, url):
    async with session.get(url) as resp:
        data = await resp.json()
        return data


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        todo_list = []
        for id in todo_ids:
            url = f"https://jsonplaceholder.typicode.com/todos/{id}"
            tasks.append(asyncio.ensure_future(get_todos(session, url)))
            await asyncio.sleep(0.01) #We are adding a delay to avoid unclosed ports warning in testing.
                                    ## previous line to increase performance
        todos_list = await asyncio.gather(*tasks)
        for todo in todos_list:
            todo_list.append(todo)
        write_json_file(json.dumps(todos_list))

    return todo_list


asyncio.run(main())
## time spent for all requests --- 0.23920941352844238 seconds ---
