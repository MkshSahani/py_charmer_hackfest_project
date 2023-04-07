# python main.py

from fastapi import FastAPI
import uvicorn
from validator import StressDataModel, TypingDataModel, ScreenTimeDataModel
from database import DataStoring

app = FastAPI()


@app.post("/register_student")
async def registerStudent(student_data: StudentModel):
    student_data = student_data.dict()
    print(student_data)
    if(DataStoring(student_data)):
        return {
            "result": student_data,
        }
    else:
        return {
            "result": "Not saved"
        }


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
async def stress(screen_time_data: ScreenTimeDataModel):
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
