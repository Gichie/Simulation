from project.simulation.actions import Actions
from project.simulation.map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creature_moves import CreatureMove
from project.simulation.creating_objects import CreatingObjects
from project.simulation.move_counter import MoveCounter
import time
from project.entity.creatures.predator import Predator

class Simulation:
    def __init__(self):
        setting = Setting()
        Actions(setting).creature()
        self.map = Map(setting.width, setting.height).map
        print(CreatingObjects.moving_creatures)
        self.render = Render(setting.width, setting.height, self.map)
        self.render.display()

    def next_step(self):
        '''Метод для симуляции и рендеринга одного хода для всех существ'''

        while CreatingObjects.moving_creatures:
            if Predator in map(type, CreatingObjects.moving_creatures):
                CreatureMove(sim.map, self.render).moves()
                print(CreatingObjects.moving_creatures)
                print(MoveCounter.move_counter())
                print()
                time.sleep(0.001)


if __name__ == '__main__':
    sim = Simulation()
    sim.next_step()
