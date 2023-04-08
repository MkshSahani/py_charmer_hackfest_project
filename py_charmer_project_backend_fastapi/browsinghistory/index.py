from fastapi import APIRouter 

browser_api_router = APIRouter(
    prefix="/browsing_history",
    tags = ["browsing_history"]
)

@browser_api_router.post("/add_user_browsing_history")
async def add_user_browing_hist():
    pass 