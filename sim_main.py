from project.simulation.actions import Actions
from project.simulation.map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creature_moves import CreatureMove
from project.simulation.creating_objects import CreatingObjects
from project.simulation.move_counter import MoveCounter

class Simulation:
    def __init__(self):
        setting = Setting()
        Actions(setting).creature()
        self.map = Map(setting.width, setting.height)
        Render(setting.width, setting.height, self.map).display()

    def next_step(self):
        '''Метод для симуляции и рендеринга одного хода для всех существ'''
        for i in range(2):
            CreatureMove(sim.map).moves()
            print(MoveCounter.move_counter())
            print()


if __name__ == '__main__':
    sim = Simulation()
    sim.next_step()
