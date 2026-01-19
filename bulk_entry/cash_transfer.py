import pandas as pd



def create_cash_tran(bulk_trades,other_income,stub_interest):
    bt = bulk_trades.copy()
    oi = other_income.copy()
    si = stub_interest.copy()

    bt['Amount'] = bt['Price'] * bt['Units'] * .01

    bt = bt[['Account ID','Post Date','Amount']]
    oi = oi[['Account ID','Post Date','Amount']]
    si = si[['Account ID','Post Date','Amount']]


    concat_df = pd.concat([bt,oi,si])

    grouped_df = concat_df.groupby(['Account ID','Post Date'])['Amount'].sum().reset_index()


    grouped_df['Transaction Type'] = 'TRN'
    grouped_df['Entry Date'] = grouped_df['Post Date']
    grouped_df['Settle Date'] = grouped_df['Post Date']
    grouped_df['Currency'] = 'USD'
    grouped_df['Asset ID'] = 'CCYUSD'

    grouped_df = grouped_df[['Account ID','Transaction Type','Entry Date','Settle Date','Post Date','Asset ID','Currency','Amount']]


    return grouped_df
