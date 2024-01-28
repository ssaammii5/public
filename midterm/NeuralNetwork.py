import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Random----------
X = np.vstack([(np.random.rand(10, 2)*5),(np.random.rand(10, 2)*10)])
Y = np.hstack([[0]*10 , [1]*10])
dataset = pd.DataFrame(X, columns=["X1", "X2"])
dataset["Y"] =Y

print(dataset.head())

plt.plot(dataset,label='Inline label')
plt.legend(["X2","X1","Y"])
#--------------------

# # Load your dataset (replace "your_dataset.csv" with your actual dataset file)
# dataset = pd.read_csv("C:/Users/Sami/Downloads/data.csv")
#
# X = dataset[["Position", "Level"]].values
# Y = dataset["Salary"].values
#
# plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Spectral)
# plt.xlabel('X1')
# plt.ylabel('X2')
# plt.title('Scatter plot of the dataset')
# plt.show()

Z = np.zeros((len(Y), 2))
for i in range(len(Y)):
    Z[i, Y[i]] = 1

Wi_1 = np.random.randn(3, 2)
Bi_1 = np.random.randn(3)
Wi_2 = np.random.randn(2, 3)
Bi_2 = np.random.randn(2)

def forward_prop(X, Wi_1, Bi_1, Wi_2, Bi_2):
    M = 1 / (1 + np.exp(-(X.dot(Wi_1.T) + Bi_1)))
    A = M.dot(Wi_2.T) + Bi_2
    expA = np.exp(A)
    Y = expA / expA.sum(axis=1, keepdims=True)
    return Y, M

def diff_Wi_2(H, Z, Y):
    return H.T.dot(Z - Y)

def diff_Wi_1(X, H, Z, output, Wi_2):
    dZ = (Z - output).dot(Wi_2) * H * (1 - H)
    return X.T.dot(dZ)

def diff_B2(Z, Y):
    return (Z - Y).sum(axis=0)

def diff_B1(Z, Y, Wi_2, H):
    return ((Z - Y).dot(Wi_2) * H * (1 - H)).sum(axis=0)

learning_rate = 1e-3
for epoch in range(5000):
    output, hidden = forward_prop(X, Wi_1, Bi_1, Wi_2, Bi_2)
    Wi_2 += learning_rate * diff_Wi_2(hidden, Z, output).T
    Bi_2 += learning_rate * diff_B2(Z, output)
    Wi_1 += learning_rate * diff_Wi_1(X, hidden, Z, output, Wi_2).T
    Bi_1 += learning_rate * diff_B1(Z, output, Wi_2, hidden)

X_test = np.array([1, 1])

hidden_output = 1 / (1 + np.exp(-X_test.dot(Wi_1.T) - Bi_1))
outer_layer_output = hidden_output.dot(Wi_2.T) + Bi_2
expA = np.exp(outer_layer_output)
Y_test = expA / expA.sum()
print("Probability of class 0: {:.4f}\nProbability of class 1: {:.4f}".format(Y_test[0], Y_test[1]))
