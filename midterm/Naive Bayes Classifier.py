import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import seaborn as sns

# Taking input for the number of data points and features
num_data_points = int(input("Enter the number of data points: "))
num_features = int(input("Enter the number of features: "))

# Generate random data for demonstration
np.random.seed(42)
X = np.random.rand(num_data_points, num_features)
y = (X.sum(axis=1) > num_features / 2).astype(int)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Naive Bayes classifier
clf = GaussianNB()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Plot decision boundary
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k', marker='o', s=100, label='Data Points')

# Plot decision boundary
if num_features == 2:  # Only plot decision boundary for 2D data
    xx, yy = np.meshgrid(np.linspace(0, 1.5, 100), np.linspace(0, 1.5, 100))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')

plt.title("Naive Bayes Classifier Decision Boundary")
plt.xlabel(f"Feature 1")
plt.ylabel(f"Feature 2" if num_features > 1 else "Target")
plt.legend()
plt.show()

