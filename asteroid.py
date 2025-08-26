from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.radius = radius
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self, dt):
        self.position += (self.velocity *dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            a1 = Asteroid(self.position[0], self.position[1],self.radius-ASTEROID_MIN_RADIUS)
            a2 = Asteroid(self.position[0], self.position[1],self.radius-ASTEROID_MIN_RADIUS)
            a1.velocity=(self.velocity*1.2).rotate(angle)
            a2.velocity=(self.velocity*1.2).rotate(-angle)
            
            self.velocity.rotate