import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import os

# Set tracking URI ke local directory agar tidak perlu menjalankan server terpisah
tracking_uri = "file://" + os.path.abspath("mlruns")
mlflow.set_tracking_uri(tracking_uri)

# Create a new MLflow Experiment
mlflow.set_experiment("Latihan Credit Scoring Optimization")

data = pd.read_csv("train_pca.csv")

X_train, X_test, y_train, y_test = train_test_split(
    data.drop("Credit_Score", axis=1),
    data["Credit_Score"],
    random_state=42,
    test_size=0.2
)

# Definisikan input_example untuk log_model (sebelumnya belum didefinisikan)
input_example = X_train[0:5]

# Mendefinisikan Metode Grid Search sederhana
n_estimators_range = np.linspace(10, 200, 3, dtype=int)  # Dikurangi jangkauannya agar lebih cepat
max_depth_range = np.linspace(1, 20, 3, dtype=int)      # Dikurangi jangkauannya agar lebih cepat

best_accuracy = 0
best_params = {}

# Pindahkan autolog ke luar loop agar lebih efisien
mlflow.autolog()

print("Memulai optimasi model...")

for n_estimators in n_estimators_range:
    for max_depth in max_depth_range:
        # Gunakan nested=True jika ingin run ini berada di bawah run utama,
        # tapi di sini kita buat run terpisah untuk tiap kombinasi hyperparameter
        with mlflow.start_run(run_name=f"rf_n{n_estimators}_d{max_depth}"):
            # Train model
            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
            model.fit(X_train, y_train)

            # Evaluate model
            accuracy = model.score(X_test, y_test)
            mlflow.log_metric("accuracy", accuracy)

            print(f"Run: n_estimators={n_estimators}, max_depth={max_depth} -> Accuracy: {accuracy:.4f}")

            # Save the best model
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_params = {"n_estimators": n_estimators, "max_depth": max_depth}

                # Log model terbaik
                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path="best_model",
                    input_example=input_example
                )

print("-" * 30)
print(f"Optimasi Selesai!")
print(f"Best Accuracy: {best_accuracy:.4f}")
print(f"Best Params: {best_params}")
