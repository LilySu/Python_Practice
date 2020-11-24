# How do we define attributes in a class
# get attribute is a string

class MyClass:
    language = 'Python' # this is an attribute
    version = '3.6' # this is an attribute

print(getattr(MyClass, 'language')) # class, property names are always strings
# returns Python because that is its state
# print(getattr(MyClass, 'X')) # causes an AttributeError
print(getattr(MyClass, 'x', 'N/A')) # passes a default value
# without raising error if value does not exist

# the dot notation for getting attributes is a lot simpler
print(MyClass.language)


# Set Attribute Values in Objects
# setattr(object_symbol, attribute_name (string), attribute_value)
print(setattr(MyClass, 'version', '3.7'))
# or
MyClass.version = '3.7'

print(getattr(MyClass, 'version'))