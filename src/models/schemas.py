from pydantic import BaseModel

class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

class FertilizerInput(BaseModel):
    Crop: str
    N: float
    P: float
    K: float
