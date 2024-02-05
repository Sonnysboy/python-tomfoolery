a = type(1.0).__name__[3]
b = type(True).__name__[0]
c = str(print.__module__.__class__)[1]
d = __builtins__.__dict__['copyright']._Printer__data[44] # this one's my favorite
e = type({None}).__name__[1]
f = type(1.0).__name__[0]
g = __builtins__.globals.__name__[0]
h = str(__annotations__.__class_getitem__.__hash__)[22]
i = type(1).__name__[0]
j = str(complex(1, 2))[4]
k = ().__class__.__subclasses__()[2].__name__[13]
l = type(1.0).__name__[1]
m = getattr(dict, "__doc__")[15] 
n = type(1).__name__[1]
o = type(1.0).__name__[2]
p = (None,).__class__.__name__[2] 
q = list(zip(enumerate((None,).__class__.__subclasses__().__class__.__dict__.keys())))[6][0][1][3] # wtf
r = ().__class__.__bases__[0].__subclasses__()[40].__name__[-1]
s = type("").__name__[0]
t = type('', (), {}).__bases__[0].__name__[-1]
u = (None,).__class__.__name__[1]
v = property.__doc__[77] # this one was easier than i thought it'd be
w = ().__class__.__bases__[0].__subclasses__()[47].__name__[-1] # memoryview
x = list(zip(enumerate(type(().__class__.__subclasses__()).__dict__)))[28][0][1][1] # it happened again
y = getattr(dict, "__doc__")[18] 
z = list(zip(enumerate(str.__dict__)))[63][0][1][0]
alpha=""
alphaset = {}
for k in vars():
    if (__import__('re').search(r'^[a-z]$', k)):
        alpha += vars()[k]

print(alpha)