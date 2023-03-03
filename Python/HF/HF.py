#c:\users\sibuj\appdata\local\programs\python\python36-32\lib\site-packages

import pandas as pd
import os

XL_PATH='C:/Sibu/Personal/Others/Church/Trustees/2022/'
XLF='AMC-MemberList-2023-Public.xlsx'
print(path+excel_file)

#df_members = pd.read_excel(path+excel_file)

df_members = pd.read_excel(
     os.path.join(XL_PATH, "Data", XLF),
     engine='openpyxl',
)

print(df_members)
