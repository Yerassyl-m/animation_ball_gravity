import pygame
import math

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

# Set up the window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Set up the ball
ball_radius = 30
initial_x = ball_x = 50
initial_y = ball_y = 30 + ball_radius
initial_vy = ball_vy = 0
initial_vx = ball_vx = 5
rho = 1.2255
v = 2
A = 4
Cd = 1.48
ball_color = (0, 128, 128)
air_resistance = 5


# Set up the gravity
gravity = 0.98
start = False
end = False

# Set up the clock
clock = pygame.time.Clock()

# Main game loop

# text
textx = 400
texty = initial_y
font = pygame.font.Font('freesansbold.ttf', 16)
speedText = font.render(f"X Speed: {ball_vx}", True, green, black)
gravityText = font.render(f"Gravity: {10 * gravity}", True, green, black)
gravityTextRect = gravityText.get_rect()
speedTextRect = speedText.get_rect()

# set the center of the rectangular object.
speedTextRect.center = (textx, texty + 100)
gravityTextRect.center = (textx, texty )

Air_resistance = 0.5 * rho * v**2 * A * Cd

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True
            if event.key == pygame.K_UP:
                ball_y = initial_y
                ball_x = initial_x
                ball_vx = initial_vx
                ball_vy = initial_vy
                end = False

    currSpeedText = font.render(f"Y Speed: {ball_vy}", True, green, black)
    currSpeedTextRect = currSpeedText.get_rect()
    currSpeedTextRect.center = (textx, texty + 50)

    if start:
        # Update the ball's position
        ball_y += ball_vy
        ball_vy += gravity/air_resistance
        ball_x += ball_vx/air_resistance

        # Check for collisions with the bottom of the screen
        if ball_y + ball_radius > height:
            ball_vy = -ball_vy * 0.8
            ball_y = height - ball_radius
            if end:
                start = False
        if ball_x + ball_radius + ball_vx == width:
            ball_vx = 0
            end = True

    # Clear the screen
    screen.fill(black)

    screen.blit(speedText, speedTextRect)
    screen.blit(currSpeedText, currSpeedTextRect)
    screen.blit(gravityText, gravityTextRect)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, int(ball_y)), ball_radius)

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)
