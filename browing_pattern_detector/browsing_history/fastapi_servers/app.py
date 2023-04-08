import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import URLDetails
from MLModel.model import *
app = FastAPI() 

origins = [
    "*",
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
    print(data)
    print("-------------------------")
    print(data)
    if data['url'] != '' and data['url'].startswith('chrome://') == False : 
        domain = re.search(r"([^/]*/){2}([^/]*)", data['url']).group(0)
        print(domain)
        print("-------------------------------------------------------------------")
        print("\n")
        # running ML code for categorize the website
        category=prediction(domain)
        print(category)
        # storing the category in the mongoDB server

        return {
        'status': "Success"
        }

@app.post("/quit_url")
async def quit_url(data : URLDetails): 
    print(data)
    data = data.dict()
    print("--------------------------------------")
    print(data)
    return {
        'status': "Success"
    }

@app.get("/test") 
async def test(): 
    return {
        'message' : 'Sucesss'
    }