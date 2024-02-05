@lambda __: lambda _: 0 if not _ else _.pop() + sumi(_)
@lambda a: a
def sumi(a):...
print(sumi([]))
print(sumi([1,2,3,4]))