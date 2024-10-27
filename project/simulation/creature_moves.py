from project.simulation.creatingObjects import CreatingObjects
from project.simulation.breadth_first_search import Bfs
from project.simulation.render import Render
from project.entity.Static_objects.Grass import Grass
from project.entity.Creatures.herbivore import Herbivore


class CreatureMove:
    def __init__(self, map):
        self.map = map

    def moves(self):
        goals = {'Herb': 'Grss', 'Pred': 'Herb'}
        for creature in CreatingObjects.moving_creatures:
            print(f'Ходит {creature}')
            animal = Bfs((creature.x, creature.y), self.map)
            self.__path_of_animal = animal.bfs(goals[creature.name])
            if not self.__path_of_animal:
                print(f'{creature}{creature.x, creature.y} больше некуда идти :(')
            else:
                print(f'Его путь: {self.__path_of_animal}')
                creature.make_move(self.__path_of_animal, self.map.map)
                print()
                Render.display(self.map)
