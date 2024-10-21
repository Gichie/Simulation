from project.Entity.Creatures.Creature import Creature
from project.Entity.Creatures.herbivore import Herbivore
from project.Entity.Creatures.Predator import Predator
from project.Entity.Static_objects.Grass import Grass
from project.Entity.Static_objects.Rock import Rock
from project.Entity.Static_objects.Tree import Tree
from project.simulation.creatingObjects import CreatingObjects
from project.simulation.breadth_first_search import Bfs
from project.simulation.Map import Map
from project.setting import Setting
from random import shuffle


class Actions:
    '''Список действий, исполняемых перед стартом симуляции или на каждом ходу '''
    def __init__(self):
        self._creating_objects = CreatingObjects()


    class CreateCoordsCreatures:
        coords = [(i,j) for j in range(Setting.height) for i in range(Setting.width)]
        shuffle(coords)
        # Отображение распределенных координат в случайном порядке
        # print(coords)


    def creature(self):
        self.create_herbivores(self._creating_objects)
        self.create_predators(self._creating_objects)
        self.create_grasses(self._creating_objects)
        self.create_rocks(self._creating_objects)
        self.create_trees(self._creating_objects)
        return self._creating_objects


    @staticmethod
    def create_grasses(creating_objects):
        for i in range(Setting.count_grass):
            x, y = __class__.CreateCoordsCreatures.coords.pop()
            grass = Grass(x, y)
            creating_objects.creating_objects.append(grass)

    @staticmethod
    def create_rocks(creating_objects):
        for i in range(Setting.count_rock):
            x, y = __class__.CreateCoordsCreatures.coords.pop()
            rock = Rock(x, y)
            creating_objects.creating_objects.append(rock)

    @staticmethod
    def create_trees(creating_objects):
        for i in range(Setting.count_tree):
            x, y = __class__.CreateCoordsCreatures.coords.pop()
            tree = Tree(x, y)
            creating_objects.creating_objects.append(tree)

    @staticmethod
    def create_herbivores(creating_objects):
        '''Метод для создания травоядных существ'''
        for i in range(Setting.count_herbivore):
            x, y = __class__.CreateCoordsCreatures.coords.pop()
            herbivore = Herbivore(x, y, Setting.speed, Setting.hp)
            creating_objects.creating_objects.append(herbivore)
            creating_objects.moving_creatures.append(herbivore)

    @staticmethod
    def create_predators(creating_objects):
        for i in range(Setting.count_predator):
            if __class__.CreateCoordsCreatures.coords:
                x, y = __class__.CreateCoordsCreatures.coords.pop()
                predator = Predator(x, y, Setting.speed, Setting.hp, Setting.pred_strength)
                creating_objects.creating_objects.append(predator)
                creating_objects.moving_creatures.append(predator)
            else:
                break

