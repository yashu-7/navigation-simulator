import pygame
import random
from go_to_goal import linear_angular,move_towards_goal

pygame.init()

WIDTH = 640
HEIGHT = 480

bot_img = pygame.image.load('idle.png')

class Robot():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 3  
        self.angle = 0  
        self.turn_rate = 4  

class Object():
    def __init__(self, x, y):
        self.color = (255, 0, 0)
        self.x = x
        self.y = y
        self.radius = 7

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

robo = Robot(0, 0, 40, 40)
goal_x = random.randint(10, WIDTH-7)
goal_y = random.randint(10, HEIGHT-7)
goal = Object(goal_x, goal_y)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SIMULATOR")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)

def check_goal_reached(r_x, r_y, g_x, g_y):
    distance = ((r_x - g_x) ** 2 + (r_y - g_y) ** 2) ** 0.5

    if distance < robo.w // 2:  
        new_goal_x = random.randint(10, WIDTH - 7)
        new_goal_y = random.randint(10, HEIGHT - 7)
        return new_goal_x, new_goal_y
    return None

def update():
    window.fill((86, 181, 255))
    goal.draw(window)
    
    rotated_img = pygame.transform.rotate(bot_img, -robo.angle)
    new_rect = rotated_img.get_rect(center=(robo.x + robo.w // 2, robo.y + robo.h // 2))
    
    window.blit(rotated_img, new_rect.topleft)

    text_surface = font.render(f"Distance to goal: {dis:.4}", True, (0, 0, 0))
    window.blit(text_surface, (10, 10))
    
    pygame.display.flip()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    robo_c_x = robo.x + robo.w // 2
    robo_c_y = robo.y + robo.h // 2

    dis, ori = linear_angular(robo_c_x, robo_c_y, goal.x, goal.y)

    robo.x,robo.y = move_towards_goal(robo, ori)
    robo.x
    robo.y
    new_goal = check_goal_reached(robo_c_x, robo_c_y, goal.x, goal.y)
    if new_goal:
        goal.x, goal.y = new_goal

    update()

pygame.quit()