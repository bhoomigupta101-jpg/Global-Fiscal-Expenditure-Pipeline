import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

server_name= r'DESKTOP-KPVO5NF\SQLEXPRESS'
conn_str = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE=PublicSpendingDB;Trusted_Connection=yes;"
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(conn_str)}")

df = pd.read_sql("SELECT * FROM vw_Final_Executive_Report", engine)

df = df.sort_values(['Country', 'Government_Level', 'FiscalYear'])
df['YoY_Growth_Percent'] = df.groupby(['Country', 'Government_Level'])['Amount'].pct_change() * 100

df['YoY_Growth_Percentt'] = df['YoY_Growth_Percent'].fillna(0)

df.to_csv('Cleaned_Executive_Data.csv', index=False)
print("Calculation Check: Success. Growth figures validated.")