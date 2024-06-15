import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Replace 'path_to_your_file.csv' with the actual path to your CSV file
file_path = r'C:\Users\divya\Desktop\cognifyz\Dataset .csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv (file_path)

#Task2
# Determine the percentage of restaurants offering table booking and online delivery
total_restaurants = len(df)

# Count the number of restaurants offering table booking and online delivery
restaurants_with_table_booking = df['Has Table booking'].value_counts()['Yes']
restaurants_with_online_delivery = df['Has Online delivery'].value_counts()['Yes']

# Calculate the percentage
table_booking_percentage = (restaurants_with_table_booking / total_restaurants) * 100
online_delivery_percentage = (restaurants_with_online_delivery / total_restaurants) * 100

# Display the results
print(f"\nPercentage of Restaurants Offering Table Booking: {table_booking_percentage:.2f}%")
print(f"Percentage of Restaurants Offering Online Delivery: {online_delivery_percentage:.2f}%")

# Convert 'Aggregate rating' column to numeric
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

# Compare the average ratings
average_rating_with_table_booking = df[df['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
average_rating_without_table_booking = df[df['Has Table booking'] == 'No']['Aggregate rating'].mean()

# Display the results
print(f"Average Rating for Restaurants with Table Booking: {average_rating_with_table_booking:.2f}")
print(f"Average Rating for Restaurants without Table Booking: {average_rating_without_table_booking:.2f}")

# Explore the unique values in the 'Price range' and 'Has Online delivery' columns
unique_price_ranges = df['Price range'].unique()
unique_online_delivery = df['Has Online delivery'].unique()

# Display the unique values
print("Unique Price Ranges:", unique_price_ranges)
print("Unique Online Delivery Options:", unique_online_delivery)

# Analyze the availability of online delivery among restaurants with different price ranges
delivery_by_price_range = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack()

# Display the results
print("\nAvailability of Online Delivery Among Restaurants with Different Price Ranges:")
print(delivery_by_price_range)

# Determine the most common price range
most_common_price_range = df['Price range'].mode().iloc[0]

# Display the result
print("Most Common Price Range: ", most_common_price_range)

# Convert 'Aggregate rating' and 'Price range' columns to numeric
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')
df['Price range'] = pd.to_numeric(df['Price range'], errors='coerce')

# Calculate the average rating for each price range
average_rating_by_price_range = df.groupby('Price range')['Aggregate rating'].mean()

# Identify the color that represents the highest average rating
highest_avg_rating_color = 'green'  # Default color
if not average_rating_by_price_range.empty:
    highest_avg_rating_price_range = average_rating_by_price_range.idxmax()
    if pd.notnull(highest_avg_rating_price_range):
        highest_avg_rating_color = 'red'  # Change color to red for the highest average rating

# Display the average rating for each price range
print("Average Rating for Each Price Range:")
print(average_rating_by_price_range)

# Plot a bar chart with colors
plt.bar(average_rating_by_price_range.index, average_rating_by_price_range, color=[highest_avg_rating_color if x == highest_avg_rating_price_range else 'lightblue' for x in average_rating_by_price_range.index])
plt.xlabel('Price Range')
plt.ylabel('Average Rating')
plt.title('Average Rating for Each Price Range')
plt.show()

# Extract additional features
df['Restaurant Name Length'] = df['Restaurant Name'].apply(len)
df['Address Length'] = df['Address'].apply(len)

# Display the updated DataFrame with additional features
print("Updated DataFrame with Additional Features:")
print(df.head())

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_dataset.csv', index=False)

# Perform one-hot encoding for 'Has Table Booking' and 'Has Online Delivery'
df_encoded = pd.get_dummies(df, columns=['Has Table booking', 'Has Online delivery'], drop_first=True)

# Display the updated DataFrame with new features
print("Updated DataFrame with New Features:")
print(df_encoded.head())

# Save the updated DataFrame to a new CSV file
df_encoded.to_csv('encoded_dataset.csv', index=False)
