import pandas as pandas
import numpy as np
import kagglehub
from kagglehub import KaggleDatasetAdapter
from sklearn.tree import 


df = kagglehub.dataset_load(
    KaggleDatasetAdapter, PANDAS,
    "ucinl/iris"
    "Iris.csv"
)
print("First 5 records", df.head())

#DATA PREPRATION
X=df.drop(columns=["Id","Species"])
y=df["Species"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=42
)

#GINI INDEX
def gini_index(labels):
    classes, counts = np.unique(labels, return_counts=True)
    return 1- sum((count/len(labels))**2 for count in counts)

print("Gini Index:", gini_index(y))

#Train Decision Tree
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=1,
    random_state=42
)
model.fit(X_train, y_train)

#ACCURACY
print("Accuracy", model.score(X_test, y_test))

#VISUALIZE TREE
def_data = export_graphiz(
    model,
    out_file=None,
    feature_names=X.columns,
    class_names=model.classes,
    
)
