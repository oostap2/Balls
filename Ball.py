from Circle import Circle
from RigidBody import RigidBody
from Vector2 import Vector2
from CircleCollider import CircleCollider

class Ball():
    def __init__(self, pos : Vector2, color : tuple[int, int, int] = (255, 255, 255), radius : float = 20, mass : float = 1):
        self.rigid_body = RigidBody(pos, mass)
        self.circle = Circle(pos, radius, color)
        self.collider = CircleCollider(pos, self.rigid_body, radius)

    def update(self, delta_time):
        self.rigid_body.update(delta_time)

    def draw(self, win):
        self.circle.draw(win)
