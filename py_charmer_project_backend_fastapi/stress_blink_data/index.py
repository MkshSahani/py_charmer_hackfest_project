from fastapi import APIRouter 

stress_blink_router = APIRouter(
    prefix="/stress_blink_value",
    tags = ["stress_blink_value"]
)
from .validator import StressBlinkValue
from setup import pycharmer_mongo_db

@stress_blink_router.post("/add_stress_blink_values") 
async def add_stress_blink_values(stressBlinkValue : StressBlinkValue):
    print(stressBlinkValue)
    stress_blink_value = stressBlinkValue.dict()
    pycharmer_mongo_db.stress_blink_data.insert(stress_blink_value)
    return {
        "status_code" : 200,
        "message": "Success",
        "data": {}
    }
    