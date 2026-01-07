import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Initialize and train the Random Forest model
# We use a fixed random_state for reproducibility
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# 3. Save the model and the class names
# We save the class names (Setosa, Versicolor, Virginica) to map predictions later
joblib.dump(clf, 'iris_model.pkl')
joblib.dump(iris.target_names, 'iris_class_names.pkl')

print("Model trained and saved as 'iris_model.pkl'")
print("Class names saved as 'iris_class_names.pkl'")