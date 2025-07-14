from Vector2 import Vector2
from RigidBody import RigidBody

class CircleCollider():
	def __init__(self, pos : Vector2, rigid_body : RigidBody, radius : float = 20, elasticity : float = 1):
		self.pos = pos
		self.radius = radius
		self.parent_rigid_body = rigid_body
		self.elasticity = elasticity