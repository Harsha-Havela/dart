import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score

# =========================
# LOAD DATA
# =========================
data = load_breast_cancer()
X = data.data
y = data.target

print("Q1:")
print("Feature types: Numeric")
print("Class distribution:", np.bincount(y), "\n")

# =========================
# SPLIT DATA
# =========================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# =========================
# BASE MODEL (DECISION TREE)
# =========================
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

pred_dt = dt.predict(X_test)

print("Q2: Decision Tree")
print("Accuracy:", accuracy_score(y_test, pred_dt))
print("Precision:", precision_score(y_test, pred_dt))
print("Recall:", recall_score(y_test, pred_dt))
print("F1:", f1_score(y_test, pred_dt), "\n")

# =========================
# BAGGING (RANDOM FOREST)
# =========================
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

print("Q3: Random Forest")
print("Accuracy:", accuracy_score(y_test, pred_rf))

# FEATURE IMPORTANCE
plt.bar(range(len(rf.feature_importances_)), rf.feature_importances_)
plt.title("Feature Importance")
plt.show()

# =========================
# BOOSTING
# =========================
ada = AdaBoostClassifier(n_estimators=50)
gb = GradientBoostingClassifier(n_estimators=50)

ada.fit(X_train, y_train)
gb.fit(X_train, y_train)

print("\nQ4: Boosting")
print("AdaBoost Acc:", accuracy_score(y_test, ada.predict(X_test)))
print("GradientBoost Acc:", accuracy_score(y_test, gb.predict(X_test)), "\n")

# =========================
# VOTING
# =========================
hard = VotingClassifier(
    estimators=[('dt',dt),('rf',rf),('gb',gb)],
    voting='hard'
)

soft = VotingClassifier(
    estimators=[('dt',dt),('rf',rf),('gb',gb)],
    voting='soft'
)

hard.fit(X_train, y_train)
soft.fit(X_train, y_train)

print("Q5: Voting")
print("Hard Voting Acc:", accuracy_score(y_test, hard.predict(X_test)))
print("Soft Voting Acc:", accuracy_score(y_test, soft.predict(X_test)), "\n")

# =========================
# COMPARISON (ROC + CM)
# =========================
print("Q6:")
models = {"DT":dt, "RF":rf, "GB":gb}

for name, m in models.items():
    pred = m.predict(X_test)
    prob = m.predict_proba(X_test)[:,1]
    
    print(name, "Acc:", accuracy_score(y_test, pred),
          "ROC-AUC:", roc_auc_score(y_test, prob))
    
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred), "\n")

# =========================
# OVERFITTING CHECK
# =========================
print("Q7:")
print("DT Train Acc:", accuracy_score(y_train, dt.predict(X_train)))
print("DT Test Acc:", accuracy_score(y_test, dt.predict(X_test)))
print("RF reduces overfitting using multiple trees\n")

# =========================
# INTERPRETABILITY
# =========================
print("Q8:")
print("Decision Tree is interpretable")
print("Ensemble models are less interpretable but more accurate\n")

# =========================
# N_ESTIMATORS EFFECT
# =========================
print("Q9:")
for n in [10,50,100]:
    rf_temp = RandomForestClassifier(n_estimators=n)
    rf_temp.fit(X_train, y_train)
    print("Estimators:", n, "Accuracy:", accuracy_score(y_test, rf_temp.predict(X_test)))

print()

# =========================
# FINAL ENSEMBLE
# =========================
final = VotingClassifier(
    estimators=[('rf',rf),('gb',gb),('ada',ada)],
    voting='soft'
)

final.fit(X_train, y_train)

print("Q10:")
print("Final Ensemble Accuracy:", accuracy_score(y_test, final.predict(X_test)))
