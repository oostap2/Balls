from Vector2 import Vector2
from CircleCollider import CircleCollider

class ContactPoint():
	def __init__(self, depth : float, normal : Vector2, coll1 : CircleCollider, coll2 : CircleCollider):
		self.depth = depth
		self.normal = normal
		self.coll1 = coll1
		self.coll2 = coll2