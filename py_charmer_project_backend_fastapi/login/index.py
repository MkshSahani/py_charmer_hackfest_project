from fastapi import APIRouter
from .validator import *
from db.database import *

'''
/user/login
'''

user_router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@user_router.post("/login")
async def userLogin(login_data: LoginModel):
    login_data = login_data.dict()
    print(login_data)
    if(UserLogin(
        email=login_data['email'], 
        pwd=login_data['pass_word'])):
        return {
            "result": "authenticated user"
        }
    else:
        return {
            "result": "unauthenticated user"
        }