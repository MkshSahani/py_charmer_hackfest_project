import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import URLDetails
from MLModel.model import *
app = FastAPI() 

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send_url")
async def send_url(data : URLDetails):
    data = data.dict()
    if data['url'] != '' and data['url'].startswith('chrome://') == False : 
        domain = re.search(r"([^/]*/){2}([^/]*)", data['url']).group(0)
        category=prediction(domain)
        
        return {
        'status': "Success"
        }

@app.post("/quit_url")
async def quit_url(data : URLDetails): 
    print(data)
    data = data.dict()
    return {
        'status': "Success"
    }
