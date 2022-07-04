## Welcome!

The purpose of this exercise is to evaluate your familiarity with python, how you handle tests and your thought process during problem solving. Make sure to ask any questions you have.

Take some time to familiarize yourself with this project. To finish this exercise you need to complete the most challenges you can, these are challenge1.py, challenge2.py and challenge3.py.

You should be provided with a virtual python environment (virtualenv)

Here is a description of what each function should do. Make sure you put your best effort in writing clean and readable code.


## What we expect:
 - All 3 challenges should be running properly
 - Each challenge has a bonus, completing them will be a big plus
 - Testing is very important for use so please add unit testing to the challenges.


## Challenge 1: Aggregate and process orders into a summary

Given a list of accounts and using the information in data module, return a dictionary where each key is an account and its value is dictionary with the accounts total orders, completed orders and pending orders
example:
given ["u2"]

```
{
  'u2': {
    'total_orders': 5,
    'completed_orders': 3,
    'pending_orders': 2
  }
}
```

After the function is completed make units tests for the function.

As a bonus the you can also save the summary as a .cvs

## Challenge 2: Consume API

For this challenge you will consume an API to fetch todos individually

Given a list of todo ids,  fetch each todo and return a list of todos
Example of a request: https://jsonplaceholder.typicode.com/todos/1

Improve the performance of the above function afterwards if have not done yet.


## Challenge 3: Clean and save data

Take a look at files/employee_data.csv

In this challenge you need to read the csv file and perform the following:
1. Clean the data as best as you can
2. Calculate the mean of the annual salaries, calculate the max and minimum of the annual salaries
3. Calculate the most common employment_status and most common married status


As a bonus you need save the clean data as a VALID JSON file.

Remember that you can use any library