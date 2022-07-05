import asyncio
import unittest
from challenge2 import main
import random


class AsyncTest(unittest.TestCase):
    def test_get_todos(self):
        test_cases = [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False},
                      {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False},
                      {'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}]


        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(main())
        loop.close()
        random_entry = random.randint(0, len(test_cases)-1)
        self.assertDictEqual(test_cases[random_entry], result[random_entry] )





if __name__ == '__main__':
    unittest.main()
