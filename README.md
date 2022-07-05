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

## Libraries

##AsyncIO
```
asyncio is a library to write concurrent code using the async/await syntax.

asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level structured network code.
```

[AsyncIO](https://docs.python.org/3/library/asyncio.html)




##AIOHTTP

```
Asynchronous HTTP Client/Server for asyncio and Python.
```

[AIOHHTP](https://docs.aiohttp.org/en/stable/)

## Pandas

```
pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
```
[Pandas](https://pandas.pydata.org/)

## Json

```
JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired by JavaScript object literal syntax (although it is not a strict subset of JavaScript 1 ).
```
[Json](https://docs.python.org/3/library/json.html)

## Run proyect
Challenge output files are being saved in files directory

Create your virtual environment
```
$ python3 -m venv .venv
```

Activate VirtualEnv (Linux, Mac)
```
$ source .venv/bin/activate
```

Install requirements

```
$ pip install -r requirements.txt
```

Run tests

```
$ python -m unittest
```