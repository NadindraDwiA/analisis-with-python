import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset into a DataFrame
data = pd.read_csv('./dataset/all_data.csv')  # Replace with the actual file path if it's a CSV file

# Convert 'order_purchase_timestamp' to a datetime object
data['order_purchase_timestamp'] = pd.to_datetime(data['order_purchase_timestamp'])

# Extract the month and year from the 'order_purchase_timestamp'
data['order_month_year'] = data['order_purchase_timestamp'].dt.to_period('M')

# Create a Streamlit app
st.title("E-commerce Data Analysis Dashboard")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Question 1: Peak Sales Time
st.header("Question 1: Kapan waktu puncak penjualan?")
monthly_sales = data.groupby('order_month_year')['payment_value'].sum()
peak_month = monthly_sales.idxmax()
peak_sales = monthly_sales.max()
st.write(f"The peak sales month is {peak_month} with total sales of {peak_sales:.2f}.")

# Question 2: Most Popular Product and Product Category
st.header("Question 2: Produk apa yang paling laris? Kategori produk apa yang paling populer?")
product_sales = data.groupby('product_id')['payment_value'].sum()
most_popular_product_id = product_sales.idxmax()
most_popular_product_sales = product_sales.max()

category_sales = data.groupby('product_category_name_english')['payment_value'].sum()
most_popular_category = category_sales.idxmax()
most_popular_category_sales = category_sales.max()

st.write(f"The most popular product is {most_popular_product_id} with total sales of {most_popular_product_sales:.2f}.")
st.write(f"The most popular product category is {most_popular_category} with total sales of {most_popular_category_sales:.2f}.")

# Question 3: Most Customers by City and State
st.header("Question 3: Pelanggan dari kota atau negara bagian mana yang paling banyak melakukan pembelian?")
city_customers = data.groupby('customer_city')['customer_unique_id'].nunique()
most_customers_city = city_customers.idxmax()
most_customers_count_city = city_customers.max()

state_customers = data.groupby('customer_state')['customer_unique_id'].nunique()
most_customers_state = state_customers.idxmax()
most_customers_count_state = state_customers.max()

st.write(f"The city with the most customers is {most_customers_city} with {most_customers_count_city} customers.")
st.write(f"The state with the most customers is {most_customers_state} with {most_customers_count_state} customers.")

# Question 4: Most Frequently Used Payment Method
st.header("Question 4: Metode pembayaran apa yang paling sering digunakan oleh pelanggan?")
payment_counts = data['payment_type'].value_counts()
most_frequent_payment = payment_counts.idxmax()
most_frequent_payment_count = payment_counts.max()
st.write(f"The most frequently used payment method is {most_frequent_payment} with {most_frequent_payment_count} transactions.")

# Question 5: Average Delivery Time
st.header("Question 5: Berapa lama waktu pengiriman rata-rata?")
average_delivery_time = data['delivery_time'].mean()
st.write(f"The average delivery time is {average_delivery_time:.2f} days.")

# Visualizations
st.header("Visualizations")
st.subheader("Monthly Sales")
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
st.pyplot()

st.subheader("Top 10 Product Categories by Sales")
plt.figure(figsize=(12, 6))
category_sales.nlargest(10).plot(kind='bar')
plt.title('Top 10 Product Categories by Sales')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
st.pyplot()

st.subheader("Number of Customers by State")
plt.figure(figsize=(12, 6))
state_customers.plot(kind='bar')
plt.title('Number of Customers by State')
plt.xlabel('State')
plt.ylabel('Number of Customers')
st.pyplot()

st.subheader("Payment Method Usage")
plt.figure(figsize=(12, 6))
payment_counts.plot(kind='bar')
plt.title('Payment Method Usage')
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
st.pyplot()

st.subheader("Delivery Time Distribution")
plt.figure(figsize=(12, 6))
data['delivery_time'].plot(kind='hist', bins=20, edgecolor='k')
plt.title('Delivery Time Distribution')
plt.xlabel('Delivery Time (days)')
plt.ylabel('Frequency')
st.pyplot()
