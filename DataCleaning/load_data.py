import pandas as pd

customers = pd.read_csv(r'C:\DV\Global electronic\Data\RawData\Customers.csv',encoding="latin1",keep_default_na=False)
exchange_rate = pd.read_csv(r'C:\DV\Global electronic\Data\RawData\Exchange_Rates.csv',encoding="latin1")
products = pd.read_csv(r'C:\DV\Global electronic\Data\RawData\Products.csv',encoding="latin1")
sales = pd.read_csv(r'C:\DV\Global electronic\Data\RawData\Sales.csv',encoding="latin1")
stores = pd.read_csv(r'C:\DV\Global electronic\Data\RawData\Stores.csv',encoding="latin1")