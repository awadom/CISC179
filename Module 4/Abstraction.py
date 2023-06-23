# Abstract base class for an Employee
class Employee:
    def __init__(self, base_salary, overtime, rate):
        self.base_salary = base_salary
        self.overtime = overtime
        self.rate = rate
    
    # Declaring the calculate_wage() method as a virtual method
    def calculate_wage(self):
        raise NotImplementedError("Subclasses must implement the calculate_wage() method.")
    
    # Providing a common interface to access the wage calculation
    def get_wage(self):
        return self.calculate_wage()

# Subclass of Employee representing a Full-Time Employee
class FullTimeEmployee(Employee):
    def calculate_wage(self):
        # Implementing the calculate_wage() method specific to full-time employees
        return self.base_salary + (self.overtime * self.rate)

# Creating an instance of the FullTimeEmployee class
employee = FullTimeEmployee(30000, 10, 20)

# Accessing the get_wage() method through the instance
print(employee.get_wage())
