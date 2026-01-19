import pandas as pd

def data_intake(filename):

    df = pd.read_excel(fr'C:\Users\matthewray\OneDrive - Clearwater\Desktop\Ladder\Python\Loan_Orig_Helios\inputs\{filename}.xlsx',header=1)

    return df


