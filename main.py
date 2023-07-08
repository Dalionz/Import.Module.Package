from aplication.salary import calculate_salary
from aplication.db.people import get_employees
from datetime import date
import pyjokes



def my_func1():
    calculate_salary()
    get_employees()
    current_date = date.today()
    print(current_date)

def my_func2():
    print(pyjokes.get_joke())


if __name__ == '__main__':
    my_func1()
    my_func2()
