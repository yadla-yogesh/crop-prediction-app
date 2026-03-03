# 🌾 Smart Crop Recommendation System

An AI-powered web application that predicts the most suitable crop based on soil nutrients and environmental conditions.

🔗 **Live Demo:** [https://YOUR-RENDER-LINK.onrender.com](https://crop-prediction-app-d8yd.onrender.com/)

---

## 🚀 Project Overview

This project uses Machine Learning to recommend the best crop based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

The system was trained on an agricultural dataset and deployed as a live web application using Flask.

---

## 🧠 Machine Learning Models Used

- Random Forest
- XGBoost
- LightGBM
- Ensemble Voting Classifier (Final Model)

The final deployed model uses **Soft Voting Ensemble**, achieving ~97% accuracy.

---

## 📊 Features

- 🌱 Crop prediction with confidence score
- 🌙 Dark mode support
- 💻 Responsive UI
- 🚀 Live deployment on Render
- 🧠 Ensemble ML model
- 🔁 Post-Redirect-Get pattern for clean form handling

---

## 🏗 Tech Stack

**Backend**
- Python
- Flask
- Scikit-learn
- XGBoost
- LightGBM

**Frontend**
- HTML
- CSS
- Bootstrap
- JavaScript

**Deployment**
- Render
- GitHub

---

## 📂 Project Structure
crop_prediction/
│
├── app.py
├── crop_model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── requirements.txt
├── runtime.txt
└── templates/
└── index.htm

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/crop-prediction-app.git
cd crop-prediction-app
pip install -r requirements.txt
python app.py

## Then open:

http://127.0.0.1:5000

## 📈 Model Training Workflow

1. Data preprocessing (Label Encoding + StandardScaler)
2. Train/Test split (80/20)
3. Train Random Forest, XGBoost, and LightGBM
4. Combine using Soft Voting Ensemble
5. Save model using joblib
6. Deploy using Gunicorn on Render

---

## 🌍 Future Improvements

- Add top-3 crop predictions  
- Add feature importance visualization  
- Add crop information display  
- Dockerize application  
- Deploy on AWS/GCP  

---

## 👨‍💻 Author

Developed as part of a Machine Learning academic project.

---

⭐ If you found this project useful, feel free to star the repository!
