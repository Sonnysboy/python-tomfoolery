
import numpy
a=(b:=numpy.base_repr(8337503854730415241050377135811259267835, 36)).lower()+b
def letter_positions(s):
    replaced_string = "".join("{" + f"a[{a.index(c)}]" + "}" if c in a else c for c in s)

    return replaced_string
# assumes you use ' for all your strings
def ruincode(code):
    return f'''
a=(b:=__import__('numpy').base_repr(8337503854730415241050377135811259267835, 36)).lower()+b
eval(f"{letter_positions(code)}")
'''
print(ruincode("print('python moment')"))


