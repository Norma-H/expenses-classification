#!/usr/bin/python3
import pandas as pd
from pandas import DataFrame, Series
import glob

month = input("Enter month number: ") # when running test file, put a hard coded number (for now test file has '3')
# use the following 'categories' when running test file
# categories = DataFrame({'Description': ['PAYPAL *PROGRESSIVE','VW CREDIT ONLINE PMT','9495 PARKING CORP','ASBURY PARK PASSPORT PAR','COSTCO GAS #0329','NJ EZPASS','GOOGLE *Google Fi','TMOBILE*AAL TEL','TMOBILE*AUTO PAY','Chabad at','ORG FOR RESOL AGUNOT','SEPHARDIC INSTITUTE FOR','SQ *CONGREGATION MAGEN DA','SQ *RACHEL LEAH CHESED FU','NORDSTROM RACK #0650','On Inc','REI.COM','Zara.com/USA','DOORDASH CREDIT','DOORDASH*THE JUICE THE','FALAFEL OFF THE CORNER','ROOK COFFEE LITTLE OOakhurst NJ','GBCI','HUMBLEBUNDLE.COM','REUVEN LERNER','EMBROIDER A GIFT','SP * DIMPLES BABY BROO','WISHING WELL','COSTCO WHSE #0329','LOCAL 130 SEAFOOD Asbury Park NJ','M A KOSHER MEATS INOAKHURST NJ','SP * BURLAP &amp; BARREL','SQ *LOCAL 130 SEAFOOD','STOP &amp; SHOP 2813','WEGMANS OCEAN NJ','HIGH MAINTENANCE','HIGH MAINTENANCE STUOAKHURST NJ',"KIMMY'S NAIL SALON",'COURT LIQUORS','CAPSULE PHARMACY','TDBANK BILL PAY CHECK 995030 Phyliss Tobin','CITIZEN WATCH COMPANY','Amazon web services','GOOGLE*GOOGLE STORAGE','PAYPAL *LINKEDIN','PAYPAL *NY TIMES NYTIMES','PP*APPLE.COM/BILL','Spotify USA','ICHIBAN JAPANESE RESTAU','AUTOMATIC PAYMENT - THANK','Payment Thank You-Mobile','Chabad at Emory','PAYPAL *MODERNMOSAI','BENNY`S BRICK OVEN INC','WEGMANS             OCEAN               NJ','I&D Glatt Ave P     Brooklyn            NY','LOCAL 130 SEAFOOD   Asbury Park         NJ','MOBILE PAYMENT - THANK YOU','COMETEER            GLOUCESTER          MA','ROOK COFFEE LITTLE OOcean Township      NJ','KINGS HIGHWAY GLATT OAKHURST            NJ','SHOPRITE NEPTUNE S1 NEPTUNE             NJ','AUTOPAY PAYMENT - THANK YOU','ROOK COFFEE LITTLE OOakhurst            NJ','RENEWAL MEMBERSHIP FEE','CHASE CREDIT CRD AUTOPAY ','CHASE CREDIT CRD AUTOPAYBUS','AMEX EPAYMENT    ACH PMT ','NYS DOL UI DD    UI DD ','IOD INTEREST PAID ','Online Xfer Transfer to CK x9776','VW CREDIT        ONLINE PMT ','FLATIRON HEALTH  PAYROLL ','CHASE CREDIT CRD EPAY '],
#                        'Classification': ['Car Insurance','Car Insurance','Car Transportation','Car Transportation','Car Transportation','Car Transportation','Cell Phone','Cell Phone','Cell Phone','Charity','Charity','Charity','Charity','Charity','Clothing','Clothing','Clothing','Clothing','Eating Out','Eating Out','Eating Out','Eating Out','Education','Education','Education','Gifts','Gifts','Gifts','Grocery','Grocery','Grocery','Grocery','Grocery','Grocery','Grocery','Haircut','Haircut','Haircut','Liquor','Medical','Medical','Other-Luxury','Subscriptions','Subscriptions','Subscriptions','Subscriptions','Subscriptions','Subscriptions','Eating Out','Excluded','Excluded','Charity','Gifts','Eating Out','Grocery','Grocery','Grocery','Excluded','Grocery','Eating Out','Grocery','Grocery','Excluded','Eating Out','Fees','Excluded','Excluded','Excluded','Excluded','Excluded','Excluded','Excluded','Excluded','Excluded']})

def TD_formatter(df):
    df = df[['Date', 'Description', 'Debit', 'Credit']]
    df['Debit'] *= -1
    df['Amount'] = df['Credit'].fillna(df['Debit'])
    df = df.drop(['Debit', 'Credit'], axis='columns')
    df['Card'] = 'TD'
    df['Post Date'] = df['Date']
    df['Month'] = month
    df = pd.merge(df, categories, how='left')
    df.columns = ['Transaction Date', 'Description', 'Amount', 'Card', 'Post Date', 'Month', 'Classification']
    df = df.reindex(columns=['Transaction Date', 'Post Date', 'Month', 'Description', 'Classification', 'Amount', 'Card'])
    return df

def AMEX_formatter(df):
    df = df[['Date', 'Description', 'Amount']]
    # file_path = 'hello' # this line should be used when running the test file
    if 'blue' in file_path:
        df['Card'] = 'Amex - Blue'
    elif 'hilton' in file_path:
        df['Card'] = 'Amex - Hilton'
    elif 'bonvoy' in file_path:
        df['Card'] = 'Amex - Bonvoy'
    elif 'business' in file_path:
        df['Card'] = 'Amex - Bonvoy Business'
    else:
        df['Card'] = 'Amex - ?'
    df['Amount'] *= -1
    df['Post Date'] = df['Date']
    df['Month'] = month
    df = pd.merge(df, categories, how='left')
    df.columns = ['Transaction Date', 'Description', 'Amount', 'Card', 'Post Date', 'Month', 'Classification']
    df = df.reindex(columns=['Transaction Date', 'Post Date', 'Month', 'Description', 'Classification', 'Amount', 'Card'])
    return df

def Chase_formatter(df):
    df = df[['Transaction Date', 'Post Date', 'Description', 'Amount']]
    if '8517' in file_path:
        df['Card'] = 'Chase - Freedom'
    elif '6937' in file_path:
        df['Card'] = 'Chase - Sapphire'
    elif '1277' in file_path:
        df['Card'] = 'Chase - United'
    elif '1389' in file_path:
        df['Card'] = 'Chase - Ink'
    else:
        df['Card'] = 'Chase - ?'
    df['Month'] = month
    df = pd.merge(df, categories, how='left')
    df = df.reindex(columns=['Transaction Date', 'Post Date', 'Month', 'Description', 'Classification', 'Amount', 'Card'])
    return df

def Barclays_formatter(df):
    df = df[['Transaction Date', 'Description', 'Amount']]
    df['Card'] = 'Barclays'
    df['Post Date'] = df['Transaction Date']
    df['Month'] = month
    df = pd.merge(df, categories, how='left')
    df = df.reindex(columns=['Transaction Date', 'Post Date', 'Month', 'Description', 'Classification', 'Amount', 'Card'])
    return df

all_files = DataFrame(columns=['Transaction Date', 'Post Date', 'Month', 'Description', 'Classification', 'Amount', 'Card'])

with open('/Users/norma/Downloads/expenses_this_month.csv', 'w') as outfile:
    categories = pd.read_csv('/Users/norma/Code/expenses/env-expenses/Categories.csv', header=0) # do not use this line when running test file
    for file_path in glob.glob('/Users/norma/Downloads/Expenses/*'):
        if 'barclays' in file_path:

            df = pd.read_csv(file_path, header=3)
            df = Barclays_formatter(df)
        else:
            df = pd.read_csv(file_path)
            if 'td' in file_path:
                df = TD_formatter(df)
            elif 'amex' in file_path:
                df = AMEX_formatter(df)
            elif 'Chase' in file_path:
                df = Chase_formatter(df)
        all_files = pd.concat([all_files, df])
    all_files.to_csv(outfile, index=False)