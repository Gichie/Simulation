from project.simulation.actions import Actions
from project.simulation.Map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creature_moves import CreatureMove




class Simulation:
    def __init__(self):
        Actions.creature()
        self.map = Map(Setting.width, Setting.height)
        Render.display(self.map, self.map.create_map())


if __name__ == '__main__':
    sim = Simulation()
    creature_move = CreatureMove(sim.map)
    creature_move.moves()



