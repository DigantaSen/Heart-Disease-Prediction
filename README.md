# ❤️ Heart Disease Prediction App

A machine learning web application that predicts the risk of heart disease based on various health parameters using Logistic Regression.

## 🌐 Live Demo

**Try the app here:** [https://heart-disease-prediction-bydiganta.streamlit.app/](https://heart-disease-prediction-bydiganta.streamlit.app/)

## 🎯 Overview

This application uses a trained Logistic Regression model to predict whether a person has a high or low risk of heart disease. The model is deployed using Streamlit, providing an interactive and user-friendly interface for real-time predictions.

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Real-time Predictions**: Instant heart disease risk assessment
- **Multiple Health Parameters**: Considers 11 different health indicators
- **Pre-trained Model**: Uses a saved Logistic Regression model with standardized inputs
- **Visual Feedback**: Clear risk indication with color-coded results

## 📊 Model Details

- **Algorithm**: Logistic Regression
- **Preprocessing**: StandardScaler for feature normalization
- **Model Files**:
  - `logistic_regression_heart.pkl` - Trained model
  - `scaler.pkl` - Feature scaler
  - `columns.pkl` - Expected feature columns

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd HeartDisease
```

2. **Create a virtual environment (recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. **Run the application**
```bash
streamlit run app.py
```

2. **Open your browser** and navigate to the local URL (typically `http://localhost:8501`)

3. **Input patient data** using the interactive controls:
   - Age (18-100 years)
   - Sex (Male/Female)
   - Chest Pain Type
   - Resting Blood Pressure
   - Cholesterol Level
   - Fasting Blood Sugar
   - Resting ECG
   - Maximum Heart Rate
   - Exercise Induced Angina
   - Oldpeak (ST depression)
   - ST Slope

4. **Click "Predict"** to get the heart disease risk assessment

## 📋 Input Parameters

| Parameter | Description | Range/Options |
|-----------|-------------|---------------|
| **Age** | Patient's age in years | 18-100 |
| **Sex** | Biological sex | Male, Female |
| **Chest Pain Type** | Type of chest pain experienced | ATA, NAP, TA, ASY |
| **Resting BP** | Resting blood pressure (mm Hg) | 80-200 |
| **Cholesterol** | Serum cholesterol (mg/dl) | 100-600 |
| **Fasting BS** | Fasting blood sugar > 120 mg/dl | Yes, No |
| **Resting ECG** | Resting electrocardiogram results | Normal, ST, LVH |
| **Max HR** | Maximum heart rate achieved | 60-220 |
| **Exercise Angina** | Exercise induced angina | Yes, No |
| **Oldpeak** | ST depression induced by exercise | 0.0-10.0 |
| **ST Slope** | Slope of peak exercise ST segment | Up, Flat, Down |

## 🔍 How It Works

1. **Data Collection**: User inputs health parameters through the Streamlit interface
2. **Feature Engineering**: The app creates one-hot encoded features and categorical bins for blood pressure and cholesterol levels
3. **Preprocessing**: Input features are standardized using the pre-trained scaler
4. **Prediction**: The Logistic Regression model predicts the risk (0 = Low Risk, 1 = High Risk)
5. **Result Display**: Color-coded output showing the prediction result

### Feature Engineering Details

The application performs the following transformations:
- One-hot encoding for categorical variables (Sex, Chest Pain Type, ECG, etc.)
- Blood pressure categorization (Hypertension stages)
- Cholesterol level categorization (Normal, Borderline High, High)
- Standardization of numerical features

## 📁 Project Structure

```
HeartDisease/
│
├── app.py                              # Streamlit application
├── logistic_regression_heart.pkl       # Trained model
├── scaler.pkl                          # Feature scaler
├── columns.pkl                         # Expected columns
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

## 🎓 Model Training

The model was trained on a heart disease dataset with the following steps:
1. Data preprocessing and cleaning
2. Feature engineering (one-hot encoding, binning)
3. Train-test split
4. Feature scaling using StandardScaler
5. Logistic Regression model training
6. Model evaluation and validation

## ⚠️ Disclaimer

**Important**: This application is for educational and informational purposes only. It should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation
- **Scikit-learn**: Machine learning library
- **Joblib**: Model serialization

## 👨‍💻 Author

**Diganta**

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📞 Support

For questions or support, please open an issue in the repository.

---

**Note**: Make sure all required model files (`logistic_regression_heart.pkl`, `scaler.pkl`, `columns.pkl`) are present in the same directory as `app.py` before running the application.
