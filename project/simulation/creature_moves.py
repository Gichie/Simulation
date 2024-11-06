from project.entity.creatures.herbivore import Herbivore
from project.entity.static_objects.grass import Grass
from project.setting import Setting
from project.simulation.breadth_first_search import Bfs
from project.simulation.creating_objects import CreatingObjects
from project.simulation.move_counter import MoveCounter


class CreatureMove:
    def __init__(self, map: dict[tuple[int, int]], render: 'Render', setting: Setting):
        self.map = map
        self.render = render
        self.setting = setting

    def moves(self) -> None:
        goals = {'Herb': Grass, 'Pred': Herbivore}
        for creature in CreatingObjects.moving_creatures:
            print()
            animal = Bfs((creature.x, creature.y), self.map, self.setting)
            self.__path_of_animal = animal.bfs(goals[creature._name])
            creature.make_move(self.__path_of_animal, self.map)
            self.render.display()
        print(CreatingObjects.moving_creatures)
        print(MoveCounter.move_counter())
        print()
