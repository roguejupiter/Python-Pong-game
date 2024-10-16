import pygame
import random


WIDTH, HEIGHT = 1200, 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
paddle_speed = 5

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface((10, 115))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        
    def move(self, speed):
        keys = pygame.key.get_pressed()
        
        if self.rect.x < HEIGHT/2:
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= speed
            if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
                self.rect.y += speed
        else:
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= speed
            if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += speed

left_paddle = Paddle(50, HEIGHT/2)
right_paddle = Paddle(WIDTH-50, HEIGHT/2)

paddles = pygame.sprite.Group()
paddles.add(left_paddle)
paddles.add(right_paddle)

ball_size = 25
ball = pygame.Rect(WIDTH/2 - ball_size // 2, HEIGHT/2 - ball_size // 2, ball_size, ball_size)
ball_speed_x, ball_speed_y = 4, 4

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle.rect) or ball.colliderect(right_paddle.rect):
        ball_speed_x *= -1.05
        paddle_speed = paddle_speed * 1.05
    
    if ball.left <= 0 or ball.right >= WIDTH:
        pygame.quit()
        
    left_paddle.move(paddle_speed)
    right_paddle.move(paddle_speed)

    paddles.draw(screen)
    pygame.draw.ellipse(screen, WHITE, ball)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()