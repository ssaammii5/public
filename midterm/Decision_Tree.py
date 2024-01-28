import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# Load data from CSV file
# Replace 'your_dataset.csv' with the actual path to your CSV file
df = pd.read_csv('C:/Users/Sami/Downloads/zzz.csv')

# Convert categorical columns to numerical using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['outlook', 'temp', 'humidty'])

# Separate features (X) and target variable (y)
X = df_encoded.drop('play', axis=1)
y = df_encoded['play']

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the dataset
clf.fit(X, y)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=clf.classes_, filled=True, rounded=True, fontsize=10)
plt.show()
