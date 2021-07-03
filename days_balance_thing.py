#!/usr/bin/env python
# a feature engineering attempt

import pandas as pd
import datetime

df = pd.read_csv("twm_checking_tran.csv", sep=";")

df["duplicated"] = df.duplicated(subset=["cust_id", "new_balance"])
df = df.loc[df["duplicated"] == True]
# df.sort_values(['cust_id', 'new_balance'], inplace=True)
df["tran_date"] = pd.to_datetime(df["tran_date"], format="%d.%m.%Y")
df.sort_values(["cust_id", "new_balance", "tran_date"], inplace=True)
df = df[["cust_id", "new_balance", "tran_date"]]
# only_dupes_df = df[['cust_id', 'new_balance', 'tran_date']]
df = df.reset_index()
# df.to_csv('new_csv.csv', index=False)
# only_duplicates.sort_values('cust_id', inplace=True)
results = []

start = None
end = None
for index, row in df.iterrows():
    cust_id = row["cust_id"]
    new_bal = row["new_balance"]
    if not start:
        start = row["tran_date"]
    try:
        next_row = df.iloc[index + 1]
    except:
        next_row = None
    if next_row is not None:
        if next_row["new_balance"] != new_bal or next_row["cust_id"] != cust_id:
            end = row["tran_date"]
    if cust_id and new_bal and start and end:
        number_of_days = abs((start - end).days)
        row = [cust_id, new_bal, start, end, number_of_days]
        results.append(row)
        cust_id, new_bal, start, end = None, None, None, None

results_df = pd.DataFrame(columns=["cust_id", "new_bal", "start", "end", "number_of_days"], data=results)

# # # print(results)
# # # only_duplicates = df.loc[df['duplicated'] == True]
# # # print(only_duplicates)
# # # df.to_csv('new_csv.csv', index=False)
# # only_dupes_df.to_csv('new_csv.csv', index=False)
results_df.to_csv("new_csv.csv", index=False)
