import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('2016-2019_finance_liquor_sales.csv')

df1 = pd.DataFrame(data, columns=['zip_code', 'item_description', 'bottles_sold'])
df1.groupby('zip_code').bottles_sold.max()
idx = df1.groupby('zip_code').bottles_sold.transform(max) == df1['bottles_sold']
print(df1[idx])

df2 = pd.DataFrame(data, columns=['store_name','sale_dollars'])
x= df2.groupby('store_name').sale_dollars.sum()
xdf = pd.DataFrame(x)
xdf['sales_perc'] =round((xdf['sale_dollars'] / xdf['sale_dollars'].sum()) * 100, 2)
print(xdf)




