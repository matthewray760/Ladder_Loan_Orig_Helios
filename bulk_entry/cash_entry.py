import pandas as pd

from util.functions import get_first_day_of_next_month, calculate_entry_date, calculate_settle_date

def generate_cash_entry(norm_data):
    df = norm_data

    # Remove irrelevant columns and Expense Types
    df.drop(columns = 'OriginalPrincipalAmount', inplace = True)
    df = df[df['Expense_Type'] != 'Origination Fee']
    df = df[df['Amount'] != 0]


    ######## Seprate OI from Stub Interest

    ### Stub interest

    stub_int = df.copy()
    stub_int = stub_int[stub_int['Expense_Type'] == 'Prepaid Interest at Next Month End']

    stub_int['first_month_stub'] = df['Stub Interest'] - df['Amount']
    stub_int['second_month_stub'] = df['Amount']

    stub_int = stub_int.melt(id_vars=['Identifier','IssueDate','CW Account Number'], value_vars=['first_month_stub','second_month_stub'], var_name='Stub_Month', value_name='Stub_amount')

    #Create columns
    stub_int['Transaction Type'] = 'CPN'
    stub_int['Currency'] = 'USD'


    stub_int['Entry Date'] = stub_int.apply(calculate_entry_date, axis=1)
    
    
    stub_int['Settle Date'] = stub_int.apply(calculate_settle_date, axis=1)
    stub_int['Post Date'] = stub_int['IssueDate']

    stub_int['Settle Date'] = pd.to_datetime(stub_int['Settle Date']).dt.date
    stub_int['Post Date'] = pd.to_datetime(stub_int['Post Date']).dt.date
    stub_int['Entry Date'] = pd.to_datetime(stub_int['Entry Date']).dt.date


    #rename columns

    stub_int.rename(columns = {
        'Identifier': 'Asset ID',
        'CW Account Number': 'Account ID',
        'Stub_amount': 'Amount'
    }, inplace=True)

    stub_int = stub_int[['Account ID','Transaction Type','Entry Date','Settle Date','Post Date','Asset ID','Currency','Amount']]


    ### OI

    other_income = df.copy()

    other_income = other_income[other_income['Expense_Type'] != 'Prepaid Interest at Next Month End']

    other_income['Entry Date'] = other_income['IssueDate'] + pd.DateOffset(days=1)
    other_income['Settle Date'] = other_income['IssueDate']
    other_income['Post Date'] = other_income['IssueDate']
    other_income['Transaction Type'] = 'INC'
    other_income['Currency'] = 'USD'

    other_income.rename(columns = {
        'Identifier': 'Asset ID',
        'CW Account Number': 'Account ID'
    }, inplace=True)

    other_income['Entry Date'] = pd.to_datetime(other_income['Entry Date']).dt.date

    other_income = other_income[['Account ID','Transaction Type','Entry Date','Settle Date','Post Date','Asset ID', 'Currency','Amount']]


    return stub_int, other_income
