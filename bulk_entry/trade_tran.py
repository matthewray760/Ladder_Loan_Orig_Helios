import pandas as pd


def generate_trade_tran(norm_data):
    df = norm_data

    df = df[['Identifier','IssueDate','CW Account Number','OriginalPrincipalAmount','Expense_Type','Amount']]

    df = df[df['Expense_Type'] == 'Origination Fee']
    df.rename(columns = {'Amount': 'Origination Fee'}, inplace = True)

    df['Price'] = ((df['OriginalPrincipalAmount'] - df['Origination Fee'])/ df['OriginalPrincipalAmount']) * 100
    df['Transaction Type'] = 'BUY'
    df['Settle Date'] = df['IssueDate']
    df['Post Date'] = df['IssueDate']

    rename_columns = {
        'CW Account Number' : 'Account ID',
        'Identifier': 'Asset ID',
        'IssueDate': 'Entry Date',
        'OriginalPrincipalAmount': 'Units'
    }

    df.rename(columns = rename_columns,inplace=True)

    df = df[['Account ID','Transaction Type','Asset ID','Entry Date', 'Settle Date', 'Post Date', 'Price', 'Units']]



    return df
