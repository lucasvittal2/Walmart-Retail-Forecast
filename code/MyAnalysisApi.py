import os
from Parameters import THESHOLD_SALES_VALUE, PROJECT_ROOT_PATH
import pandas as pd

def setup_env():
    os.chdir(PROJECT_ROOT_PATH)
    
def load_data():
    
    setup_env()
    
    #load data
    df_train = pd.read_csv( "dataset/train/train.csv")
    df_test = pd.read_csv(  "dataset/test/test.csv")
    df_stores = pd.read_csv(  "dataset/features/stores.csv")
    df_sampleSub = pd.read_csv( "dataset/features/sampleSubmission.csv")
    df_features = pd.read_csv("dataset/features/features.csv")
    
    
    dataset =  {
        "train" : df_train,
        "test" : df_test,
        "stores" : df_stores,
        "sampleSub" : df_sampleSub,
        "features" : df_features 
    }
    
    return dataset
    
def split_by_store(df, column):
    data_per_store = {}
    stores = df[column].values
    
    #split dataset by store
    for store in stores:
        data_per_store[ str(store) ] = df[ df[column] == store]
        
    return data_per_store

def save_df(df, path, filename):
    df.to_csv(path + filename)
    