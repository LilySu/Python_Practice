# tutorial from: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer
# each employee will have attributes and methods

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount # same as saying Employee.raise_amt = 1.05

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # if you don't reference instance or class anywhere in the function
    @staticmethod # does not take instance or class as first argument
        # return if our day falls on a weekday
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

Employee.set_raise_amt(1.05)

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

# class methods as alternative constructors - use class methods
# to provide multiple ways of creating objects

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))