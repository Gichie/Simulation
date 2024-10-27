from project.simulation.actions import Actions
from project.simulation.Map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creature_moves import CreatureMove
from project.simulation.creatingObjects import CreatingObjects
from project.simulation.move_counter import MoveCounter

class Simulation:
    def __init__(self):
        Actions().creature()
        self.map = Map(Setting.width, Setting.height)
        Render.display(self.map)

    def next_step(self):
        '''Метод для симуляции и рендеринга одного хода для всех существ'''
        for i in range(2):
            CreatureMove(sim.map).moves()
            print(MoveCounter.move_counter())


if __name__ == '__main__':
    sim = Simulation()
    sim.next_step()
