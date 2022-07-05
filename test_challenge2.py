import asyncio
import unittest
from challenge2 import main


class AsyncTest(unittest.TestCase):
    def test_get_todos(self):
        """
        This test will print unclosed transport warnings. however in challenge2.py im using
        with keyword to make sure that we close all connections.
        we can add a sleep time to not show this warnings but that will slow down or code
        """
        test_cases = [ #We can change this test cases with objects from our todolist
            {"userId": 3, "id": 44, "title": "cum debitis quis accusamus doloremque ipsa natus sapiente omnis",
             "completed": True
             },
            {
                "userId": 3,
                "id": 48,
                "title": "sit reprehenderit omnis quia",
                "completed": False
            },
            {
                "userId": 3,
                "id": 49,
                "title": "ut necessitatibus aut maiores debitis officia blanditiis velit et",
                "completed": False
            }
        ]


        loop = asyncio.new_event_loop() #we create an event loop to use our async functions
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(main())
        loop.close()

        for order in test_cases:
            order_number = order['id']-1
            self.assertDictEqual(order, result[order_number]) #We verify that we are fetching the correct data



if __name__ == '__main__':
    unittest.main()
