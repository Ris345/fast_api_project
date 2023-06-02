from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import List
from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI, Path
app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}

# import uvicorn
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World"}
# if __name__ == "__main__":
#    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(name):
    return {"name": "Rishav"}


# @app.get("/hello/{name}/{age}")
# async def hello(*, name: str=Path(...,min_length=3 , max_length=10), age: int = Path(..., ge=1, le=100)):
#    return {"name": name, "age":age}


# from typing import List
# from pydantic import BaseModel, Field
# class Student(BaseModel):
#    id: int
#    name :str = Field(None, title="The description of the item", max_length=10)
#    subjects: List[str] = []


# # def check(name:str):
# #     return "Heyy there!!" + " " + name

# # class rectangle:
# #    def __init__(self, w:int, h:int) ->None:
# #       self.width=w
# #       self.height=h


# # def area(r:rectangle)->int:
# #    return r.width*r.height
# # r1=rectangle(10,20)


# # print ("area = ", area(r1))

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str = Field(None, title="name of student", max_length=10)
    subjects: List[str] = []


@app.post("/students/")
async def student_data(s1: Student):
    return s1


@app.post("/students")
async def student_data(name: str = Body(...),
                       marks: int = Body(...)):
    return {"name": name, "marks": marks}


@app.post("/students/{college}")
async def student_data(college: str, age: int, student: Student):
    retval = {"college": college, "age": age, **student.dict()}
    return retval


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/hello/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", {"request": request})

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(request: Request, name:str):
   return templates.TemplateResponse("hello.html", {"request": request, "name":name})


# app.mount(app.mount("/static", StaticFiles(directory="static"), name="static"))
          
          

# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")
# @app.get("/hello/{name}", response_class=HTMLResponse)
# async def hello(request: Request, name:str):
#    return templates.TemplateResponse("hello.html", {"request": request, "name":name})





# from fastapi.responses import HTMLResponse
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/hello/")
# async def hello():
#    ret='''
# <html>
# <body>
# <h2>Hello World!</h2>
# </body>
# </html>
# '''
#    return HTMLResponse(content=ret)
