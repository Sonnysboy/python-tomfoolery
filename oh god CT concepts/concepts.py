identity = lambda x: x
def Functor(methods):
    def wrap(datatype):
        if not isinstance(methods, dict): raise "your mom"
        datatype.fmap = methods['fmap']
        datatype.leftdollar = lambda _, x: (datatype.fmap(_, lambda _: x))
        return datatype
    return wrap


# # really this should have a functor check too but i dont give a single damn
# def Applicative(methods):
#     def wrap(datatype):
#         if not isinstance(methods, dict): raise "applcative requires PURE"
#         if not methods['pure']: raise "applicative requires PURE"
        
#         def liftA2(function, )
#         def sequence(self, function):
            

#         pure = methods['pure']

# CBF


def Monad(methods):
    def wrap(datatype):
        if not isinstance(methods, dict): raise "your mom"
        datatype.bind = methods['bind'] # honestly it's up to the programmer to do this correc tly
def __maybe_functor():
    def fmap(self, function):
        if self.is_empty(): return Maybe.empty()
        return Maybe(function(self.get()))
    return { 'fmap' : fmap}
@Functor(__maybe_functor())
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
print(x.whatisthisevencalled(4))