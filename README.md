# AgriTech - Smart Agriculture Decision Support System

AgriTech is a modern, scalable AI-driven platform designed to help farmers make data-driven decisions. It provides ML-based crop recommendations and rule-based fertilizer advice based on soil and environmental data.

## 🚀 Features
- **Crop Recommendation**: Predictive analysis using a Random Forest model.
- **Fertilizer Advice**: Precision nutrient recommendations based on crop requirements.
- **Modern API**: Built with FastAPI for high performance and asynchronous support.
- **Service-Oriented**: Clean separation of business logic and API routes.

https://github.com/user-attachments/assets/53830072-36b1-4158-8c17-963a6df65c7f


## 🛠️ Tech Stack
- **Backend**: FastAPI, Pydantic, Jinja2
- **ML/Data**: Scikit-Learn, Pandas, NumPy
- **Frontend**: Tailwind CSS, Lucide Icons

## 📁 Project Structure
```text
├── src/                # Core application logic
│   ├── api/            # API Route handlers
│   ├── services/       # Business & ML services
│   ├── core/           # Configuration & Settings
│   └── models/         # Data schemas (Pydantic)
├── data/               # Datasets
├── models/             # Trained ML model binaries
├── static/             # CSS, JS, and images
├── templates/          # HTML templates (Jinja2)
├── notebooks/          # Research & training notebooks
└── requirements.txt    # Project dependencies
```

## 🏁 Getting Started

### Local Setup
1. Activate your virtual environment:
   ```powershell
   venv\Scripts\activate
   ```
2. Run the application:
   ```bash
   python -m uvicorn src.main:app --reload
   ```

The application will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## 📜 License
© 2026 AgriTech Decision Support System.
