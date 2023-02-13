import MyAnalysisApi as myapi



myapi.setup_env()



dataset = myapi.load_data()
df_train  = dataset["train"]

print("Grouping by store.... \n ")
groupby_columns = [ "Date"]
df_grouped_by_store = myapi.group_by_store(df_train, groupby_columns)
print("Grouping By Processe completed Successfully!\n")

PATH = "C:\\Users\\lucas\\Documents\\data_science projects\\Walmart Retail Forecast\\dataset\\assets\\transformed\\grouped_by\\"
FILE_NAME = "trainset_grouped_by_store.csv"

print("Saving Dataframe...\n")
myapi.save_df(df_grouped_by_store, PATH, FILE_NAME)

print("Data transformed is avaialable, all done successfully!\n")