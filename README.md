# 🌾 AgriTech: Smart Agriculture Decision Support System

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15+-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**AgriTech** is an AI-powered platform designed to empower farmers and agricultural experts with data-driven insights. By leveraging Machine Learning and Deep Learning models, the system provides accurate crop recommendations, fertilizer optimization, and real-time disease detection for sustainable farming.

---

## ✨ Key Features

### 🚜 1. Crop Recommendation
Predict the most suitable crop for your land using soil and environmental parameters.
- **Model**: Random Forest Classifier
- **Parameters**: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall.

### 🧪 2. Fertilizer Optimizer
Receive precise nutrient advice based on the specific requirements of your chosen crop and current soil health.
- **Logic**: Rule-based optimization engine integrated with historical agricultural data.
- **Goal**: Prevent over-fertilization and reduce environmental impact.

### 🦠 3. Rice Disease Identification
Upload an image of a rice leaf to identify common diseases instantly.
- **Model**: Convolutional Neural Network (CNN)
- **Classes**: Bacterial Leaf Blight, Brown Spot, Leaf Smut.
- **Accuracy**: Optimized for mobile-captured images.
- **Dataset**: [Rice Leaf Diseases Dataset](https://www.kaggle.com/datasets/vbookshelf/rice-leaf-diseases) (Used for training).

---
## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous, High Performance)
- **Machine Learning**: Scikit-Learn (Random Forest)
- **Deep Learning**: TensorFlow/Keras (CNN for Image Classification)
- **Data Handling**: NumPy, Pandas
- **Frontend**: Jinja2 Templates, Tailwind CSS, Lucide Icons
- **Image Processing**: Pillow

---

## 📁 Project Structure

```text
├── src/
│   ├── api/            # API endpoints and route definitions
│   ├── core/           # Configuration and global settings
│   ├── models/         # Pydantic data schemas
│   ├── services/       # Business logic and ML inference services
│   └── main.py         # Application entry point
├── data/               # CSV datasets for training and reference
├── models/             # Pre-trained model binaries (.pkl, .keras)
├── static/             # Frontend assets (CSS, JS, Images)
├── templates/          # HTML templates with Jinja2 syntax
├── notebooks/          # Research and model training experiments
├── requirements.txt    # Project dependencies
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Virtual Environment (recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NehaChowdhury/AgriTech.git
   cd AgriTech
   ```

2. **Set up Virtual Environment**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

Start the development server using Uvicorn:
```bash
uvicorn src.main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

---

## 📖 API Documentation

AgriTech provides a fully documented REST API out of the box:
- **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Example Endpoint: Crop Prediction
**POST** `/predict-crop`
```json
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.8,
  "humidity": 82.0,
  "ph": 6.5,
  "rainfall": 202.9
}
```

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

© 2026 AgriTech Decision Support System.
