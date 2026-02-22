import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

def train_model():
    if not os.path.exists("heart_disease.csv"):
        print("Dataset not found. Please run download_data.py first.")
        return

    df = pd.read_csv("heart_disease.csv")
    
    # Split features and target
    X = df.drop("target", axis=1)
    y = df["target"]
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    # Using RandomForest with some tuned parameters
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model
    with open("heart_disease_model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    print("Model saved to heart_disease_model.pkl")

if __name__ == "__main__":
    train_model()
