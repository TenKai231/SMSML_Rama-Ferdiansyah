import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(path):
    print(f"Membaca data dari: {path}")
    df = pd.read_csv(path)

    df_clean = df.copy()

    # Pisahkan kolom kategorikal dan numerik
    cat_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
    num_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()

    # Hapus kolom target dari list fitur numerik/kategorikal
    if 'Credit_Score' in num_cols:
        num_cols.remove('Credit_Score')
    if 'Credit_Score' in cat_cols:
        cat_cols.remove('Credit_Score')

    print("Memulai penanganan missing value...")
    # Imputasi numerik dengan median
    if len(num_cols) > 0:
        imputer_num = SimpleImputer(strategy='median')
        df_clean[num_cols] = imputer_num.fit_transform(df_clean[num_cols])

    # Imputasi kategorikal dengan modus (most_frequent)
    if len(cat_cols) > 0:
        imputer_cat = SimpleImputer(strategy='most_frequent')
        df_clean[cat_cols] = imputer_cat.fit_transform(df_clean[cat_cols])

    print("Memulai encoding fitur kategorikal dan target...")
    # Label Encoding untuk Target jika targetnya Object/String
    if 'Credit_Score' in df_clean.columns and df_clean['Credit_Score'].dtype == 'object':
        le_target = LabelEncoder()
        df_clean['Credit_Score'] = le_target.fit_transform(df_clean['Credit_Score'])

    # One-Hot Encoding untuk fitur kategorikal
    if len(cat_cols) > 0:
        df_clean = pd.get_dummies(df_clean, columns=cat_cols, drop_first=True)
        # Pastikan tipe data boolean dari dummy variable diubah menjadi numerik (1/0)
        dummy_cols = [c for c in df_clean.columns if c not in num_cols and c != 'Credit_Score']
        for col in dummy_cols:
            df_clean[col] = df_clean[col].astype(int)

    print("Memulai scaling fitur numerik...")
    # Standarisasi pada fitur numerik
    if len(num_cols) > 0:
        scaler = StandardScaler()
        df_clean[num_cols] = scaler.fit_transform(df_clean[num_cols])

    print(f"Preprocessing Selesai! Sisa nilai null: {df_clean.isnull().sum().sum()}")
    return df_clean

if __name__ == "__main__":
    import os

    # Dapatkan path dinamis ke folder tempat skrip ini berada
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Path dataset input yang bersifat absolut berdasarkan lokasi skrip
    input_path = os.path.join(current_dir, "..", "dataset_raw", "train_pca.csv")

    # Jalankan preprocessing pada data raw
    data_bersih = preprocess_data(input_path)

    # Simpan dataset hasil bersih (disimpan ke folder tempat skrip ini berada)
    output_path = os.path.join(current_dir, "dataset_clean.csv")
    data_bersih.to_csv(output_path, index=False)

    print(f"Data bersih berhasil disimpan di: {output_path}")