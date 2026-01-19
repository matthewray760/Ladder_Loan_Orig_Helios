import pandas as pd


def data_norm(raw_data):
    df = raw_data

    df['IssueDate'] = pd.to_datetime(df['IssueDate']).dt.date

    ## filter for relevant columns
    df = df[['Identifier','IssueDate','CW Account Number','OriginalPrincipalAmount','Origination Fee','UW Fee','Processing Fee','Broker Fee','Rate Lock Fee', 'Misc Expenses','Prepaid Interest at Next Month End','Stub Interest']]


    # Generate required format. Move columns to rows and consolidate amounts
    df = df.melt(id_vars=['Identifier','IssueDate','CW Account Number','OriginalPrincipalAmount','Stub Interest'], value_vars=df.columns[3:], var_name='Expense_Type', value_name='Amount')


    ## Update Dtypes
    df['OriginalPrincipalAmount'] = pd.to_numeric(df['OriginalPrincipalAmount'])
    df['Stub Interest'] = pd.to_numeric(df['Stub Interest'])
    df['Amount'] = pd.to_numeric(df['Amount'])

    return df
