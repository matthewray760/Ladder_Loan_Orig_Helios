from datetime import datetime, timedelta, date
import pandas as pd

def get_first_day_of_next_month(input_date):
    if isinstance(input_date, str):
        # Parse the input date from a string
        date_obj = datetime.strptime(input_date, '%Y-%m-%d').date()
    elif isinstance(input_date, date):
        # If input is already a date object, use it directly
        date_obj = input_date
    else:
        raise ValueError("Input must be a string in 'YYYY-MM-DD' format or a datetime.date object.")
    
    if date_obj.month == 12:  # If December, go to January of the next year
        next_month = 1
        next_year = date_obj.year + 1
    else:
        next_month = date_obj.month + 1
        next_year = date_obj.year

    # Create the first day of the next month
    return date(next_year, next_month, 1)




def calculate_entry_date(row):
    if row['Stub_Month'] == 'first_month_stub':
        return row['IssueDate'] + pd.DateOffset(days=1)  # or another date of your choosing
    else:
        return get_first_day_of_next_month(row['IssueDate'])
    


def calculate_settle_date(row):
    if row['Stub_Month'] == 'second_month_stub':
        return row['Entry Date'] + pd.DateOffset(days=5)
    else:
        return row['IssueDate']
