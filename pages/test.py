from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

data = pd.read_csv('/content/drive/MyDrive/MSIB Skilvul 2024/Tugas/Capstone Project/dataset/Credit Score Classification Dataset.csv')

# Display first few rows of the dataset | Menampilkan beberapa baris pertama dari dataset
print(data.head())
print('\n-------------\n')

# Display data types and info | Menampilkan tipe data dan info
print(data.info())
print('\n-------------\n')

# Describe the dataset | Deskripsi dataset
print(data.describe())

# Check for missing values | Memeriksa nilai yang hilang
print(data.isnull().sum())

# Visualize data distribution | Visualisasi distribusi data
sns.pairplot(data)
plt.show()

# Handle missing values | Menangani nilai yang hilang
numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = data.select_dtypes(include=['object']).columns

# Fill missing values in numeric columns with the mean | Mengisi nilai yang hilang pada kolom numerik dengan mean/rata-rata
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Fill missing values in categorical columns with the most frequent value |
# Mengisi nilai yang hilang pada kolom kategorikal dengan nilai yang paling sering muncul
for col in categorical_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Encode categorical variables | Encoding variabel kategorikal
le = LabelEncoder()
for column in categorical_cols:
    data[column] = le.fit_transform(data[column])

# Check the data after preprocessing | Memeriksa data setelah preprocessing
print(data.head())

# Visualize correlation matrix | Visualisasi matriks korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.show()

# Feature and target selection | Seleksi Fitur dan Target
X = data.drop('Credit Score', axis=1)
y = data['Credit Score']

# Encode target variable | Encode variabel target
y = le.fit_transform(y)

# Split the data | Membagi data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data | Standardisasi data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize models | Menginisialisasi model
log_reg = LogisticRegression()
random_forest = RandomForestClassifier()
xgb = XGBClassifier(learning_rate=0.001, n_estimators=100)
lgbm = LGBMClassifier(learning_rate=0.001, n_estimators=100)

# Train models | Melatih model
log_reg.fit(X_train, y_train)
random_forest.fit(X_train, y_train)
xgb.fit(X_train, y_train)
lgbm.fit(X_train, y_train)

# Predictions | Prediksi
y_pred_log_reg = log_reg.predict(X_test)
y_pred_random_forest = random_forest.predict(X_test)
y_pred_xgb = xgb.predict(X_test)
y_pred_lgbm = lgbm.predict(X_test)

print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_log_reg))
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_random_forest))
print("XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))
print("LGBM Accuracy:", accuracy_score(y_test, y_pred_lgbm))

# Classification reports | Laporan klasifikasi
print("Logistic Regression Report:\n", classification_report(y_test, y_pred_log_reg))
print("Random Forest Report:\n", classification_report(y_test, y_pred_random_forest))
print("XGBoost Report:\n", classification_report(y_test, y_pred_xgb))
print("LGBM Report:\n", classification_report(y_test, y_pred_lgbm))

# Confusion matrices | Matriks konfusi
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

sns.heatmap(confusion_matrix(y_test, y_pred_log_reg), annot=True, fmt='d', ax=ax[0,0])
ax[0,0].set_title('Logistic Regression')
sns.heatmap(confusion_matrix(y_test, y_pred_random_forest), annot=True, fmt='d', ax=ax[0,1])
ax[0,1].set_title('Random Forest')
sns.heatmap(confusion_matrix(y_test, y_pred_xgb), annot=True, fmt='d', ax=ax[1,0])
ax[1,0].set_title('XGBoost')
sns.heatmap(confusion_matrix(y_test, y_pred_lgbm), annot=True, fmt='d', ax=ax[1,1])
ax[1,1].set_title('LGBM')

plt.show()

# Save the selected models | Menyimpan model yang dipilih
model_path = '/content/drive/MyDrive/MSIB Skilvul 2024/Tugas/Capstone Project/'
joblib.dump(random_forest, model_path + 'random_forest_model.pkl')