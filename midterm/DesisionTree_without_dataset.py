import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# Sample data
data = {
    'outlook': ['rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'sunny', 'rainy', 'overcast', 'overcast', 'sunny'],
    'temp': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'humidity': ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high'],
    'windy': [False, True, False, False, False, True, True, False, False, False, True, True, False, True],
    'play': ['NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'YES', 'NO']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert categorical columns to numerical using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['outlook', 'temp', 'humidity'])

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
