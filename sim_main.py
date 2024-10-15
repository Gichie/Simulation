from project.Simulation.actions import Actions
from project.Simulation.Map import Map
from project.setting import Setting
from project.Simulation.render import Render


class Simulation:
    Actions.creature()
    map = Map(Setting().width, Setting().height)
    Render.display(Map, map.create_map())



if __name__ == '__main__':
    Simulation()



