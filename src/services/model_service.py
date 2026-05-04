import pickle
import os
import logging
import numpy as np
from src.core.config import settings

logger = logging.getLogger(__name__)

class ModelService:
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelService, cls).__new__(cls)
        return cls._instance

    def load_model(self):
        if self._model is None:
            if not os.path.exists(settings.MODEL_PATH):
                logger.error(f"Model file not found at {settings.MODEL_PATH}")
                return None
            try:
                with open(settings.MODEL_PATH, 'rb') as f:
                    self._model = pickle.load(f)
                    logger.info("Crop prediction model loaded successfully via Service.")
            except Exception as e:
                logger.error(f"Error loading model: {e}")
        return self._model

    def predict_crop(self, features: list):
        model = self.load_model()
        if model is None:
            raise Exception("Model not loaded")
        
        input_data = np.array([features])
        prediction = model.predict(input_data)
        return str(prediction[0]).capitalize()

model_service = ModelService()
