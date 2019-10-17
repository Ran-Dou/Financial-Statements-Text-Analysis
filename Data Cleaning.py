import os
os.chdir('/Users/rdou/OneDrive - brandeis.edu/2019 Fincura Data Analyst Intern/Work/6 FINCURA Insights/Data')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('masked_3_NAICS_codes_20190520 (with LineOfBusiness and Officer).xlsx')
data['masked EntityID'].value_counts().sort_values(ascending=False).head()  # chekc whether the first column is unique
data = pd.read_excel('masked_3_NAICS_codes_20190520 (with LineOfBusiness and Officer).xlsx', index_col=0)
data.index.names = ['masked EntityID']
 
# Exploring NA Values  
data.info(verbose=True, null_counts=True)
data.isna().sum().plot()
data.isna().sum().sort_values(ascending=False).head(111)

#### Column Start with 'Cov'
data_Cov = data.filter(regex='^Cov', axis=1).dropna(how='all').dropna(axis=1, how='all')
columns = list(data.filter(regex='^Cov', axis=1).columns)
data.drop(columns=columns, inplace=True)
 
#### Check NA values again 
data.isna().sum().plot()
data.isna().sum().sort_values(ascending=False).head(111)

data.isna().sum().sort_values(ascending=False).head(111).index
 





 







