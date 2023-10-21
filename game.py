import pgzrun
import pygame
import secrets

pygame.mouse.set_visible(False)

WIDTH = 840
HEIGHT = 600


target = Actor('target_red1')
target.x = 100
target.y = 200

target2 = Actor('target_red2')
target2.right = WIDTH
target2.top = 0


target3 = Actor('target_red3')
target3.center = WIDTH/2, 0
target3.bottom = HEIGHT


cursor = Actor('crosshair_outline_large')
cursor.score = 0

def on_mouse_move(pos):
    cursor.pos = pos

def on_mouse_down(pos):
    if cursor.colliderect(target):
        target.right = 0
        target.y = secrets.randbelow(HEIGHT)
        cursor.score += 10
    if cursor.colliderect(target2):
        target2.right = 0
        target2.y = secrets.randbelow(HEIGHT)
        cursor.score -= 5
    if cursor.colliderect(target3):
        target3.left = 0
        target3.y = secrets.randbelow(HEIGHT)
        cursor.score += 5


# runs 60 times per second
def update():
    target.x += 5 + cursor.score / 2
    target2.x += 5 + cursor.score / 2
    target3.x -= 5 + cursor.score / 2

    if target.left > WIDTH:
        target.right = 0

    if target2.left > WIDTH:
        target2.right = 0

    if target3.right < 0:
        target3.left = WIDTH

    


def draw():
    screen.clear()
    screen.draw.text(f'Score: {cursor.score}', (10, 10), color = 'white', fontsize = 30)
    target.draw()
    target2.draw()
    target3.draw()
    cursor.draw()


pgzrun.go()
