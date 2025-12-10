

# YAP470 – Mantar Analizi Projesi
----------------------------------------------------------
## 🍄 Mushroom Predictor – Live Demo
Streamlit app for predicting mushroom edibility using ML.

🔗 Live App: https://mushroom-predictor-ml.streamlit.app/
----------------------------------------------------------

Bu proje, mantar veri seti üzerinde veri analizi ve makine öğrenimi modelleri geliştirmek için hazırlanmış bir Jupyter Notebook projesidir. Proje; pandas, numpy, seaborn, matplotlib, plotly ve scikit-learn kütüphanelerini kullanır. Tüm çalışma izole bir virtual environment (venv) üzerinde gerçekleştirilir.

## Kurulum Adımları

### 1. Projeyi Klonla

```bash
git clone https://github.com/KULLANICI_ADI/yap470mantar.git
cd yap470mantar
```

---

### 2. Virtual Environment (venv) Oluştur

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Gereksinimleri Yükle

```bash
pip install -r requirements.txt
```

### 4. Jupyter Kernel’ini venv’e Tanıt

```bash
pip install ipykernel nbformat
python -m ipykernel install --user --name=y470env --display-name "YAP470 Mantar Env"
```

Bu işlem, notebook’un doğru Python ortamını kullanmasını sağlar.

---

### 5. Jupyter Notebook’u Aç

```bash
jupyter notebook
```

Notebook açıldığında kernel seçiminden:

Kernel → Change Kernel → “YAP470 Mantar Env”

seçilmelidir.

## Proje Yapısı

```
yap470mantar/
│
├── venv/                      # Sanal ortam (git tarafından takip edilmez)
├── mushrooms.csv              # Veri seti
├── analysis.ipynb             # Jupyter Notebook
├── requirements.txt           # Gereksinimler
└── README.md                  # Bu dosya
`

