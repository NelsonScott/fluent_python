from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar

        return Vector(x, y)

v = Vector()
repr(v)
print abs(v)
print bool(abs(v))
v.x = v.y = 3
print abs(v)

x = Vector(4.0, 5)
print bool(x)
repr(x)
print x * 3

print x + v
