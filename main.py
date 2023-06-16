class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self, hours_worked):
        return self.salary * hours_worked

    def display(self):
        print("Name: {}".format(self.name))
        print("Salary: {}".format(self.salary))


class HourlyEmployee(Employee):
    def calculate_pay(self, hours_worked):
        if hours_worked <= 40:
            return self.salary * hours_worked
        else:
            overtime_pay = (hours_worked - 40) * (self.salary * 1.5)
            return (self.salary * 40) + overtime_pay


class SalariedEmployee(Employee):
    def calculate_pay(self, hours_worked):
        return self.salary / 52 * 2


hourly_employee = HourlyEmployee("John Doe", 10)
salaried_employee = SalariedEmployee("Jane Doe", 52000)

hourly_employee.display()
print("Pay: {}".format(hourly_employee.calculate_pay(45)))
print()

salaried_employee.display()
print("Pay: {}".format(salaried_employee.calculate_pay(0)))
