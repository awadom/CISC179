# baseSalary = 30000
# overtime = 10
# rate = 20

# def getWage():
#     return baseSalary + (overtime * rate)

# print(getWage())

class Employee:
    def __init__(self, base_salary, overtime, rate):
        self.base_salary = base_salary
        self.overtime = overtime
        self.rate = rate
    
    def get_wage(self):
        return self.base_salary + (self.overtime * self.rate)

# Create an instance of the Employee class (constructor)
employee = Employee(30000, 10, 20)

# Access the get_wage() method through the instance
print(employee.get_wage())