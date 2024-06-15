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

#Task 3
# Assuming you have selected relevant features for prediction
# For example, let's consider features like 'Average Cost for two', 'Votes', 'Price range', etc.
selected_features = ['Average Cost for two', 'Votes', 'Price range']

# Extract features and target variable
X = df[selected_features]
y = df['Aggregate rating']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build a Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Predict on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display the evaluation metrics
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R-squared (R2): {r2:.2f}')

# Build and evaluate Linear Regression model
linear_reg_model = LinearRegression()
linear_reg_model.fit(X_train, y_train)
y_pred_linear_reg = linear_reg_model.predict(X_test)

# Build and evaluate Decision Tree model
decision_tree_model = DecisionTreeRegressor(random_state=42)
decision_tree_model.fit(X_train, y_train)
y_pred_decision_tree = decision_tree_model.predict(X_test)

# Build and evaluate Random Forest model
random_forest_model = RandomForestRegressor(random_state=42)
random_forest_model.fit(X_train, y_train)
y_pred_random_forest = random_forest_model.predict(X_test)

# Evaluate models
def evaluate_model(name, y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f'{name} - Mean Squared Error (MSE): {mse:.2f}, R-squared (R2): {r2:.2f}')

evaluate_model('Linear Regression', y_test, y_pred_linear_reg)
evaluate_model('Decision Tree', y_test, y_pred_decision_tree)
evaluate_model('Random Forest', y_test, y_pred_random_forest)

# Assuming you have a 'Cuisines' column and an 'Aggregate rating' column
# If your 'Cuisines' column contains multiple cuisines separated by commas, you may need to preprocess it.

# Plot a violin plot to visualize the distribution of ratings for each type of cuisine
plt.figure(figsize=(16, 8))
sns.violinplot(x='Cuisines', y='Aggregate rating', data=df)
plt.xticks(rotation=90)
plt.title('Relationship between Cuisine and Restaurant Rating')
plt.xlabel('Cuisine Type')
plt.ylabel('Aggregate Rating')
plt.show()

# Extracting cuisines and their corresponding votes
cuisine_votes = df.groupby('Cuisines')['Votes'].sum().reset_index()

# Sorting cuisines based on the total number of votes in descending order
popular_cuisines = cuisine_votes.sort_values(by='Votes', ascending=False)

# Display the most popular cuisines
print("Most Popular Cuisines Based on Votes:")
print(popular_cuisines.head())

# Create a boxplot to visualize the distribution of ratings for each cuisine
plt.figure(figsize=(16, 8))
sns.boxplot(x='Cuisines', y='Aggregate rating', data=df)
plt.xticks(rotation=90)
plt.title('Distribution of Ratings for Each Cuisine')
plt.xlabel('Cuisine Type')
plt.ylabel('Aggregate Rating')
plt.show()

#Histogram
# Assuming you have an 'Aggregate rating' column
plt.figure(figsize=(10, 6))
sns.histplot(df['Aggregate rating'], bins=30, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.show()

#Bar plot
# Assuming you have an 'Aggregate rating' column
plt.figure(figsize=(10, 6))
sns.countplot(x='Aggregate rating', data=df, hue='Aggregate rating', palette='viridis', dodge=False, legend=False)
plt.title('Distribution of Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Count')
plt.show()

#Bar Plot for Cuisines
# Assuming you have 'Cuisines' and 'Aggregate rating' columns
plt.figure(figsize=(14, 8))
sns.barplot(x='Cuisines', y='Aggregate rating', data=df, err_kws={'linewidth': 0}, palette='viridis', hue='Cuisines', dodge=False, legend=False)
plt.title('Average Ratings for Different Cuisines')
plt.xlabel('Cuisine Type')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.show()

#Bar Plot for Cities
# Assuming you have 'City' and 'Aggregate rating' columns
plt.figure(figsize=(12, 6))
sns.barplot(x='City', y='Aggregate rating', data=df, errorbar=None, palette='viridis', hue='City', dodge=False, legend=False)
plt.title('Average Ratings for Different Cities')
plt.xlabel('City')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Aggregate rating', y='Rating color', data=df, alpha=0.7)
plt.title('Scatter Plot: Relationship between Aggregate rating and Rating color')
plt.xlabel('Aggregate rating')
plt.ylabel('Rating color')
plt.show()

# Pairplot for multiple features against the target
selected_features = ['Aggregate rating', 'Rating color']
sns.pairplot(df[selected_features], height=2)
plt.suptitle('Pairplot of Aggregate rating against Rating color', y=1.02)
plt.show()
