import pandas as pd
from di_and_norm.data_intake import data_intake
from di_and_norm.normalization import data_norm
from bulk_entry.trade_tran import generate_trade_tran
from bulk_entry.cash_entry import generate_cash_entry
from bulk_entry.cash_transfer import create_cash_tran
from util.excel_output import to_excel


to_excel_flag = True

filename = 'Copy of LADR_Mod_SMF 20260115 - 6xGainesville Arba'




def run_pipeline():
    raw_data = data_intake(filename)
    norm_data = data_norm(raw_data)
    bulk_trades = generate_trade_tran(norm_data)
    stub_interest,other_income = generate_cash_entry(norm_data)
    cash_transfers = create_cash_tran(bulk_trades,other_income,stub_interest)



    if to_excel_flag == True:
        to_excel(bulk_trades,other_income,stub_interest,cash_transfers,filename)
    else:
        print("to_excel set to False")



    return




if __name__ == '__main__':
    run_pipeline()



#other_income.to_excel(fr'C:\Users\matthewray\OneDrive - Clearwater\Desktop\Ladder\Python\Loan_Orig_Helios\outputs\test.xlsx')
