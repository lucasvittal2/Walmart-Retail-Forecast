import MyAnalysisApi as myapi

#setup enviorment
myapi.setup_env()

#load Data
dataset  = myapi.load_data()

# spliting data by store
df_train = dataset["train"]

# save  each dataframe per store
PATH_OUTPUT =  "C:\\Users\\lucas\\Documents\\data_science projects\\Walmart Retail Forecast\dataset\\assets\\transformed\\splited"
print("Spliting Data per store...\n")
data_per_store = myapi.split_by_store(df_train, "Store")
print("Dataset was splited successfully and dataframe per store generated!\n")
stores = [store for store in range(1,46)]

print("Starting to save stores dataframe...\n")
for store in stores:
    key = str(store)
    filename = "df_train_" + key +".csv"
    myapi.save_df(data_per_store[key], PATH_OUTPUT, filename)
    print( filename + " was saved\n")

print("Data Transformation completed successfully")




# resampling data through mean of weekly sales of all store

