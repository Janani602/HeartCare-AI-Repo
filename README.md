# ❤️ HeartCare AI: Advanced Cardiovascular Intelligence

This project is a premium machine learning application designed for clinical decision support and predictive analytics in cardiovascular health.

## 🌟 Advanced Features

1.  **🧠 Intelligent Diagnosis & Decision Support**: Leverages Explainable AI (SHAP) to interpret model decisions and provide clinical reasoning for each prediction.
2.  **📈 Predictive Analytics**: Advanced data trends, population comparisons, and 10-year risk estimation with interactive "What-if" scenario modeling.
3.  **💊 Personalized Treatment Recommendations**: Dynamic clinical pathways suggesting lifestyle optimizations, dietary adjustments, and medication reviews based on biometric markers.
4.  **💬 HeartBot AI Assistant**: Integrated conversational agent providing instant answers to health queries based on the patient's specific profile.
5.  **🔎 Automated Data Interpretation**: Real-time analysis of clinical markers like ST-depression and blood pressure with automated medical alerts.
6.  **📊 Operational Efficiency & Workflow**: Single-click generation of professional medical reports in PDF format for clinical documentation and physician review.
7.  **📅 Personalized Alerts & Follow-Ups**: AI-driven follow-up scheduling based on the calculated risk level.

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare Data
Download and clean the UCI dataset:
```bash
python download_data.py
```

### 3. Train Model
Train the Random Forest model and save it:
```bash
python train_model.py
```

### 4. Launch Application
Start the premium Streamlit dashboard:
```bash
streamlit run app.py
```

## 📊 Feature Reference
| Feature | Description |
| :--- | :--- |
| **Age** | Patient age in years |
| **Chest Pain** | Typical Angina, Atypical, Non-anginal, Asymptomatic |
| **BP** | Resting Blood Pressure in mm Hg |
| **Cholesterol** | Serum cholestoral in mg/dl |
| **ST-Depression** | ST depression induced by exercise (Oldpeak) |
| **Vessels** | Number of major vessels (0-3) colored by flourosopy |

## 🎨 Design Philosophy
- **Rich Aesthetics**: Custom CSS with radial gradients and glassmorphism.
- **Explainable AI**: Visualizing the "why" behind the numbers.
- **Clinical Focus**: Designed for both patients (clarity) and doctors (data density).

---
**Disclaimer:** *This tool is for educational purposes only. Always consult a healthcare professional for medical advice.*
