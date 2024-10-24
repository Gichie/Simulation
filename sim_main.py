from project.simulation.actions import Actions
from project.simulation.Map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creature_moves import CreatureMove
from project.simulation.creatingObjects import CreatingObjects
from project.simulation.move_counter import MoveCounter

class Simulation:
    def __init__(self):
        actions = Actions()
        creating_objects = actions.creature()
        self.map = Map(Setting.width, Setting.height)
        Render.display(self.map, self.map.create_map(creating_objects))


    def next_step(self):
        print(CreatingObjects.creating_objects)
        print(CreatingObjects.moving_creatures)
        print(CreatingObjects.grasses)
        '''Метод для симуляции и рендеринга одного хода для всех существ'''
        for i in range(2):
            CreatureMove(sim.map).moves()
            print(MoveCounter.move_counter())





if __name__ == '__main__':
    sim = Simulation()
    sim.next_step()
