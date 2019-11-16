# importing useful packages
import pandas as pd

# i create a function to easily retrive data in case of an update of original files
def call_data_merged():
    # importing meta
    meta_browser = pd.read_csv('./Data/raw_data/meta_browser.csv')
    print('meta_browser data: \n', meta_browser.head())
    meta_device = pd.read_csv('./Data/raw_data/meta_device.csv')
    print('\n \n meta_device data: \n', meta_device.head())
    meta_os = pd.read_csv('./Data/raw_data/meta_os.csv')
    print('\n \n meta_os data: \n', meta_os.head())

    # importing dataset
    ds = pd.read_csv('./Data/raw_data/dataset.csv')
    #print('\n \n Dataset: \n', ds.head())

    # importing pickle
    data_pickle = pd.read_pickle('./Data/raw_data/dataset.pkl')
    print('\n \n Dataset: \n', data_pickle.head())

    # check if missing values:
    data_pickle.info()
    # there are some missing values, but i can retrive from other sets

    # top 10 by durata_vita
    data_pickle.sort_values(by=['conteggio_giorni_totale'], ascending=False).head(10)

    data_pickle.equals(ds) # dataset csv and pickle are equals

    # let's merge dataframes:
        # with meta browser
    df = pd.merge(ds, meta_browser, how='left', left_on = 'browser_type', right_on = 'id')
    df = df.drop(['browser_type','id'], axis=1)
    df = df.rename({'name':'browser_name'}, axis=1)
        # with meta device
    df = pd.merge(df, meta_device, how='left', left_on = 'device_type', right_on = 'id')
    df = df.drop(['device_type','id'], axis=1)
    df = df.rename({'name':'device_name'}, axis=1) 
        # with meta os
    df = pd.merge(df, meta_os, how='left', left_on = 'os_type', right_on = 'id')
    df = df.drop(['os_type','id'], axis=1)
    df = df.rename({'name':'os_name'}, axis=1)

    df.head()
    df.to_csv(r".\Data\processed_data\data_merged.csv")
    return df
call_data_merged()