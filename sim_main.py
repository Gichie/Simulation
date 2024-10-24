from project.simulation.actions import Actions
from project.simulation.Map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creature_moves import CreatureMove
from project.simulation.creatingObjects import CreatingObjects

class Simulation:
    def __init__(self):
        actions = Actions()
        creating_objects = actions.creature()
        self.map = Map(Setting.width, Setting.height)
        Render.display(self.map, self.map.create_map(creating_objects))


    def next_step(self):
        '''Метод для симуляции и рендеринга одного хода для всех существ'''
        print(CreatingObjects.moving_creatures)
        CreatureMove(sim.map).moves()
        print()
        print(CreatingObjects.moving_creatures)


if __name__ == '__main__':
    sim = Simulation()
    sim.next_step()
