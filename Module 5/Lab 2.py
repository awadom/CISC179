class Employee:
    def __init__(self,name, ID_number, department,job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

Susan_Meyers = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
Mark_Jones = Employee("Mark Jones", 39119, "IT", "Programmer")
Joy_Rogers = Employee("Joy Rogers", 81774, "Manufacturing", "Engineering")


print("Name:", Susan_Meyers.get_name())
print("ID Number:", Susan_Meyers.get_ID_number())
print("Department:", Susan_Meyers.get_department())
print("Job Title:", Susan_Meyers.get_job_title())
print()
print("Name:", Mark_Jones.get_name())
print("ID Number:", Mark_Jones.get_ID_number())
print("Department:", Mark_Jones.get_department())
print("Job Title:", Mark_Jones.get_job_title())
print()
print("Name:", Joy_Rogers.get_name())
print("ID Number:", Joy_Rogers.get_ID_number())
print("Department:", Joy_Rogers.get_department())
print("Job Title:", Joy_Rogers.get_job_title())
print()