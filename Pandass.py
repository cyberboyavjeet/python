import pandas as pd
df=pd.read_excel('data.xlsx')
# print(df.head(1))
# print(df.head(5))
# print(df.tail(1))
# print(df.info())
# print(df.describe())
# print(df['Phone'].mean())
y=df['Phone']
print(y)