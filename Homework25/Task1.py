import json


class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        
class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        
    def max_salary(self):
        emp_salary = []
        for i in self.employees:
            emp_salary.append(i.salary)
        return max(emp_salary)
    
    def min_salary(self):
        emp_salary = []
        for i in self.employees:
            emp_salary.append(i.salary)
        return min(emp_salary)
    
    
    def avg_salary(self):
        sum = 0
        for i in self.employees:
            sum += i.salary
        average = sum / len(self.employees)
        return average
    
    def position_emp(self):
        positions = {}
        for i in self.employees:
            positions[i.position] = positions.get(i.position, 0) + 1
        return positions
    
            
            
def main():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file was not found.")
        
    employees_data = data.get('employees')
    employees = []
    for emp_data in employees_data:
        emp_id = emp_data.get('id')
        emp_name = emp_data.get('name')
        emp_position = emp_data.get('position')
        emp_salary = emp_data.get('salary')
        employee = Employee(emp_id, emp_name, emp_position, emp_salary)
        employees.append(employee)

    department_name = data.get('name')
    department = Department(department_name, employees)


    
if __name__ == "__main__":
    main()




