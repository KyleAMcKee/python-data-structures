class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return self.fullname().__len__()

class Developer(Employee):
    raise_amt = 1.12

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language

class Manager(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if not employees:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    
    def print_employees(self):
        for emp in self.employees:
            print(emp.fullname())

dev1 = Employee('Homer', 'Simpson', 50000)
dev2 = Developer('Bart', 'Simpson', 65000, 'KabaScript')
man1 = Manager('Marge', 'Simpson', 75000)

man1.add_employee(dev1)
man1.add_employee(dev2)
man1.print_employees()
man1.remove_employee(dev2)
man1.print_employees()

print(isinstance(man1, Developer))
print(issubclass(Manager, Employee))
print(dev1)
print(dev1 + dev2)
print(len(dev1))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# print(dev2.pay)