from fishhook import hook

@hook(int)
def __xor__(self, other):
    return self * other
a = 8
b = 6
print(a ^ b)