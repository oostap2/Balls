from Vector2 import Vector2

class RigidBody():
    def __init__(self, position : Vector2, mass : float = 1, dampening : float = 0.9):
        self.position = position
        self.acceleration = Vector2(0, 0) # прискорення
        self.velocity = Vector2(0, 0) # швидкість
        self.mass = mass
        self.inv_mass = 1 / mass
        self.temp_total_force = Vector2(0, 0)
        self.dampening = dampening

    def update(self, delta_time: float) -> None:
        self.acceleration = self.temp_total_force * self.inv_mass
        self.temp_total_force.x = 0
        self.temp_total_force.y = 0

        self.velocity += self.acceleration * delta_time
        self.velocity *= self.dampening ** delta_time
        self.position += self.velocity * delta_time
        self.acceleration.x = 0
        self.acceleration.y = 0

    def add_force(self, force : Vector2) -> None:
        self.temp_total_force += force

    def add_impulse(self, impulse : Vector2):
        self.velocity += impulse * self.inv_mass