from typing import *

class Maybe:
    value = None
    
    def __init__(self, value):
        self.value = value
    
    def is_empty(self):
        return self.value == None 

    def empty():
        return Maybe(None)

    def get(self):
        return self.value
    # type: g : (a -> Maybe b)
    def __lshift__(self, g): 
        if self.is_empty():
            return Maybe.empty()
        return g(self.get())

    def pure(x):
        return Maybe(x)
    def __repr__(self):
        return ["Nothing", f'Just {self.value}'][not self.is_empty()]

x = Maybe(4)

# print(x >>=(lambda x: Maybe.pure(x+3)))