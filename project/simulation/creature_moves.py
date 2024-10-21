from project.simulation.creatingObjects import CreatingObjects
from project.simulation.breadth_first_search import Bfs
from project.simulation.render import Render

class CreatureMove:
    def __init__(self, map):
        self.map = map


    def update_map(self, creature_name):
        print(self.__path_of_animal)
        self.map.map[self.__path_of_animal[0]] = '(..)'
        self.map.map[self.__path_of_animal[1]] = creature_name

    def moves(self):
        goals = {'Herb': 'Grss', 'Pred': 'Herb'}
        for creature in CreatingObjects.moving_creatures:
            animal = Bfs((creature.x, creature.y), self.map)
            self.__path_of_animal = animal.bfs(goals[creature.name])
            if not self.__path_of_animal:
                print('Существу больше некуда идти')
            else:
                self.update_map(creature.name)
                print()

                Render(self.map).display(self.map.map)


