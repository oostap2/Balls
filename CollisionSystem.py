from Vector2 import Vector2
from CircleCollider import CircleCollider
from ContactPoint import ContactPoint
from RigidBody import RigidBody
import math

def check_collision(coll1 : CircleCollider, coll2 : CircleCollider) -> ContactPoint:
	radius_sum = coll1.radius + coll2.radius
	radius_sum_sq = radius_sum **2
	distance_vector = coll2.pos - coll1.pos
	distance_sq = distance_vector.length_squared()

	if radius_sum_sq > distance_sq:
		distance = math.sqrt(distance_sq)
		depth = radius_sum - distance
		normal = distance_vector.normalized()
		contact_point = ContactPoint(depth, normal, coll1, coll2)
		return contact_point

def correct_colliders(contact_point):
	correction_vector = contact_point.normal * contact_point.depth
	contact_point.coll1.pos += correction_vector * -0.5
	contact_point.coll2.pos += correction_vector * 0.5

def apply_impact_force(contact_point):
	rb1 : RigidBody = contact_point.coll1.parent_rigid_body
	rb2 : RigidBody = contact_point.coll2.parent_rigid_body
	relative_velocity : Vector2 = rb2.velocity - rb1.velocity
	effective_relative_velocity = Vector2.dot_product(relative_velocity, contact_point.normal)

	if effective_relative_velocity > 0:
		return

	e = min(contact_point.coll1.elasticity, contact_point.coll2.elasticity) 
	j = (-(1 + e) * effective_relative_velocity) / (rb1.inv_mass + rb2.inv_mass)
	impulse_vector = contact_point.normal * j
	rb1.add_impulse(impulse_vector * -1)
	rb2.add_impulse(impulse_vector)

def resolve_circle_collision(contact_point):
	apply_impact_force(contact_point)
	correct_colliders(contact_point)

def resolve_all_collisions(collider_list) -> None:
	contact_point_list = []
	i = 1
	for coll1 in collider_list:
		for coll2 in collider_list[i:]:
			contact_point = check_collision(coll1, coll2)
			if isinstance(contact_point, ContactPoint):
				contact_point_list.append(contact_point)
		i += 1
	# print('AMOGUS')
	for contact_point in contact_point_list:
		resolve_circle_collision(contact_point)

