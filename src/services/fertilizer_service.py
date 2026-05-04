import pandas as pd
import os
import logging
from src.core.config import settings

logger = logging.getLogger(__name__)

class FertilizerService:
    _instance = None
    _df = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FertilizerService, cls).__new__(cls)
        return cls._instance

    def load_data(self):
        if self._df is None:
            if not os.path.exists(settings.DATA_PATH):
                logger.error(f"Fertilizer data not found at {settings.DATA_PATH}")
                return None
            try:
                self._df = pd.read_csv(settings.DATA_PATH)
                self._df.columns = [c.strip() for c in self._df.columns]
                logger.info("Fertilizer dataset loaded successfully via Service.")
            except Exception as e:
                logger.error(f"Error loading fertilizer dataset: {e}")
        return self._df

    def get_crop_list(self):
        df = self.load_data()
        if df is not None:
            return sorted(df['Crop'].unique().tolist())
        return []

    def recommend_fertilizer(self, crop_name: str, N: float, P: float, K: float):
        df = self.load_data()
        if df is None:
            raise Exception("Fertilizer data not available")

        crop_data = df[df['Crop'].str.lower() == crop_name.strip().lower()]
        if crop_data.empty:
            return None

        optimal_N = crop_data['N'].iloc[0]
        optimal_P = crop_data['P'].iloc[0]
        optimal_K = crop_data['K'].iloc[0]

        recommendations = []
        if N < optimal_N - 10: recommendations.append("Nitrogen is low → Add Urea")
        elif N > optimal_N + 10: recommendations.append("Nitrogen is high → Reduce Nitrogen usage")

        if P < optimal_P - 5: recommendations.append("Phosphorus is low → Add Bone Meal or Superphosphate")
        elif P > optimal_P + 5: recommendations.append("Phosphorus is high → Avoid DAP")

        if K < optimal_K - 5: recommendations.append("Potassium is low → Add Potash or Kelp Meal")
        elif K > optimal_K + 5: recommendations.append("Potassium is high → Reduce Potassium usage")

        if not recommendations:
            recommendations.append("Balanced soil → No fertilizer needed")

        return recommendations

fertilizer_service = FertilizerService()
