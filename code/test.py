import pandas as pd
from MyAnalysisApi import load_data, setup_env

setup_env()

dataset = load_data()

df_train = dataset["train"]


date_records = df_train["Date"].unique() 
amount_date_records =  len(date_records)

print(amount_date_records)

# lest validate if all stores has all days
stores = [ store for store in range(1,46)]
for store in stores:
    df_store = df_train[ df_train["Store"] == store]
    store_dates =  df_store["Date"].unique()
    store_registers = len( store_dates)
    print(store_registers)
    if store_registers != amount_date_records:
        print("Store ID %d does not have all date records\n" %store)


print("Alright, you can peform groupby without introducing bias")