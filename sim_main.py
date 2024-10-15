from project.Simulation.actions import Actions
from project.Simulation.Map import Map
from project.setting import Setting


class Simulation:
    Actions.creature()
    map = Map(Setting().width, Setting().height)
    map.create_map()
    map.display_map()



if __name__ == '__main__':
    Simulation()



