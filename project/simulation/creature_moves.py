from project.simulation.creating_objects import CreatingObjects
from project.simulation.breadth_first_search import Bfs
from project.simulation.render import Render


class CreatureMove:
    def __init__(self, map):
        self.map = map

    def moves(self):
        goals = {'Herb': 'Grss', 'Pred': 'Herb'}
        for creature in CreatingObjects.moving_creatures:
            print(f'Ходит {creature} со скоростью {creature.speed}')
            animal = Bfs((creature.x, creature.y), self.map)
            self.__path_of_animal = animal.bfs(goals[creature.name])
            if not self.__path_of_animal:
                print(f'{creature}{creature.x, creature.y} больше некуда идти :(')
            else:
                print(f'Его путь: {self.__path_of_animal}')
                creature.make_move(self.__path_of_animal, self.map.map)
                print()
                Render.display(self.map)
