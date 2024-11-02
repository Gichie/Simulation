from project.simulation.creating_objects import CreatingObjects
from project.simulation.breadth_first_search import Bfs
from project.simulation.move_counter import MoveCounter


class CreatureMove:
    def __init__(self, map, render):
        self.map = map
        self.render = render

    def moves(self):
        goals = {'Herb': 'Grss', 'Pred': 'Herb'}
        for creature in CreatingObjects.moving_creatures[:]:
            print()
            animal = Bfs((creature.x, creature.y), self.map)
            self.__path_of_animal = animal.bfs(goals[creature.name])
            creature.make_move(self.__path_of_animal, self.map)
            self.render.display()
        print(CreatingObjects.moving_creatures)
        print(MoveCounter.move_counter())
        print()
