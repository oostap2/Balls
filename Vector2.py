import math
from random import randint

class Vector2():
    def __init__(self, x : float = 0, y : float = 0):
        self.x = x
        self.y = y

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x + other, self.y + other)

    def __iadd__(self, other):
        if isinstance(other, Vector2):
            self.x += other.x
            self.y += other.y
            return self
        if isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x - other, self.y - other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        if isinstance(other, (int, float)):
            rec = 1 / other
            return Vector2(self.x * rec, self.y * rec)

    def __rtruediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(other.x / self.x, other.y / self.y)

    def length(self) -> float:
        return math.sqrt(self.x **2 + self.y **2)

    def length_squared(self) -> float:
        return self.x **2 + self.y **2

    def normalize(self) -> None:
        l = self.length()
        if l == 0:
            self.x = 0
            self.y = 0
            return
        rec_l = 1 / l
        self.x *= rec_l
        self.y *= rec_l

    def normalized(self) -> "Vector2":
        l = self.length()
        if l == 0:
            return Vector2(0, 0)
        rec_l = 1 / l
        return Vector2(self.x * rec_l, self.y * rec_l)

    def dot_product(a : "Vector2", b : "Vector2") -> float:
        return a.x * b.x + a.y * b.y

    def deconstruct(self) -> tuple[float, float]:
        return (self.x, self.y)
