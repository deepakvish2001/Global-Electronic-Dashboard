from load_data import *
import numpy as np

#clean customer
customers.columns = customers.columns.str.lower().str.strip()
customers = customers.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
customers['gender'] = customers['gender'].astype('category')
customers['country'] = customers['country'].astype('category')
customers['state'] = customers['state'].astype('category')
customers['continent'] = customers['continent'].astype('category')

#handle customer dates 
customers['birthday'] = customers['birthday'].astype(str).str.strip()
customers['birthday'] = pd.to_datetime(customers['birthday'],format='mixed',errors='coerce')

customers.loc[
    customers['birthday'] > pd.Timestamp.today(),
    'birthday'
] -= pd.DateOffset(years=100)

#clean products
products.columns = products.columns.str.strip().str.lower()
products['color'] = products['color'].astype('category')
products['brand'] = products['brand'].astype('category')
products['category'] = products['category'].astype('category')
products['subcategory'] = products['subcategory'].astype('category')
products['unit cost usd'] = (products['unit cost usd'].astype(str).str.strip().str.replace('$','', regex=False).str.replace(',','',regex=False))
products['unit cost usd'] = pd.to_numeric(products['unit cost usd'], errors='coerce')
# bad_values = products[
#     pd.to_numeric(
#         products['unit cost usd'].astype(str).str.replace('$','',regex=False).str.replace(',','',regex=False).str.strip(),
#         errors='coerce'
#     ).isna()
# ]['unit cost usd']

# print(bad_values)
products['unit price usd'] = products['unit price usd'].astype(str).str.replace('$','',regex=False).str.replace(',','', regex=False).str.strip()
products['unit price usd'] = pd.to_numeric(products['unit price usd'],errors='coerce')


# clean sales and handle dates
sales.columns = sales.columns.str.strip().str.lower()
date_cols = ['order date', 'delivery date']

for col in date_cols:
    sales[col] = sales[col].astype(str).str.strip()
    sales[col] = pd.to_datetime(sales[col],format='mixed',errors='coerce')
    sales.loc[
        sales[col] > pd.Timestamp.today(),
        col
    ] -= pd.DateOffset(years=100)

#clean Exchange rate
exchange_rate.columns = exchange_rate.columns.str.strip().str.lower()
exchange_rate['currency'] = exchange_rate['currency'].astype('category')

#handle Date in Exchange rate
exchange_rate['date'] = exchange_rate['date'].astype('str').str.strip()
exchange_rate['date'] = pd.to_datetime(exchange_rate['date'],format='mixed',errors='coerce')
exchange_rate.loc[
    exchange_rate['date'] > pd.Timestamp.today(),
    'date'
] -= pd.DateOffset(years=100)


#clean stores
stores.columns = stores.columns.str.strip().str.lower()
stores['country'] = stores['country'].astype('category')
stores['state'] = stores['state'].astype('category')

#handle stores date
stores['open date'] = stores['open date'].astype('str').str.strip()
stores['open date'] = pd.to_datetime(stores['open date'],format='mixed',errors='coerce')
stores.loc[
    stores['open date'] > pd.Timestamp.today(),
    'open date'
] -= pd.DateOffset(years=100)