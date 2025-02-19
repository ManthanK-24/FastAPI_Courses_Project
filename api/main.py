from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fakeDB = []

class Course(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None

@app.get("/")
def home():
    return {"Msg":"Hello from FastAPI Home Page"}

@app.get("/courses")
def get_courses():
    return fakeDB

@app.get("/course/{courseID}")
def get_a_course(course_id:int):
    courseIndex = course_id - 1
    if courseIndex<0 or courseIndex>=len(fakeDB):
        raise HTTPException(status_code=404, detail="CourseId not exist")
    return fakeDB[courseIndex]

@app.post("/addCourse")
def add_Course(course: Course):
    fakeDB.append(course.dict())
    return fakeDB[-1]

@app.delete("/courses/{course_id}")
def delete_course(courseID: int):
    fakeDB.pop(courseID-1)
    return {"task":"deleted successful"} 
    