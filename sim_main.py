from project.simulation.actions import Actions
from project.simulation.map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creature_moves import CreatureMove
from project.simulation.creating_objects import CreatingObjects


class Simulation:
    def __init__(self):
        setting = Setting()
        Actions(setting).creature()
        self.map = Map(setting.width, setting.height).map
        print(CreatingObjects.moving_creatures)
        self.render = Render(setting.width, setting.height, self.map)
        self.creature_move = CreatureMove(self.map, self.render)
        self.render.display()

    def start_simulation(self):
        '''Метод, запускающий бесконечный цикл симуляции и рендеринга'''
        while CreatingObjects.moving_creatures:
            self.next_step()

    def next_step(self):
        '''Метод для симуляции и рендеринга одного хода для всех существ'''
        self.creature_move.moves()


if __name__ == '__main__':
    sim = Simulation()
    sim.next_step()
    sim.start_simulation()
