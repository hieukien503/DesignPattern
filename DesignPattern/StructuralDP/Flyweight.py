import random

class Particle:
    def __init__(self, color: str, image: str):
        self.color = color
        self.sprite = image
    def move(self, coord: list[int], vector: list[int], speed: int) -> str:
        result = "Particle from coord ({}) to coord ({}) with speed {}".format(",".join([str(x) for x in coord]), ",".join(x for x in vector), speed)
    def draw(self, coord: list[int], canvas: str):
        print("Draw particle at coord ({}) in {}".format(",".join([str(x) for x in coord]), canvas))

class MovingParticle:
    def __init__(self, particle: Particle, coord: list[int], vector: list[int], spd: int):
        self.particle = particle
        self.coord = coord
        self.vector = vector
        self.spd = spd
    def move(self) -> str:
        return self.particle.move(self.coord, self.vector, self.spd)
    def draw(self, canvas):
        self.particle.draw(self.coord, canvas)

class Game:
    def __init__(self):
        self.mps = list()
        self.__particles = list()
    def add(self, coord: list[int], vector: list[int], speed: int, color: str, image: str):
        particle = Particle(color, image)
        self.__particles.append(particle)
        self.mps.append(MovingParticle(particle, coord, vector, speed))
    def draw(self, canvas):
        for x in self.mps:
            x.draw(canvas)

class Unit:
    def __init__(self, x: int, y: int):
        self.coord = list()
        self.coord.extend([x, y])
    def FireAt(self, target):
        print("Shoot unit at coordinate ({})".format(",".join([str(x) for x in target.coord])))

def ClientCode():
    game = Game()
    units = list()
    for x in range(10):
        coord, vector = [random.randrange(0, 800), random.randrange(0, 800)], [random.randrange(0, 800), random.randrange(0, 800)]
        speed = random.randrange(20, 30)
        color = 'red'
        sprite = 'bullet.png'
        game.add(coord, vector, speed, color, sprite)
        units.append(Unit(vector[0], vector[1]))
    game.draw(canvas = 'Figma')
    random.shuffle(units)
    for x in range(10):
        units[x].FireAt(random.choice(units))

if __name__ == '__main__':
    ClientCode()
    
        
