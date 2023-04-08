from fastapi import APIRouter 
from setup import mongo_client
stress_blink_router = APIRouter(
    prefix="/stress_blink_value",
    tags = ["stress_blink_value"]
)
from .validator import StressBlinkValue, GetStressBlinkData
from setup import pycharmer_mongo_db

@stress_blink_router.post("/add_stress_blink_values") 
async def add_stress_blink_values(stressBlinkValue : StressBlinkValue):
    stress_blink_value = stressBlinkValue.dict()
    pycharmer_mongo_db.stress_blink_data.insert(stress_blink_value)
    return {
        "status_code" : 200,
        "message": "Success",
        "data": {}
    }


@stress_blink_router.post("/get_stress_blink_values") 
async def get_stress_blink_data(getStressBlinkValues : GetStressBlinkData):
    get_stress_blink_data = getStressBlinkValues.dict() 
    data = pycharmer_mongo_db.stress_blink_data.find({"access_token": get_stress_blink_data['access_token']}) 
    time_stamp_lst = []
    
    for i in data:
        print(i)
    return {
        "status_code" : 200,
        "message": "Success",
        "data": {}
    }
    
