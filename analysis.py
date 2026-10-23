# FCS Kiosk - Data Science Project
# 7th Semester Software Engineering
# Student: Bushra Batool Kharal
# Project: Smart Kiosk System - Lee Dong Issue Solved

import pandas as pd

# Sample Sales Data
data = {
    'Product': ['Burger', 'Fries', 'Pizza', 'Coffee', 'Sandwich'],
    'Total_Sold': [111, 123, 110, 92, 87],
    'Price_PKR': [350, 150, 400, 180, 200],
    'Location': ['Main Campus', 'Cafeteria', 'Library', 'Main Campus', 'Cafeteria']
}

df = pd.DataFrame(data)
df['Revenue'] = df['Total_Sold'] * df['Price_PKR']

print("FCS Kiosk Data Analysis")
print(df)
print("\nMost Popular:", df.loc[df['Total_Sold'].idxmax()]['Product'])
print("Total Revenue:", df['Revenue'].sum(), "PKR")
