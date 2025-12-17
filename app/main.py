from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from .database import get_session, create_db_and_tables
from .models import Employee, Department, Project
from . import crud
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/employees/", response_model=Employee)
def create_emp_route(employee: Employee, session: Session = Depends(get_session)):
    return crud.create_employee(session, employee)

@app.get("/employees/", response_model=list[Employee])
def read_emps_route(session: Session = Depends(get_session)):
    return crud.get_employees(session)

@app.post("/departments/", response_model=Department)
def create_dept_route(dept: Department, session: Session = Depends(get_session)):
    return crud.create_department(session, dept)

@app.post("/projects/", response_model=Project)
def create_proj_route(project: Project, session: Session = Depends(get_session)):
    return crud.create_project(session, project)