from project.Entity.Creatures.Herbivore import Herbivore
from project.Entity.Static_objects.Grass import Grass
from project.Simulation.Map import Map
from project.Simulation.CreatingObjects import CreatingObjects
import random

class Actions:
    '''Список действий, исполняемых перед стартом симуляции или на каждом ходу '''
    pass
    class CreateHerbivores:
        w = random.randint(0, Map.width)
        h = random.randint(0, Map.height)
        herbivore = Herbivore(1, 1, 1, 10)
        CreatingObjects.creating_objects.append(herbivore)

    class CreateGrass:
        grass = Grass(0, 0)
        CreatingObjects.creating_objects.append(grass)
