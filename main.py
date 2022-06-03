import sys, pygame
pygame.init()

# Window Size
size = width, height = 800, 400

# This actually indicates where the ball should move in one iteration
speed = [1, 1]
background = 255, 255, 255
# Set size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")
ball = pygame.image.load("ball.png")
# Turn the image into a rectangle in PyGame
ball_rect = ball.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Each time, the ball will move according to speed [x, y]
    ball_rect = ball_rect.move(speed)
    # Bounce Effect
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]
    # Fill screen with white background
    screen.fill(background)
    screen.blit(ball, ball_rect)
    #Update display
    pygame.display.flip()
