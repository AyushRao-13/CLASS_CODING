import os
import numpy as np
import pandas as pd
import matplotlib as plt

data = {
    'Name': ['Ayush', 'Yadav', 'Rao', 'Sahab'],
    'Age' : [20,24,23,21],
    'City': ['Delhi', 'Haryana', 'Chandigarh', 'Punjab']
}
df_show = pd.DataFrame(data)
print(df_show)

df_csv = pd.read_csv('E:\\Users\\Dell\\Downloads\\archive\\Sensitivity_Soil_Nutrient_Pools.csv')
print(df_csv)

df_excel = pd.read_excel('D:\\AYUSH\\RANDOM SHIT\\student_data.xlsx', engine='openpyxl')
print(df_excel)