
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Veri setlerinin dosya yolları
attack_free_path = "C:/Users/sudea/CANintrusionDetection/Attack_free_dataset.txt"
dos_attack_path = "C:/Users/sudea/CANintrusionDetection/DoS_attack_dataset.txt"
fuzzy_attack_path = "C:/Users/sudea/CANintrusionDetection/Fuzzy_attack_dataset.txt"
impersonation_attack_path = "C:/Users/sudea/CANintrusionDetection/Impersonation_attack_dataset.txt"

# Dosyaları okuma
df_attack_free = pd.read_csv(attack_free_path, sep="\s+", header=None, 
                             names=["Timestamp", "ID", "DLC", "Data1", "Data2", "Data3", "Data4", "Data5", "Data6", "Data7", "Data8"],
                                on_bad_lines='skip')  # Hatalı satırları atla
df_dos_attack = pd.read_csv(dos_attack_path, sep="\s+", header=None, 
                            names=["Timestamp", "ID", "DLC", "Data1", "Data2", "Data3", "Data4", "Data5", "Data6", "Data7", "Data8"],
                                on_bad_lines='skip')
df_fuzzy_attack = pd.read_csv(fuzzy_attack_path, sep="\s+", header=None,
                               names=["Timestamp", "ID", "DLC", "Data1", "Data2", "Data3", "Data4", "Data5", "Data6", "Data7", "Data8"],
                                on_bad_lines='skip') 
df_impersonation_attack = pd.read_csv(impersonation_attack_path, sep="\s+", header=None, 
                                      names=["Timestamp", "ID", "DLC", "Data1", "Data2", "Data3", "Data4", "Data5", "Data6", "Data7", "Data8"],
                               on_bad_lines='skip') 


# Etiketleme: 0 = Attack Free, 1 = DoS, 2 = Fuzzy, 3 = Impersonation
df_attack_free["Label"] = 0
df_dos_attack["Label"] = 1
df_fuzzy_attack["Label"] = 2
df_impersonation_attack["Label"] = 3

# Verileri birleştirme
df_all = pd.concat([df_attack_free, df_dos_attack, df_fuzzy_attack, df_impersonation_attack], ignore_index=True)


print("Veri Setinin İlk 5 Satırı:")
print(df_all.head())
