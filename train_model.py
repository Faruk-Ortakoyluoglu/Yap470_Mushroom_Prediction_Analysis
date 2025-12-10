import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# 1. Veriyi Oku
df = pd.read_csv('mushrooms_mini.csv')

# 2. X ve y Ayrımı (class sütunu hedefdir)
X = df.drop('class', axis=1)
y = df['class']

# y (Hedef) Dönüşümü: e -> 0, p -> 1 (app.py mantığına göre kontrol edilmeli)
# app.py'de result == '0' -> Yenebilir (Edible). Demek ki 'e' -> 0 olmalı.
# sklearn LabelEncoder alfabetik yapar: e -> 0, p -> 1. Bu doğrudur.
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# 3. One-Hot Encoding (app.py ile uyumlu olması için drop_first=True şart)
X_encoded = pd.get_dummies(X, drop_first=True)

# 4. Modeli Eğit
model = RandomForestClassifier()
model.fit(X_encoded, y)

# 5. Kaydet
joblib.dump(model, 'random_forest_model.pkl')
print("Model başarıyla yeniden eğitildi ve 'random_forest_model.pkl' olarak kaydedildi.")
