# save_model.py
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import pickle

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)
model.fit(X, y)
pickle.dump(model, open("model.pkl", "wb"))

