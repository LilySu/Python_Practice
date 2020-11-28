class Person:
    pass

print(Person.__name__)

class Program:
    language = 'Python'
    version = '3.6'

print(Program.__name__)
print(type(Program))

# program is an object, so we can access it:
print(Program.version)
Program.version = '3.7'
# we mutated the attribute value inside the Program class
print(Program.version)

print(getattr(Program, 'version'))
setattr(Program, 'version','3.6')
print(getattr(Program, 'version'))

# for doing a getattr on attributes that do not exist,
# we can set a default value:
getattr(Program, 'x','N/A')
# since 'x' is not an attribute of Program, it returns 'N/A' instead