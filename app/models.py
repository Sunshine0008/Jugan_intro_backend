from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    employees: List["Employee"] = Relationship(back_populates="department")

class Employee(SQLModel, table=True):
    empid: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None
    dept_id: Optional[int] = Field(default=None, foreign_key="department.id")
    department: Optional[Department] = Relationship(back_populates="employees")
    projects: List["Project"] = Relationship(back_populates="lead")

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    lead_id: Optional[int] = Field(default=None, foreign_key="employee.empid")
    lead: Optional[Employee] = Relationship(back_populates="projects")