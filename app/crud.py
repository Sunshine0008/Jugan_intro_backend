from sqlmodel import Session, select
from .models import Employee, Department, Project

# --- EMPLOYEE CRUD ---
def create_employee(session: Session, employee: Employee):
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee

def get_employees(session: Session):
    return session.exec(select(Employee)).all()

def get_employee_by_id(session: Session, emp_id: int):
    return session.get(Employee, emp_id)

def delete_employee(session: Session, emp_id: int):
    db_emp = session.get(Employee, emp_id)
    if db_emp:
        session.delete(db_emp)
        session.commit()
    return db_emp

# --- DEPARTMENT CRUD ---
def create_department(session: Session, dept: Department):
    session.add(dept)
    session.commit()
    session.refresh(dept)
    return dept

def get_departments(session: Session):
    return session.exec(select(Department)).all()

# --- PROJECT CRUD ---
def create_project(session: Session, project: Project):
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

def get_projects(session: Session):
    return session.exec(select(Project)).all()