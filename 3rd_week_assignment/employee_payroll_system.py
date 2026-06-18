from abc import ABC, abstractmethod
# Abstract Base Class
class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

    def payslip(self):
        print(f"{self.name} | Pay: Rs {self.calculate_pay()}")

# Full-Time Employee
class FullTimeEmployee(Employee):

    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"FullTimeEmployee({self.name})"

# Part-Time Employee
class PartTimeEmployee(Employee):

    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"PartTimeEmployee({self.name})"

# Contractor
class Contractor(Employee):

    def __init__(self, name, project_fee, projects):
        super().__init__(name)
        self.project_fee = project_fee
        self.projects = projects

    def calculate_pay(self):
        return self.project_fee * self.projects

    def __str__(self):
        return f"Contractor({self.name})"


# ---------------------------------
# Main Program
# ---------------------------------

staff = [
    FullTimeEmployee("Asha", monthly_salary=60000),
    PartTimeEmployee("Bibek", hourly_rate=500, hours_worked=80),
    Contractor("Chen", project_fee=15000, projects=3)
]

print("=" * 50)
print("EMPLOYEE PAYROLL SYSTEM")
print("=" * 50)

# Polymorphism
for emp in staff:
    print(emp)
    emp.payslip()
    print("-" * 30)

# Total Payroll
total = sum(emp.calculate_pay() for emp in staff)

print(f"\nTotal Payroll: Rs {total}")

# Testing Abstract Class
try:
    test = Employee("Test")
except TypeError as e:
    print("\nError:", e)