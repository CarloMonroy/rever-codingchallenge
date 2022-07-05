import data
import pandas as pd

accounts_list = ["u2", "u3"]

def get_orders_summary(accounts):
    """
    Given a list of accounts and using the information in data module,
    return a dictionary where each key is an account and its value is 
    a dictionary with the accounts total orders, completed orders and pending orders
    example:
    given ["u2"]
    {
      'u2': {
        'total_orders': 5,
        'completed_orders': 3,
        'pending_orders': 2
      }
    }

    Step 2: add unit test for this function

    BONUS: create an CSV file with the summary, this can be done as a different function
    This can be done with external libraries
    """

    orders_summary = {}
    all_orders = data.orders
    account_orders = data.account_orders

    for user_account in accounts:
        total_orders = 0
        completed_orders = 0
        pending_orders = 0
        for user_order in account_orders[user_account]:
            total_orders += 1
            if all_orders[int(user_order)-1]["status"] == "pending" :
                pending_orders += 1

            if all_orders[int(user_order)-1]["status"]== "completed":
                completed_orders += 1

        orders_summary[user_account] = {
            'total_orders': total_orders,
            'completed_orders': completed_orders,
            'pending_orders': pending_orders
        }

    return orders_summary

def orders_summary_to_csv(order_summary):
    """
    Takes a dict and it creates a csv file callse order_summary.csv
    """
    df = pd.DataFrame.from_dict(order_summary)
    df.to_csv ('order_summary.csv')


summary = get_orders_summary(accounts_list)
orders_summary_to_csv(summary)
print(summary)