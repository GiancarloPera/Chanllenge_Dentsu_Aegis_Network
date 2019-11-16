#%% i used jupyter notebook as easier tool to do this analysis
# import packages
import pandas as pd
import matplotlib.pyplot 
import numpy as np

# import data merged
from Data_modeling.data_retrieve import call_data_merged
df = call_data_merged()
df.head()
print(df.info())
# %%
# As we have seen in the data retrieve file, there are some missing values:
print('Records with missing values in browser_name: \n', df[df.browser_name.isnull()])
# are almost from mobile device, infact:
df.device_name[df.browser_name.isnull()].value_counts().plot.bar()

# split city from state
df['stato'] = df.prima_citta.str.split('-', expand=True)[0]
df['citta'] = df.prima_citta.str.split('-', expand=True)[1]

# %% # usefull information:
# most active users respect usage:
print('Users ordered by durata vita: \n', df[['uuid','durata_vita','conteggio_giorni_totale']].sort_values(by=['durata_vita','conteggio_giorni_totale'], ascending=False))
# most active users respect usage in range of time 
# i used log to give more importance to who is more active in the 'durata_vita'
df['ratio_attivita'] = df.conteggio_giorni_totale/df.durata_vita*np.log(df.durata_vita)
print('Users ordered by ratio attivita: \n' ,df[['uuid','ratio_attivita','durata_vita','conteggio_giorni_totale']].sort_values(by=['ratio_attivita'], ascending=False))

top_25_users = df[['uuid','ratio_attivita','durata_vita','conteggio_giorni_totale']].sort_values(by=['ratio_attivita'], ascending=False)[0:25]
def top_users():
    return top_25_users


# %%
# website + visitati (considerando lo stesso user + volte) 
print('Nr of times on each website: \n', df.iloc[:,5:23].sum().sort_values(ascending=False))

# website + visitati da tutti (lo stesso user vale 1)
print('\n \n Website most visited in general: \n', df.iloc[:,5:23].fillna(0).astype(bool).sum(axis=0).sort_values(ascending=False))


#%%
# citta
print('Nr of users per city: \n' ,df.citta.value_counts())


#%%
# cities with most long-live cookies:
# sum durata vita x citta
print('Cities ordered on long-live cookies: \n', df.groupby(['citta'])['durata_vita'].sum().sort_values(ascending=False))


# %%
# most visited sites x citta
sites_list = [site for site in df.columns if 'site' in site]
print('Nr of visited site per city', df.groupby(['citta'])[sites_list].count().sort_values(by=sites_list, ascending=False))

# %%


# %%
