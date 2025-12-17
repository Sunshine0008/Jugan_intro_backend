import pytest
from sqlmodel import SQLModel, create_engine, Session, select
from sqlalchemy.exc import IntegrityError
from models import Employee, Department # Replace with your actual filename

# Setup a clean, in-memory database for every test
@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

# TEST 1: Department Creation
def test_create_department(session: Session):
    dept = Department(name="Data Science")
    session.add(dept)
    session.commit()
    
    result = session.exec(select(Department)).first()
    assert result.name == "Data Science"
    assert result.id is not None

# TEST 2: Employee with Department (The Relationship)
def test_create_employee_with_dept(session: Session):
    # 1. Add Department
    dept = Department(name="Sales")
    session.add(dept)
    session.commit()

    # 2. Add Employee linked to Dept ID
    target_name = "Edrian Jugan"
    # CHANGE 'dept=' TO 'dept_id='
    emp = Employee(name=target_name, dept_id=dept.id, age=20) 
    session.add(emp)
    session.commit()

    # 3. Verify Join logic
    statement = select(Employee).where(Employee.name == target_name)
    employee = session.exec(statement).first()

    assert employee is not None
    # CHANGE '.dept' TO '.dept_id'
    assert employee.dept_id == dept.id
    
# TEST 3: Validation Check (Missing Required Fields)
def test_employee_missing_name(session: Session):
    # 'name' is required in your class definition
    with pytest.raises(Exception): 
        # SQLModel/Pydantic will catch missing required fields
        emp = Employee(age=25) 
        session.add(emp)
        session.commit()