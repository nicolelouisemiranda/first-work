'''
Database was downloaded from Kaggle (link: https://www.kaggle.com/datasets/cameronseamons/electronic-sales-sep2023-sep2024)

Database columns:
    Customer ID: Unique identifier for each customer.
    Age: Age of the customer (numeric)
    Gender: Gender of the customer (Male or Female)
    Loyalty Member: (Yes/No) (Values change by time, so pay attention to who cancelled and who signed up)
    Product Type: Type of electronic product sold (e.g., Smartphone, Laptop, Tablet)
    SKU: a unique code for each product.
    Rating: Customer rating of the product (1-5 stars) (Should have no Null Ratings)
    Order Status: Status of the order (Completed, Cancelled)
    Payment Method: Method used for payment (e.g., Cash, Credit Card, Paypal)
    Total Price: Total price of the transaction (numeric)
    Unit Price: Price per unit of the product (numeric)
    Quantity: Number of units purchased (numeric)
    Purchase Date: Date of the purchase (format: YYYY-MM-DD)
    Shipping Type: Type of shipping chosen (e.g., Standard, Overnight, Express)
    Add-ons Purchased: List of any additional items purchased (e.g., Accessories, Extended Warranty)
    Add-on Total: Total price of add-ons purchased (numeric)

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eletronics = pd.read_csv(r"Electronic_sales_Sep2023-Sep2024.csv",
                         header=0,
                         index_col=False)

# dataframe shape: 16 columns x 20,000 rows
print('Dataframe shape:', eletronics.shape)
#print(eletronics.head())

# convert dates to datetype mode
#print(eletronics.dtypes)
eletronics['Purchase Date'] = pd.to_datetime(eletronics['Purchase Date'])

# checking duplicates
# Customer ID is duplicated because the same customer purchased multiple times
#print(eletronics[ eletronics.duplicated(['Customer ID']) ])

# NULL VALUES
#print(eletronics.isnull().sum()) # Gender and Add-ons have null values

# print gender null value and check if row is duplicated
#print(eletronics[ eletronics['Gender'].isnull() == True ])
#print(eletronics[ eletronics['Customer ID'] == 19998 ])
# replace missing value
eletronics['Gender'] = eletronics['Gender'].fillna("Unknown")

# print add-ons missing values
#print(eletronics[ eletronics['Add-ons Purchased'].isnull() == True ])
# replace missing values
eletronics['Add-ons Purchased'] = eletronics['Add-ons Purchased'].fillna('None')

print(eletronics.describe())
print(eletronics.head())

fig1 = plt.figure(figsize=(5,5))
plt.hist(eletronics['Age'])
plt.xlabel('Age')
plt.ylabel('Counts')
fig1.show()
