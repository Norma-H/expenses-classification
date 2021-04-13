from expenses_formatter import TD_formatter, Chase_formatter, AMEX_formatter, Barclays_formatter
import pandas as pd
from pandas import DataFrame

categories = DataFrame({'Description': ['PAYPAL *PROGRESSIVE','VW CREDIT ONLINE PMT','9495 PARKING CORP','ASBURY PARK PASSPORT PAR','COSTCO GAS #0329','NJ EZPASS','GOOGLE *Google Fi','TMOBILE*AAL TEL','TMOBILE*AUTO PAY','Chabad at','ORG FOR RESOL AGUNOT','SEPHARDIC INSTITUTE FOR','SQ *CONGREGATION MAGEN DA','SQ *RACHEL LEAH CHESED FU','NORDSTROM RACK #0650','On Inc','REI.COM','Zara.com/USA','DOORDASH CREDIT','DOORDASH*THE JUICE THE','FALAFEL OFF THE CORNER','ROOK COFFEE LITTLE OOakhurst NJ','GBCI','HUMBLEBUNDLE.COM','REUVEN LERNER','EMBROIDER A GIFT','SP * DIMPLES BABY BROO','WISHING WELL','COSTCO WHSE #0329','LOCAL 130 SEAFOOD Asbury Park NJ','M A KOSHER MEATS INOAKHURST NJ','SP * BURLAP &amp; BARREL','SQ *LOCAL 130 SEAFOOD','STOP &amp; SHOP 2813','WEGMANS OCEAN NJ','HIGH MAINTENANCE','HIGH MAINTENANCE STUOAKHURST NJ',"KIMMY'S NAIL SALON",'COURT LIQUORS','CAPSULE PHARMACY','TDBANK BILL PAY CHECK 995030 Phyliss Tobin','CITIZEN WATCH COMPANY','Amazon web services','GOOGLE*GOOGLE STORAGE','PAYPAL *LINKEDIN','PAYPAL *NY TIMES NYTIMES','PP*APPLE.COM/BILL','Spotify USA','ICHIBAN JAPANESE RESTAU','AUTOMATIC PAYMENT - THANK','Payment Thank You-Mobile','Chabad at Emory','PAYPAL *MODERNMOSAI','BENNY`S BRICK OVEN INC','WEGMANS             OCEAN               NJ','I&D Glatt Ave P     Brooklyn            NY','LOCAL 130 SEAFOOD   Asbury Park         NJ','MOBILE PAYMENT - THANK YOU','COMETEER            GLOUCESTER          MA','ROOK COFFEE LITTLE OOcean Township      NJ','KINGS HIGHWAY GLATT OAKHURST            NJ','SHOPRITE NEPTUNE S1 NEPTUNE             NJ','AUTOPAY PAYMENT - THANK YOU','ROOK COFFEE LITTLE OOakhurst            NJ','RENEWAL MEMBERSHIP FEE','CHASE CREDIT CRD AUTOPAY ','CHASE CREDIT CRD AUTOPAYBUS','AMEX EPAYMENT    ACH PMT ','NYS DOL UI DD    UI DD ','IOD INTEREST PAID ','Online Xfer Transfer to CK x9776','VW CREDIT        ONLINE PMT ','FLATIRON HEALTH  PAYROLL ','CHASE CREDIT CRD EPAY '],
                       'Classification': ['Car Insurance','Car Insurance','Car Transportation','Car Transportation','Car Transportation','Car Transportation','Cell Phone','Cell Phone','Cell Phone','Charity','Charity','Charity','Charity','Charity','Clothing','Clothing','Clothing','Clothing','Eating Out','Eating Out','Eating Out','Eating Out','Education','Education','Education','Gifts','Gifts','Gifts','Grocery','Grocery','Grocery','Grocery','Grocery','Grocery','Grocery','Haircut','Haircut','Haircut','Liquor','Medical','Medical','Other-Luxury','Subscriptions','Subscriptions','Subscriptions','Subscriptions','Subscriptions','Subscriptions','Eating Out','Excluded','Excluded','Charity','Gifts','Eating Out','Grocery','Grocery','Grocery','Excluded','Grocery','Eating Out','Grocery','Grocery','Excluded','Eating Out','Fees','Excluded','Excluded','Excluded','Excluded','Excluded','Excluded','Excluded','Excluded','Excluded']})


def test_TD_formatter():
    df = DataFrame(columns=['Date','Bank RTN','Account Number','Transaction Type','Description','Debit','Credit',
                            'Check Number','Account Running Balance'])
    df['Date'] = ['3/17/21','3/17/21','3/17/21','3/17/21','3/16/21','3/16/21','3/15/21','3/15/21','3/15/21','3/15/21','3/12/21','3/9/21','3/9/21','3/9/21','3/9/21']
    df['Bank RTN'] = '11103093'
    df['Account Number'] = '4942163893'
    df['Transaction Type'] = ['DEBIT','DEBIT','DEBIT','DEBIT','DIRECTDEP','DIRECTDEP','DEBIT','DIRECTDEP','DIRECTDEP','DIRECTDEP','CREDIT','CHECK','DEBIT','DIRECTDEP','DIRECTDEP']
    df['Description'] = ['CHASE CREDIT CRD EPAY','CHASE CREDIT CRD EPAY','CHASE CREDIT CRD EPAY','VENMO            PAYMENT','NYS DOL UI DD    UI DD','NYS DOL UI DD    UI DD','GOLDMAN SACHS BA COLLECTION','FLATIRON HEALTH  PAYROLL','FLATIRON HEALTH  PAYROLL','FLATIRON HEALTH  PAYROLL','TD ZELLE RCVD 460005     P2P MEIR  SUTTON            VISA DIRECT   * AZ','CHECK # 186','VW CREDIT        ONLINE PMT','NYS DOL UI DD    UI DD','NYS DOL UI DD    UI DD']
    df['Debit'] = ['1285.93','1189.63','150','22','NaN','NaN','3000','NaN','NaN','NaN','NaN','1075','286.55','NaN','NaN']
    df['Credit'] = ['NaN','NaN','NaN','NaN','397.25','262.5','NaN','1712.27','441.6','99.68','15','NaN','NaN','397.25','262.5']
    df.loc[11]['Check Number'] = 186
    df['Account Running Balance'] = ['3115.8','4401.73','5591.36','5741.36','5763.36','5366.11','5103.61','8103.61','6391.34','5949.74','5850.06','5835.06','6910.06','7196.61','6799.36']
    result = TD_formatter(df)
    output = df[['Date', 'Description','Debit', 'Credit']]
    output['Debit'] *= -1
    output['Amount'] = output['Credit'].fillna(output['Debit'])
    output = output.drop(['Debit', 'Credit'], axis='columns')
    output['Card'] = 'TD'
    output['Post Date'] = output['Date']
    output['Month'] = 3
    output = pd.merge(output, categories, how='left')
    output.columns = ['Transaction Date', 'Description','Amount', 'Card', 'Post Date', 'Month', 'Classification']
    output = output.reindex(columns=['Transaction Date', 'Post Date', 'Month','Description','Classification','Amount', 'Card'])
    assert pd.testing.assert_frame_equal(output, result) == None

def test_Chase_formatter():
    df = DataFrame(columns=['Transaction Date','Post Date','Description','Category', 'Type', 'Amount', 'Memo'])
    df['Transaction Date'] = ['3/20/21','3/20/21','3/18/21','3/20/21','3/18/21','3/18/21','3/18/21','3/18/21','3/17/21','3/17/21','3/16/21','3/15/21','3/15/21','3/14/21','3/14/21','3/14/21','3/12/21','3/11/21','3/8/21','3/7/21','3/7/21','3/5/21','3/4/21','3/2/21','3/2/21','2/28/21','2/28/21']
    df['Post Date'] = ['3/22/21','3/22/21','3/21/21','3/21/21','3/21/21','3/21/21','3/21/21','3/21/21','3/18/21','3/18/21','3/16/21','3/16/21','3/15/21','3/15/21','3/15/21','3/15/21','3/14/21','3/12/21','3/9/21','3/8/21','3/8/21','3/7/21','3/5/21','3/3/21','3/2/21','3/1/21','3/1/21']
    df['Description'] = ['THE HOME DEPOT 949','THE HOME DEPOT 949','THE HOME DEPOT 949','PAYPAL *NY TIMES NYTIMES','THE HOME DEPOT 949','MACYS   .COM','THE HOME DEPOT 949','THE HOME DEPOT 949','PP*APPLE.COM/BILL','Amazon.com*WG2QV6I33','Payment Thank You-Mobile','NJ EZPASS','Amazon.com*B34GR05V3','NYCFINANCECONVENIENCEFEE','COSTCO GAS #0329','DOF PARKINGANDCAMERA TIX','CAPSULE PHARMACY','ICHIBAN JAPANESE RESTAU','SP * DIMPLES BABY BROO','AMZN Mktp US','Amazon.com','AMZN Mktp US*TB90L0OR3','NJ EZPASS','Amazon.com*6M97Q1SU3','AUTOMATIC PAYMENT - THANK','Spotify USA','SP * DIMPLES BABY BROO']
    df['Category'] = ['Home','Home','Home','Professional Services','Home','Shopping','Home','Home','Shopping','Shopping','NaN','Travel','Shopping','Bills & Utilities','Gas','Bills & Utilities','Health & Wellness','Food & Drink','Home','Shopping','Shopping','Shopping','Travel','Shopping','NaN','Bills & Utilities','Home']
    df['Type'] = ['Return','Sale','Sale','Sale','Sale','Return','Sale','Sale','Sale','Sale','Payment','Sale','Sale','Sale','Sale','Sale','Sale','Sale','Sale','Return','Return','Sale','Sale','Sale','Payment','Sale','Sale']
    df['Amount'] = ['1.79','-61.12','-19.13','-6','-150','29.5','-150','-43.43','-0.99','-5.44','1285.93','-60','-36','-1','-32.47','-50','-20.69','-33.05','-26','10.55','52.25','-14.92','-60','-87.52','1309.19','-5.31','-52']
    result = Chase_formatter(df)
    output = df[['Transaction Date', 'Post Date', 'Description', 'Amount']]
    output['Card'] = 'Chase - ?'
    output['Month'] = 3
    output = pd.merge(output, categories, how='left')
    output = output.reindex(columns=['Transaction Date', 'Post Date', 'Month','Description','Classification','Amount', 'Card'])
    assert pd.testing.assert_frame_equal(output, result) == None

def test_AMEX_formatter():
    df = DataFrame(columns=['Date','Description','Card Member', 'Account #', 'Amount'])
    df['Date'] = ['3/24/21','3/22/21','3/22/21','3/21/21','3/21/21','3/17/21','3/16/21','3/15/21','3/15/21','3/14/21','3/14/21','3/12/21','3/10/21','3/9/21','3/8/21','3/7/21','3/7/21','3/3/21']
    df['Post Date'] = df['Date']
    df['Description'] = ['LOCAL 130 SEAFOOD   Asbury Park         NJ','LOCAL 130 SEAFOOD   Asbury Park         NJ','WEGMANS             OCEAN               NJ','I&D Glatt Ave P     Brooklyn            NY','WEGMANS             OCEAN               NJ','LOCAL 130 SEAFOOD   Asbury Park         NJ','MOBILE PAYMENT - THANK YOU','COMETEER            GLOUCESTER          MA','LOCAL 130 SEAFOOD   Asbury Park         NJ','OURI S MARKET       BROOKLYN            NY','WEGMANS             OCEAN               NJ','ROOK COFFEE LITTLE OOcean Township      NJ','LOCAL 130 SEAFOOD   Asbury Park         NJ','KINGS HIGHWAY GLATT OAKHURST            NJ','LOCAL 130 SEAFOOD   Asbury Park         NJ','OURI S MARKET       BROOKLYN            NY','SHOPRITE NEPTUNE S1 NEPTUNE             NJ','LOCAL 130 SEAFOOD   Asbury Park         NJ']
    df['Amount'] = ['14.62','11.95','29.61','82.62','142.7','16.49','-754.26','79','12.47','33.65','134.88','15.25','13.86','10.7','11.5','24.48','131.61','11.88']
    result = AMEX_formatter(df)
    output = df[['Date', 'Description', 'Amount']]
    output['Amount'] *= -1
    output['Card'] = 'Amex - ?'
    output['Post Date'] = output['Date']
    output['Month'] = 3
    output = pd.merge(output, categories, how='left')
    output.columns = ['Transaction Date', 'Description', 'Amount', 'Card', 'Post Date', 'Month', 'Classification']
    output = output.reindex(columns=['Transaction Date', 'Post Date', 'Month','Description','Classification','Amount', 'Card'])
    assert pd.testing.assert_frame_equal(output, result) == None

def test_Barclays_formatter():
    df = DataFrame(columns=['Transaction Date', 'Description', 'Category', 'Amount'])
    df['Transaction Date'] = ['9/23/20','9/18/20','9/17/20','9/14/20']
    df['Description'] = ['111 EIGHTH AVE PKG LLC','APPLE.COM/BILL','BALANCE ADJUSTMENT','Payment Received']
    df['Category'] = ['DEBIT','DEBIT','CREDIT','CREDIT']
    df['Amount'] = ['-69','-0.99','0.99','18.99']
    result = Barclays_formatter(df)
    output = df[['Transaction Date', 'Description', 'Amount']]
    output['Post Date'] = output['Transaction Date']
    output['Card'] = 'Barclays'
    output['Month'] = 3
    output = pd.merge(output, categories, how='left')
    output = output.reindex(columns=['Transaction Date', 'Post Date', 'Month','Description','Classification','Amount', 'Card'])
    assert pd.testing.assert_frame_equal(output,result) == None