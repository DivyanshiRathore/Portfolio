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




# Display the number of rows and columns
num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# Check for missing values
missing_values = df.isnull().sum()

# Display the number of missing values in each column
print("Missing Values in Each Column:")
print(missing_values)

# Data type conversion (if necessary)
# For example, if "Aggregate rating" is a string, convert it to a numeric type
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

# Check data types after conversion
print("Data types after conversion:")
print(df.dtypes)

# Analyze the distribution of the target variable ("Aggregate rating")
plt.figure(figsize=(10, 6))
sns.histplot(df['Aggregate rating'], bins=20, kde=True)
plt.title('Distribution of Aggregate Rating')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.show()

# Identify class imbalances
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
