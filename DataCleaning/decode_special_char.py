from clean_data import *
import pandas as pd
import unicodedata

#decode special character
customers['name'] = customers['name'].apply(
    lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8')
)

customers['state'] = customers['state'].apply(
    lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8')
)

stores['state'] = stores['state'].apply(
    lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8')
)

print(customers.info())
print(exchange_rate.info())
print(products.info())
print(sales.info())
print(stores.info())