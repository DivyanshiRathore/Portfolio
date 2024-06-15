Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import matplotlib.pyplot as plt
... import seaborn as sns
... import folium
... 
... 
... # Replace 'path_to_your_file.csv' with the actual path to your CSV file
... file_path = r'C:\Users\divya\Desktop\cognifyz\Dataset .csv'
... 
... # Read the CSV file into a pandas DataFrame
... df = pd.read_csv(file_path)
... 
... # Display the number of rows and columns
... num_rows, num_columns = df.shape
... print(f"Number of rows: {num_rows}")
... print(f"Number of columns: {num_columns}")
... 
... # Check for missing values
... missing_values = df.isnull().sum()
... 
... # Display the number of missing values in each column
... print("Missing Values in Each Column:")
... print(missing_values)
... 
... # Data type conversion (if necessary)
... # For example, if "Aggregate rating" is a string, convert it to a numeric type
... df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')
... 
... # Check data types after conversion
... print("Data types after conversion:")
... print(df.dtypes)
... 
... # Analyze the distribution of the target variable ("Aggregate rating")
... plt.figure(figsize=(10, 6))
... sns.histplot(df['Aggregate rating'], bins=20, kde=True)
... plt.title('Distribution of Aggregate Rating')
... plt.xlabel('Aggregate Rating')
... plt.ylabel('Frequency')
... plt.show()
... 
... # Identify class imbalances
class_counts = df['Aggregate rating'].value_counts()
print("\nClass distribution:")
print(class_counts)

# Select numerical columns
numerical_columns = df.select_dtypes(include=['number'])

# Display the descriptive statistics
statistics = numerical_columns.describe()

# Extract mean, median, and standard deviation from the statistics DataFrame
mean_values = statistics.loc['mean']
median_values = statistics.loc['50%']  # 50% corresponds to the median
std_dev_values = statistics.loc['std']

# Display the results
print("Mean values:")
print(mean_values)
print("\nMedian values:")
print(median_values)
print("\nStandard Deviation values:")
print(std_dev_values)

# Explore distribution of "Country Code"
country_counts = df['Country Code'].value_counts()
print("\nDistribution of Country Code:")
print(country_counts)

# Explore distribution of "City"
city_counts = df['City'].value_counts()
print("\nDistribution of City:")
print(city_counts)

# Explore distribution of "Cuisines"
# Note: Split cuisines strings and count each cuisine separately
cuisines = df['Cuisines'].str.split(',').explode().str.strip()
cuisine_counts = cuisines.value_counts()
print("\nDistribution of Cuisines:")
print(cuisine_counts)

# Identify top cuisines
top_cuisines = cuisine_counts.head(10)
print("\nTop Cuisines:")
print(top_cuisines)

# Identify top cities with the highest number of restaurants
top_cities = city_counts.head(10)
print("\nTop Cities with the Highest Number of Restaurants:")
print(top_cities)

# Visualize the distribution of cities
plt.figure(figsize=(12, 6))
sns.barplot(x=top_cities.index, y=top_cities.values)
plt.title('Top Cities with the Highest Number of Restaurants')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')
plt.show()


# Filter out rows with missing latitude or longitude information
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create a map centered around the first restaurant's location
map_restaurants = folium.Map(location=[df['Latitude'].iloc[0], df['Longitude'].iloc[0]], zoom_start=12)

# Add markers for each restaurant
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(map_restaurants)

# Save the map as an HTML file
map_restaurants.save('restaurant_map.html')


# Explore distribution of restaurants across cities
city_counts = df['City'].value_counts()

# Visualize distribution of restaurants across cities
plt.figure(figsize=(12, 6))
sns.barplot(x=city_counts.index, y=city_counts.values)
plt.title('Distribution of Restaurants Across Cities')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')
plt.show()

# Determine correlation between location and rating
correlation_matrix = df[['Latitude', 'Longitude', 'Aggregate rating']].corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix: Location vs. Rating')


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
