import pickle
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

def load_data():
    # oading the wine quality dataset from OpenML
    data = fetch_openml(name='wine-quality-red', version=1)
    X = data.data
    y = data.target.astype(float)
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model():
    X_train, _, y_train, _ = load_data()

    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)

    with open("wine_model.pkl", "wb") as f:
        pickle.dump(model, f)

def get_model():
    with open("wine_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def predict(model, features):\
    return model.predict([features])
