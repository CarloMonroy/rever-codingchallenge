import unittest
from challenge1 import get_orders_summary


class MyTestCase(unittest.TestCase):
    def test_challenge1(self):
        accounts_list = ["u2", "u3"]
        test_case1 = {
            'u2': {'total_orders': 4,
                   'completed_orders': 2,
                   'pending_orders': 2
                   },
            'u3': {'total_orders': 7,
                   'completed_orders': 5,
                   'pending_orders': 2
                   }
        }

        self.assertDictEqual(get_orders_summary(accounts_list), test_case1)


if __name__ == '__main__':
    unittest.main()
