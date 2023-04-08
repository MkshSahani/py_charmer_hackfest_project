# python main.py

from fastapi import FastAPI
import uvicorn
from validator import *
from db.database import *
from user_registration.index import student_registration_router, employee_registration_router
from login.index import user_router
from url_handling.index import new_extension_router, delete_extension_router

app = FastAPI()
app.include_router(student_registration_router)
app.include_router(employee_registration_router)
app.include_router(user_router)
app.include_router(new_extension_router)
app.include_router(delete_extension_router)

'''
/stress_data_url
/screen_time_data_url
/typing_data_url
'''

@app.post("/stress_data_url")
async def stress(stress_data: StressDataModel):
    stress_data = stress_data.dict()
    print(stress_data)
    if(DataStoring(stress_data)):
        return {
            "result": stress_data,
        }
    else:
        return {
            "result": "Not saved"
        }


@app.post("/screen_time_data_url")
async def screenTime(screen_time_data: ScreenTimeDataModel):
    screen_time_data = screen_time_data.dict()
    print(screen_time_data)
    if(DataStoring(screen_time_data)):
        return {
            "result": screen_time_data,
        }
    else:
        return {
            "result": "Not saved"
        }


@app.post("/typing_data_url")
async def typing(typing_data: TypingDataModel):
    typing_data = typing_data.dict()
    print(typing_data)
    if(DataStoring(typing_data)):
        return {
            "result": typing_data,
        }
    else:
        return {
            "result": "Not saved"
        }


uvicorn.run(app, host="127.0.0.1", port=8080)
