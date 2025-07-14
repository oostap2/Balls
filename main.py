from random import randint
import math
import pygame
from Vector2 import Vector2
from Ball import Ball
from CollisionSystem import*
pygame.init()

window_size = (700, 700)
win = pygame.display.set_mode(window_size)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

colliders = []
balls = []

def temp_function(ball):
    pos = ball.circle.pos
    radius = ball.circle.radius
    if pos.x < -20:
        pos.randpos(window_size)
        return
    if pos.y < -20:
        pos.randpos(window_size)
        return
    if pos.x > window_size[0]+radius:
        pos.randpos(window_size)
        return
    if pos.y > window_size[1]+radius:
        pos.randpos(window_size)

for _ in range(8):
    ball = Ball(Vector2(randint(100, window_size[0] - 100), randint(100, window_size[1] - 100)))
    balls.append(ball)
    colliders.append(ball.collider)
balls[0].circle.color = (200, 255, 200)

def push_ball(ball : Ball, normalize : bool = False, force_multiplier : float = 15, random_pos : bool = False):
    if random_pos:
        v = Vector2()
        v.randpos(window_size)
        force = v - balls[0].rigid_body.position
    else:
        x, y = pygame.mouse.get_pos()
        force = Vector2(x, y) - balls[0].rigid_body.position
    if normalize:
        force.normalize()
    force *= force_multiplier

    ball.rigid_body.add_force(force)

while True:
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                push_ball(balls[0])

            if event.key == pygame.K_LCTRL:
                push_ball(balls[0], True, 10_000, True)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                push_ball(balls[0], True, 4000)

    for ball in balls:
        ball.update(0.016)

    resolve_all_collisions(colliders)

    for ball in balls:
        ball.draw(win)
        temp_function(ball)

    pygame.display.update()