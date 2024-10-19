from project.simulation.creatingObjects import CreatingObjects
from project.simulation.breadth_first_search import Bfs

class CreatureMove:
    def __init__(self, map):
        self.map = map

    def moves(self):
        goals = {'Herb': 'Grss', 'Pred': 'Herb'}
        for creature in CreatingObjects.moving_creatures:
            for kind_of_animal in goals:
                if creature.name == kind_of_animal:
                    animal = Bfs((creature.x, creature.y), self.map)
                    print(animal.bfs(goals[kind_of_animal]))

