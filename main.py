from random import randint
import pygame
from Ball import Ball
from CollisionSystem import*
pygame.init()

WINDOW_SIZE = (700, 700)
window = pygame.display.set_mode(WINDOW_SIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (150, 255, 150)

FPS = 60
DELTA = 1 / FPS
FORCE_MULTIPLIER = 5_000
QUANTITY = 8
RADIUS = 20
MASS = 1
SPAWN_PADDING = 200

colliders = []
balls = []

for _ in range(QUANTITY):
    ball = Ball(
        Vector2(
            randint(SPAWN_PADDING, WINDOW_SIZE[0] - SPAWN_PADDING), 
            randint(SPAWN_PADDING, WINDOW_SIZE[1] - SPAWN_PADDING), 
        ),
        WHITE,
        RADIUS,
        MASS)
    balls.append(ball)
    colliders.append(ball.collider)
balls[-1].circle.color = GREEN

def reflection(ball):
    pos = ball.circle.pos
    radius = ball.circle.radius
    if pos.x < radius:
        ball.rigid_body.velocity.x = abs(ball.rigid_body.velocity.x)
    if pos.y < radius:
        ball.rigid_body.velocity.y = abs(ball.rigid_body.velocity.y)
    if pos.x > WINDOW_SIZE[0] -radius:
        ball.rigid_body.velocity.x = - abs(ball.rigid_body.velocity.x)
    if pos.y > WINDOW_SIZE[1] -radius:
        ball.rigid_body.velocity.y = - abs(ball.rigid_body.velocity.y)

def push_ball(force_multiplier: float, ball: Ball):
    x, y = pygame.mouse.get_pos()
    force = Vector2(x, y) - ball.rigid_body.position
    force.normalize()
    force *= force_multiplier
    ball.rigid_body.add_force(force)

while True:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                push_ball(FORCE_MULTIPLIER, balls[-1])

    for ball in balls:
        ball.update(DELTA)
        reflection(ball)

    resolve_all_collisions(colliders)

    for ball in balls:
        ball.draw(window)

    pygame.display.update()