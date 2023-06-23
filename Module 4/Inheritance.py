class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_wage(self):
        # Default implementation for calculating wage
        return self.base_salary

class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        # Calling the parent class's __init__ method
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_wage(self):
        # Overriding the calculate_wage method for FullTimeEmployee
        return self.base_salary + self.bonus

# Creating instances of FullTimeEmployee and Employee classes
employee1 = Employee("John Doe", 30000)
employee2 = FullTimeEmployee("Jane Smith", 40000, 5000)

# Accessing the calculate_wage method for each instance
print(employee1.calculate_wage())  # Output: 30000
print(employee2.calculate_wage())  # Output: 45000
