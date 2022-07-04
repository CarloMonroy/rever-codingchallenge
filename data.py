# Order details
orders = [
  { "order_id": "1", "status": "pending"},
  { "order_id": "2", "status": "pending"},
  { "order_id": "3", "status": "completed"},
  { "order_id": "4", "status": "pending"},
  { "order_id": "5", "status": "completed"},
  { "order_id": "6", "status": "completed"},
  { "order_id": "7", "status": "pending"},
  { "order_id": "8", "status": "completed"},
  { "order_id": "9", "status": "pending"},
  { "order_id": "10", "status": "completed"},
  { "order_id": "11", "status": "completed"},
  { "order_id": "12", "status": "completed"},
  { "order_id": "13", "status": "completed"},
  { "order_id": "14", "status": "pending"},
  { "order_id": "15", "status": "completed"},
  { "order_id": "16", "status": "pending"},
  { "order_id": "17", "status": "completed"},
]


'''
Accounts dictionary, where each key is an account id and its value is
set of the orders each account has made
'''
account_orders = {
  "u1": { "1", "2", "4", "5" },
  "u2": { "7", "9", "10", "11" },
  "u3": { "6", "8", "12", "13", "14", "16", "17" },
}

