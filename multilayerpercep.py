import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# =========================
# LOAD DATA
# =========================
digits = load_digits()
X = digits.data
y = digits.target

# =========================
# Q1: FEATURES
# =========================
print("Q1:")
print("No. of features:", X.shape[1])
print("Each feature represents a pixel (8x8 image → 64 pixels)\n")

# =========================
# SPLIT DATA
# =========================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# =========================
# Q3: WITH SCALING
# =========================
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

mlp_scaled = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)
mlp_scaled.fit(X_train_s, y_train)

pred_scaled = mlp_scaled.predict(X_test_s)
acc_scaled = accuracy_score(y_test, pred_scaled)

# WITHOUT SCALING
mlp_no = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)
mlp_no.fit(X_train, y_train)

pred_no = mlp_no.predict(X_test)
acc_no = accuracy_score(y_test, pred_no)

print("Q3:")
print("Accuracy WITH scaling:", acc_scaled)
print("Accuracy WITHOUT scaling:", acc_no, "\n")

# =========================
# Q4: HIDDEN LAYERS EFFECT
# =========================
mlp1 = MLPClassifier(hidden_layer_sizes=(50,), max_iter=500)
mlp2 = MLPClassifier(hidden_layer_sizes=(100,100), max_iter=500)

mlp1.fit(X_train_s, y_train)
mlp2.fit(X_train_s, y_train)

acc1 = accuracy_score(y_test, mlp1.predict(X_test_s))
acc2 = accuracy_score(y_test, mlp2.predict(X_test_s))

print("Q4:")
print("1 Hidden Layer Accuracy:", acc1)
print("2 Hidden Layers Accuracy:", acc2)
print("More layers → more learning capacity but higher overfitting risk\n")

# =========================
# Q5: ACCURACY
# =========================
print("Q5:")
print("Overall Accuracy:", acc_scaled, "\n")

# =========================
# Q6: CONFUSION MATRIX
# =========================
cm = confusion_matrix(y_test, pred_scaled)
print("Q6: Confusion Matrix:\n", cm)


# =========================
# Q7: VISUALIZE MISCLASSIFIED
# =========================
mis_idx = np.where(y_test != pred_scaled)[0]

plt.figure(figsize=(8,5))
for i, idx in enumerate(mis_idx[:6]):
    plt.subplot(2,3,i+1)
    plt.imshow(X_test[idx].reshape(8,8), cmap='gray')
    plt.title(f"A:{y_test[idx]} P:{pred_scaled[idx]}")
    plt.axis('off')
plt.show()

# =========================
# Q2 & Q8 (PRINT ANSWERS)
# =========================
print("Q2:")
print("Similar digits: 3-5, 5-9, 1-7 → causes confusion\n")

print("Q8:")
print("MLP performs better because it learns complex non-linear patterns in pixel data")
