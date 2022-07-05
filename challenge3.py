import pandas as pd
import json


def process_file():
    """
    Read data from the cvs file files/employee_data.csv and do the following:
    1. Clean the data as best you can
    2. calculate the mean of the annual salaries, calculate the max and minimum of the annual salaries
    3. calculate the most common employment_status

    BONUS: save the clean data as a VALID JSON file
    """
    df = pd.read_csv('files/employee_data.csv')
    new_df = df.drop(["tax_file_no"], axis=1) ##Removing tax_file_no, its always empty
    new_df.dropna(axis=0, how='all', inplace=True) #Removing empty rows
    new_df["is_married"] = new_df["is_married"].where(new_df["is_married"].str.isalpha()) ##removing wrong values in is_married

    ## Saving cleaned data in jsonfile
    json_result = new_df.to_json(orient='split')
    with open('files/employee_data.json', 'w') as document:
        document.write(json_result)

    ## Calculate mean of the annual salaries, max and minimum salaries
    calc_df = new_df["annual_salary"].describe()
    print(f"The mean of salary is : {calc_df['mean']}")
    print(f"Max salary is {calc_df['max']}")
    print(f"Min salary is {calc_df['min']}")

    ## Calculate most common employment_status
    print(f"Most common employment status: {new_df['employment_status'].mode()}")



process_file()