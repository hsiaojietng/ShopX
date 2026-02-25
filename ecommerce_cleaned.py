import sys
print ("Python version: " + sys.version)

import pandas as pd
import numpy as np

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Loading dataset labeled "E-commerce Sales Report" 
# Link: 
import time
time_begin = time.time()

df = pd.read_csv("C:\Data Analyst Portfolio\ShopX\E-commerce Sale Report.csv")

print(f'Run time: {round(((time.time()-time_begin)/60), 3)} mins') 
