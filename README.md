# 🏡 California Housing Price Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Completed-success)

A complete **Machine Learning project** that predicts **California housing prices** based on the 1990 Census dataset.  
The project includes data analysis, feature engineering, model training, evaluation, and a **Streamlit web app** for real-time predictions.

---

## 🚀 Features
✅ End-to-end ML pipeline (data preprocessing → model training → evaluation)  
✅ Model comparison: Linear Regression, Random Forest, Gradient Boosting  
✅ Best model automatically saved as `model_pipeline.joblib`  
✅ `Streamlit` web app interface for predictions  
✅ Clean and well-documented Jupyter Notebook  

---

## 🧩 Project Structure
```
📂 housing-price-prediction/
│
├── Housing_Price_Prediction.ipynb      # Main analysis & model training notebook
├── app.py                              # Streamlit web app for predictions
├── housing.csv                         # Dataset (California Housing)
├── model_pipeline.joblib               # Saved trained model
├── preprocessing_pipeline.joblib       # Data preprocessing pipeline
├── requirements.txt                    # Dependencies list
└── README.md                           # Project documentation
```

---

## 🧠 Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python |
| **Data Handling** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Machine Learning** | scikit-learn |
| **Model Saving** | joblib |
| **Web App** | Streamlit |

---

## ⚙️ How to Run the Project

### 🔹 Step 1: Clone the repository
```bash
git clone https://github.com/WaqasGurmani/housing-price-prediction.git
cd housing-price-prediction
```

### 🔹 Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Run the Streamlit App
```bash
streamlit run app.py
```

Then open your browser and go to:  
👉 **http://localhost:8501**

---

## 📊 Model Performance

| Model | RMSE | R² Score |
|--------|------|----------|
| Linear Regression | ~68000 | 0.64 |
| Random Forest | ~51000 | 0.83 |
| Gradient Boosting | ~49500 | 0.85 |

*(Values may vary slightly depending on random seed and preprocessing.)*

---

## 🧮 Sample Prediction Inputs
| Feature | Example Value |
|----------|----------------|
| Median Income | 3.2 |
| Median Age | 25.0 |
| Total Rooms | 2500 |
| Total Bedrooms | 400 |
| Population | 800 |
| Households | 350 |
| Latitude | 34.25 |
| Longitude | -118.45 |
| Ocean Proximity | NEAR BAY |

---

## 🧠 Insights & Observations
- Income and location have the highest correlation with median house value.  
- Outlier removal and scaling significantly improved model accuracy.  
- Random Forest and Gradient Boosting outperformed Linear Regression.  

---

## 💾 Model Artifacts
- `model_pipeline.joblib` → trained ML model  
- `preprocessing_pipeline.joblib` → feature transformer (for new data)

---
## 🧠 Download Trained Model  
Trained model file (`best_model.joblib`) is too large for GitHub upload.  
You can download it here: [Download the model](https://drive.google.com/file/d/1UcgzZI_GY7VNFpEhJpZSPiJcxVwCIXxT/view?usp=drive_link)


## 👨‍💻 Author
**Waqas Gurmani**  
📧 [waqasgurmani364@gmail.com]  
🌐 [Your GitHub Profile](https://github.com/waqasgurmani)

---

## 🪪 License
This project is licensed under the **MIT License** — feel free to use and modify it for learning or portfolio purposes.



