import ctypes
import functools
def new_method(cls):
    def decorator(func):
        dict = ctypes.py_object.from_address(id(cls.__dict__) + 16).value
        dict[func.__name__] = func
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
@new_method(object)
def __matmul__(self, fn):
  return fn(self)
print(4123 @ str)