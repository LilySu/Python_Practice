# tutorial from: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer
# each employee will have attributes and methods

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    raise_amt = 1.04
    # when we create methods within a class,
    # they receive the instance as the first argument automatically
    # by convention, we call the first instance self
    def __init__(self, first, last, pay):
        # instance variables:f
        self.first = first # same thing as creating an instance variable
        # except the instance variable emp_1.first = 'Corey' will be done
        # automatically as arguments are passed in.
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # with raises, it is nice to have a class value to be overridden
        # we wouldn't want our number of employees to be different for
        # any instance
        Employee.num_of_emps += 1

    # method "fullname" allows us to automate
    # print("{} {}".format(emp_1.first, emp_2.last))
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # when we access class variables, we need access them
        # through the class itself or an instance of the class
        self.pay = int(self.pay * self.raise_amount)

    # alters the function of our method, so we receive the class
    # as the first argument instead of the instance

    # with a regular method, we called the first instance 'self'
    # the convention for class variables is 'cls'. can't use keyword 'class'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

print(Employee.num_of_emps)

# instances of the Employee class, unique, different locations in memory
emp_1 = Employee('Corey', 'Schafer', 50000) # instance self is passed in automatically
# the init method will be run automatically
# emp_1 will be passed in as self, and will set all the attributes emp_1.first, emp_1.last etc.
# first, last, pay and email are attributes of our class.

# instance variables contain data that is unique to each instance
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())

# emp_1.fullname() # passes in self automatically
# gets transformed into Employee.fullname(emp_1) # the class does not know what instance, so we pass it in
# running method with class name itself, passing in instance as an argument

# class variables are variables that are shared among all instances of a class
# class variables should be the same for each instance

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount
# Employee.raise_amount

# class variables can be accessed from the class itself as well as both instances
# when we try to access an attribute on an instance, it will first check
# if the instance contains the attribute. If it doesn't, it'll see if the class
# or any class it inherits from contains that attribute

# emp_1.raise_amount = 1.05
#
# print(Employee.raise_amount)
# # accessing the class's raise amount attribute
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# # print(emp_1.__dict__)
# # print(Employee.__dict__)
#
# print(Employee.num_of_emps)

# regular methods in the class automatically take the instance as the first argument
# by convention, we call this self, a regular method takes the instance as the first argument
# how do we change this so the method takes in the class as the first argument
# to do this, we use class methods @classmethod

# automatically accepts the class as the first instance, we just pass in our value
Employee.set_raise_amt(1.05)

# the set_raise_amt method is a class method, where we are setting the class variable
# raise_amt to 1.05, same thing as: Employee.raise_amt = 1.05 but using a class method

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Using class methods as alternative constructors: use class methods to provide
# multiple ways to create objects