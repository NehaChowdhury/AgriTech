from fastapi import APIRouter, HTTPException, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.models.schemas import CropInput, FertilizerInput
from src.services.model_service import model_service
from src.services.fertilizer_service import fertilizer_service
from src.core.config import settings
import logging

router = APIRouter()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
logger = logging.getLogger(__name__)

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@router.get("/crop", response_class=HTMLResponse)
async def crop_page(request: Request):
    return templates.TemplateResponse(request=request, name="crop.html")

@router.get("/fertilizer", response_class=HTMLResponse)
async def fertilizer_page(request: Request):
    crops = fertilizer_service.get_crop_list()
    return templates.TemplateResponse(request=request, name="fertilizer.html", context={"crops": crops})

@router.post("/predict-crop")
async def predict_crop(data: CropInput):
    try:
        features = [data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall]
        prediction = model_service.predict_crop(features)
        return {"prediction": prediction}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction service error")

@router.post("/predict-fertilizer")
async def predict_fertilizer(data: FertilizerInput):
    try:
        recommendations = fertilizer_service.recommend_fertilizer(data.Crop, data.N, data.P, data.K)
        if recommendations is None:
            raise HTTPException(status_code=404, detail=f"Data for '{data.Crop}' not available")
        return {"recommendation": recommendations}
    except Exception as e:
        logger.error(f"Fertilizer logic error: {e}")
        raise HTTPException(status_code=500, detail="Recommendation service error")

@router.get("/disease", response_class=HTMLResponse)
async def disease_page(request: Request):
    return templates.TemplateResponse(request=request, name="disease.html")

@router.post("/predict-disease")
async def predict_disease(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="File provided is not an image.")
        
        contents = await file.read()
        prediction = model_service.predict_disease(contents)
        return prediction
    except Exception as e:
        logger.error(f"Disease prediction error: {e}")
        raise HTTPException(status_code=500, detail="Disease prediction service error")
