import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

attack_free_path = "C:/Users/sudea/CANintrusionDetection/Attack_free_dataset.txt"
dos_attack_path = "C:/Users/sudea/CANintrusionDetection/DoS_attack_dataset.txt"
fuzzy_attack_path = "C:/Users/sudea/CANintrusionDetection/Fuzzy_attack_dataset.txt"
impersonation_attack_path = "C:/Users/sudea/CANintrusionDetection/Impersonation_attack_dataset.txt"

column_names = ["Timestamp", "ID", "DLC", "Data1", "Data2", "Data3", "Data4", "Data5", "Data6", "Data7", "Data8"]

df_attack_free = pd.read_csv(attack_free_path, sep="\s+", header=None, names=column_names, on_bad_lines='skip')
df_dos_attack = pd.read_csv(dos_attack_path, sep="\s+", header=None, names=column_names, on_bad_lines='skip')
df_fuzzy_attack = pd.read_csv(fuzzy_attack_path, sep="\s+", header=None, names=column_names, on_bad_lines='skip')
df_impersonation_attack = pd.read_csv(impersonation_attack_path, sep="\s+", header=None, names=column_names, on_bad_lines='skip')

#  0 = Attack Free, 1 = DoS, 2 = Fuzzy, 3 = Impersonation
df_attack_free["Label"] = 0
df_dos_attack["Label"] = 1
df_fuzzy_attack["Label"] = 2
df_impersonation_attack["Label"] = 3

# birleştir
df_all = pd.concat([df_attack_free, df_dos_attack, df_fuzzy_attack, df_impersonation_attack], ignore_index=True)

# Eksik verileri doldurma
df_all.fillna(0, inplace=True)

# Geçersiz 'ID' verilerini temizleme ve sadece geçerli hexadecimal ID'leri dönüştürme
df_all["ID"] = df_all["ID"].apply(lambda x: int(x, 16) if isinstance(x, str) and x != 'DLC:' and all(c in '0123456789abcdefABCDEF' for c in x) else x)

# Sayısal olmayan sütunları çıkarma - Timestamp ve DLC 
df_all_cleaned = df_all.drop(columns=["Timestamp", "DLC"])

# Özellikler ve etiketlerin ayrılması
features = df_all_cleaned.drop(columns=["Label"]) 
labels = df_all_cleaned["Label"] 

# **Sayısal olmayan verileri temizleme:** Özellikler üzerinde sayısal olmayan değerleri temizle
features = features.apply(pd.to_numeric, errors='coerce')

# Verileri ölçeklendirme
scaler = StandardScaler()

# **Nan değerlerini temizleme:** Sayısal olmayan değerleri 'NaN' olarak işaretlediğimiz için bunları 0 ile dolduruyoruz
features.fillna(0, inplace=True)

# Veriyi eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# KNN 
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Test seti ile tahmin 
y_pred = knn.predict(X_test)

# Sonuçlar
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))



