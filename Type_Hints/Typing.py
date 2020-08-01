import random

def add_this(a: int , b: int) -> int: # returns an integer, works after 3.5
    return random.randint(a,b)

# you need to pair with a testing library that has a type checker ie mypy

# an explicit type such as an object could be configured for checking

# we can just make people be more explicit

# you want to avoid returning optional or unions - every caller has to check what they got back to make sense of return value
from typing import Optional, overload

def get_foo(foo_id: Optional[int]) -> Optional[Foo]:
    if foo_id is None:
        return None
    return Foo(foo_id)
# you will get error: NoneType has no attribute 'id'
# better to break it down as:
@overload
def get_foo(foo_id: None) -> None:
    pass

@overload
def get_foo(foo_id: int) -> Foo:
    pass

def get_foo(foo_id: Optional[int]) -> Optional[Foo]:
    if foo_id is None:
        return None
    return Foo(foo_id)

from typing import TypeVar

AnyStr = TypeVar('AnyStr', str, bytes)

def concat(a:AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat('foo', b'bar') # when you concat two different types it won't work
concat(3, 6) # when you concat something outside AnyStr, it doesn't work
concat('foo', 'bar') # when you combine one type in, you get teh same type out

from typing import AnyStr

from typing import Any # Will never cause a type error



if __name__ == '__main__':
    print(add_this(2,3))

    my_foo = get_foo(3)
    my_foo.id