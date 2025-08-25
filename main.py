import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables,drawables)
    AsteroidField.containers = (updatables)
    clock = pygame.time.Clock()
    dt=0
    af = AsteroidField()
    p1 = Player(SCREEN_WIDTH/2.0, SCREEN_HEIGHT/2.0)
    while 1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) /1000
        



if __name__ == "__main__":
    main()
