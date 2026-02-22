import pandas as pd
import requests
import io

def download_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
    columns = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", 
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
    ]
    
    print(f"Downloading data from {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        # Load the data, handle '?' as NaN
        df = pd.read_csv(io.StringIO(response.text), header=None, names=columns, na_values="?")
        
        # Basic cleaning: drop rows with missing values (usually ca and thal have a few)
        df = df.dropna()
        
        # Convert target to binary (0 = no disease, 1-4 = disease)
        df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)
        
        # Save to csv
        df.to_csv("heart_disease.csv", index=False)
        print("Data downloaded and saved to heart_disease.csv")
        return df
    else:
        print("Failed to download data.")
        return None

if __name__ == "__main__":
    download_data()
