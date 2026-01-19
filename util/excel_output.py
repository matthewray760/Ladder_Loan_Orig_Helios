import pandas as pd
import numpy as np
import openpyxl
import xlsxwriter


def to_excel(bulk_trades, other_income, stub_interest,cash_transfers,filename):

    sheets = {
        'Bulk Trades': bulk_trades,
        'OI': other_income,
        'Stub Interest': stub_interest,
        'Cash Transfers': cash_transfers
    }

    pathway_output = fr'C:\Users\matthewray\OneDrive - Clearwater\Desktop\Ladder\Python\Loan_Orig_Helios\outputs\{filename}_output.xlsx'


    with pd.ExcelWriter(engine='openpyxl',path=pathway_output) as writer:
        for sheet_name,df in sheets.items():
            df.to_excel(writer,sheet_name= sheet_name,index=False)

            for sheet_name in writer.sheets:
                worksheet = writer.sheets[sheet_name]
            for column_cells in worksheet.columns:
                max_length = 0
                column = column_cells[0].column_letter
                for cell in column_cells:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except:
                        pass
                adjusted_width = (max_length + 6)
                worksheet.column_dimensions[column].width = adjusted_width
