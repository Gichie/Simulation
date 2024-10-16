from project.simulation.actions import Actions
from project.simulation.Map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.CreatingObjects import CreatingObjects



class Simulation:
    Actions.creature()
    map = Map(Setting().width, Setting().height)
    Render.display(Map, map.create_map())
    print(CreatingObjects.creating_objects)






if __name__ == '__main__':
    Simulation()



