from Employee import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee('john','wik',50000)
    return employee

def test_raise_salary(employee):
    employee.raise_salary()
    assert employee.annual_salary == 55000

def test_raise_custom_salary(employee):
    employee.raise_salary(6000)
    assert employee.annual_salary == 56000