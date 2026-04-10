import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# =========================
# DATA
# =========================
X = np.array([[2,2],[4,4],[4,0],[0,0],[1,1],[0,4]])
y = np.array([1,1,1,-1,-1,-1])

# =========================
# LINEAR SVM
# =========================
lin = SVC(kernel='linear')
lin.fit(X, y)

pred1 = lin.predict(X)
acc1 = accuracy_score(y, pred1)
sv1 = len(lin.support_)

# =========================
# POLYNOMIAL SVM
# =========================
poly2 = SVC(kernel='poly', degree=2)
poly2.fit(X, y)

pred2 = poly2.predict(X)
acc2 = accuracy_score(y, pred2)
sv2 = len(poly2.support_)

poly3 = SVC(kernel='poly', degree=3)
poly3.fit(X, y)

pred3 = poly3.predict(X)
acc3 = accuracy_score(y, pred3)
sv3 = len(poly3.support_)

# =========================
# RBF SVM
# =========================
rbf1 = SVC(kernel='rbf', gamma=0.1)
rbf1.fit(X, y)

pred4 = rbf1.predict(X)
acc4 = accuracy_score(y, pred4)
sv4 = len(rbf1.support_)

rbf2 = SVC(kernel='rbf', gamma=1)
rbf2.fit(X, y)

pred5 = rbf2.predict(X)
acc5 = accuracy_score(y, pred5)
sv5 = len(rbf2.support_)

# =========================
# RESULT TABLE
# =========================
res = pd.DataFrame({
    "Kernel": ["Linear", "Poly2", "Poly3", "RBF(0.1)", "RBF(1)"],
    "Accuracy": [acc1, acc2, acc3, acc4, acc5],
    "Support Vectors": [sv1, sv2, sv3, sv4, sv5]
})

print(res)
