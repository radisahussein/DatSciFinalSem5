#==============================================================================================
'''
Data Science Final Project Semester 5

Members:
- Radisa Hussien Rachmadi - 2301891752
- Rayhan Ali Darmawan
'''
# IMPORTING LIBRARIES =========================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DATASETS ====================================================================================

df_1 = pd.read_csv(r'C:\Users\Fajar Rachmadi\Desktop\CODE\DatSciFinalSem5\Data\conflict_data_idn2 - conflict_data_idn2.csv')
df_2 = pd.read_csv(r'C:\Users\Fajar Rachmadi\Desktop\CODE\DatSciFinalSem5\Data\conflict-data-for-indonesia-2 - conflict-data-for-indonesia-2.csv')

# PREPARING DATA ====================================================================================================

df = pd.concat([df_1,df_2]).drop_duplicates().reset_index(drop=True)
print(df.head(20))

print(df.sort_values(by='year'))

df.to_csv(r'C:\Users\Fajar Rachmadi\Desktop\CODE\DatSciFinalSem5\Data\final_data.csv',index=False)