print("Brenda Kouam")

import pygame
import sys

print("12-2")
class Character:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("person1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Center of the screen
        self.rect.center = self.screen_rect.center

    def draw(self):
        self.screen.blit(self.image, self.rect)


print("12-4")
class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("space rocket.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start rocket below the character
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 150

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        "Move rocket but keep it inside the screen."
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 2
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 2
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 2

    def draw(self):
        self.screen.blit(self.image, self.rect)


print("12-1")

def run_game():

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("All Exercises 12-1 to 12-5")

    BLUE = (135, 206, 250)

    # Game objects
    character = Character(screen)   
    rocket = Rocket(screen)        

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            print("12-5")
            if event.type == pygame.KEYDOWN:
                print("KEY PRESSED:", event.key)

                # Rocket movement
                if event.key == pygame.K_UP:
                    rocket.moving_up = True
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = True
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    rocket.moving_up = False
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = False
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = False

        rocket.update()

        # Draw everything
        screen.fill(BLUE)
        character.draw()
        rocket.draw()

        pygame.display.flip()


# Run the game
run_game()