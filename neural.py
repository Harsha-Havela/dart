import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# =========================
# LOAD DATA (CIFAR-10)
# =========================
print("Loading data...")
data = fetch_openml('CIFAR_10_small')

X = data.data
y = data.target.astype(int)

# =========================
# Q1: DATASET INFO
# =========================
classes = ['airplane','automobile','bird','cat','deer',
           'dog','frog','horse','ship','truck']

print("Q1:")
print("Classes:", classes)
print("Total images:", X.shape[0], "\n")

# =========================
# VISUALIZE SAMPLE IMAGES
# =========================
plt.figure(figsize=(8,5))
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(X[i].reshape(32,32,3).astype(int))
    plt.title(classes[y[i]])
    plt.axis('off')
plt.show()

# =========================
# PREPROCESSING
# =========================
X = X / 255.0

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# =========================
# MODEL (MLP)
# =========================
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=20)
mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)

# =========================
# Q6: EVALUATION
# =========================
acc = accuracy_score(y_test, y_pred)

print("\nQ6:")
print("Test Accuracy:", acc, "\n")

# =========================
# Q5: HYPERPARAMETERS
# =========================
print("Q5:")
print("Learning rate → controls learning speed")
print("Batch size → affects training stability")
print("Epochs → more epochs = better learning but overfitting risk\n")

# =========================
# Q2: CNN VS FC
# =========================
print("Q2:")
print("CNN better for images due to spatial feature learning")
print("MLP uses flattened pixels → less effective\n")

# =========================
# Q3: RELU
# =========================
print("Q3:")
print("ReLU speeds up training and avoids vanishing gradient\n")

# =========================
# Q4: FORWARD & BACKPROP
# =========================
print("Q4:")
print("Forward → compute output")
print("Backprop → update weights using error\n")

# =========================
# Q7: VALIDATION VS TRAINING
# =========================
print("Q7:")
print("Validation accuracy shows generalization\n")

# =========================
# Q8: IMPROVEMENTS
# =========================
print("Q8:")
print("Use CNN, increase layers, use dropout, data augmentation")
