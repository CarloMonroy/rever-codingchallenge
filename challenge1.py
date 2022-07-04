import data

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


    total_orders = 0
    completed = 0
    pending = 0
    orders = data.account_orders

    order.map()

        def count_orders(orders):
          if data.order[]








    orders_summary = {}
    return orders_summary



summary  = get_orders_summary(accounts_list)
print(summary)