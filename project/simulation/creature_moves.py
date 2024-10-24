from project.simulation.creatingObjects import CreatingObjects
from project.simulation.breadth_first_search import Bfs
from project.simulation.render import Render

class CreatureMove:
    def __init__(self, map):
        self.map = map

    def update_map(self, creature):
        print(self.__path_of_animal)
        creature.make_move(self.__path_of_animal, self.map.map)

    def moves(self):
        goals = {'Herb': 'Grss', 'Pred': 'Herb'}
        for creature in CreatingObjects.moving_creatures:
            animal = Bfs((creature.x, creature.y), self.map)
            self.__path_of_animal = animal.bfs(goals[creature.name])
            if not self.__path_of_animal:
                print(f'{creature} больше некуда идти')
            else:
                self.update_map(creature)
                print()
                Render(self.map).display(self.map.map)
