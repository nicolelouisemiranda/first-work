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