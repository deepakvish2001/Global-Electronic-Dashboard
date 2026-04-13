import pandas as pd
from decode_special_char import *

# Month order
order_month = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

# =========================
# 1. Merge all tables
# =========================
df = sales.merge(products, on='productkey', how='left')\
        .merge(customers, on='customerkey', how='left')\
        .merge(stores, on='storekey', how='left')\
        .merge(exchange_rate, 
               left_on=['order date','currency code'],
               right_on=['date','currency'],
               how='left')

# =========================
# 2. Date Features
# =========================
df['order date'] = pd.to_datetime(df['order date'])

df['month'] = df['order date'].dt.month
df['year'] = df['order date'].dt.year
df['month name'] = df['order date'].dt.month_name()

# Sort month correctly
df['month name'] = pd.Categorical(
    df['month name'],
    categories=order_month,
    ordered=True
)

# =========================
# 3. Store Type
# =========================
df['stores_type'] = df['storekey'].apply(
    lambda x: 'In-store' if x > 0 else 'Online'
)

# =========================
# 4. Financial Calculations
# =========================
df['revenue'] = df['quantity'] * df['unit price usd'] * df['exchange']
df['cost'] = df['quantity'] * df['unit cost usd'] * df['exchange']
df['profit'] = df['revenue'] - df['cost']

# =========================
# 5. (Optional) Clean Data
# =========================
df = df.dropna(subset=['exchange'])  # remove missing currency conversion

# =========================
# 6. Export ONLY ONE FILE
# =========================
df.to_csv(r"C:\DV\Global electronic\Data\Export_data\final_dataset.csv", index=False)

print("✅ Final dataset exported successfully!")


stores_value = df.groupby('stores_type').agg(total_revenue = ('revenue','sum'),
                                             total_order = ('order number','nunique')).reset_index()
stores_value['AOV'] = stores_value['total_revenue'] / stores_value['total_order']

stores_value.to_csv(r"C:\DV\Global electronic\Data\Export_data\AOV_values.csv", index=False)