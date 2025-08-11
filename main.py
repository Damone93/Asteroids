import sys
import pygame
import os
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
pygame.font.init()

def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    score = 0
    score_increment = 10

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        score_obj = pygame.font.Font(None, 36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Score:", score)
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Score:", score)
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += score_increment

        screen.fill("white")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        score_text = score_obj.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        pygame.display.update()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()