from pydantic import BaseModel

class StudentModel(BaseModel):
    email: str
    username: str
    password: str
    firstname: str
    lastname: str
    intervaltime: int

class StressDataModel(BaseModel):
	time: str
	stressLevel: float

class ScreenTimeDataModel(BaseModel):
	time: str
	screenTimeSpeed: int

class TypingDataModel(BaseModel):
	time: str
	typingSpeed: int