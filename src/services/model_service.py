import pickle
import os
import logging
import numpy as np
import io
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from src.core.config import settings

logger = logging.getLogger(__name__)

class ModelService:
    _instance = None
    _model = None
    _disease_model = None
    
    DISEASE_CLASSES = ['Bacterial leaf blight', 'Brown spot', 'Leaf smut']

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

    def load_disease_model(self):
        if self._disease_model is None:
            if not os.path.exists(settings.DISEASE_MODEL_PATH):
                logger.error(f"Disease model file not found at {settings.DISEASE_MODEL_PATH}")
                return None
            try:
                self._disease_model = tf.keras.models.load_model(settings.DISEASE_MODEL_PATH)
                logger.info("Disease prediction model loaded successfully via Service.")
            except Exception as e:
                logger.error(f"Error loading disease model: {e}")
        return self._disease_model

    def predict_disease(self, image_bytes: bytes):
        model = self.load_disease_model()
        if model is None:
            raise Exception("Disease model not loaded")
        
        try:
            # Process image (Matching Keras ImageDataGenerator behavior)
            img = Image.open(io.BytesIO(image_bytes))
            img = img.convert('RGB')
            # Use NEAREST interpolation to match flow_from_directory default
            img = img.resize((128, 128), resample=Image.NEAREST)
            # img_to_array ensures float32 dtype
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            
            # Predict
            predictions = model.predict(img_array)
            predicted_class_idx = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class_idx])
            
            return {
                "disease": self.DISEASE_CLASSES[predicted_class_idx],
                "confidence": confidence
            }
        except Exception as e:
            logger.error(f"Error in predicting disease: {e}")
            raise

model_service = ModelService()
