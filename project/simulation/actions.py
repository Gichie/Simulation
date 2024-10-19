from project.Entity.Creatures.herbivore import Herbivore
from project.Entity.Creatures.Predator import Predator
from project.Entity.Static_objects.Grass import Grass
from project.Entity.Static_objects.Rock import Rock
from project.Entity.Static_objects.Tree import Tree
from project.simulation.creatingObjects import CreatingObjects
from project.setting import Setting
from random import shuffle


class Actions:
    '''Список действий, исполняемых перед стартом симуляции или на каждом ходу '''

    class CreateCoordsCreatures:
        coords = [(i,j) for j in range(Setting.width) for i in range(Setting.height)]
        shuffle(coords)
        # Отображение распределенных координат в случайном порядке
        # print(coords)

    @classmethod
    def creature(cls):
        cls.create_herbivores()
        cls.create_predators()
        cls.create_grasses()
        cls.create_rocks()
        cls.create_trees()



    @staticmethod
    def create_grasses():
        for i in range(Setting.count_grass):
            x, y = __class__.CreateCoordsCreatures.coords.pop()
            grass = Grass(x, y)
            CreatingObjects.creating_objects.append(grass)

    @staticmethod
    def create_rocks():
        for i in range(Setting.count_rock):
            x, y = __class__.CreateCoordsCreatures.coords.pop()
            rock = Rock(x, y)
            CreatingObjects.creating_objects.append(rock)

    @staticmethod
    def create_trees():
        for i in range(Setting.count_tree):
            x, y = __class__.CreateCoordsCreatures.coords.pop()
            tree = Tree(x, y)
            CreatingObjects.creating_objects.append(tree)

    @staticmethod
    def create_herbivores():
        '''Метод для создания травоядных существ'''
        for i in range(Setting.count_herbivore):
            x, y = __class__.CreateCoordsCreatures.coords.pop()
            herbivore = Herbivore(x, y, Setting.speed, Setting.hp)
            CreatingObjects.creating_objects.append(herbivore)

    @staticmethod
    def create_predators():
        for i in range(Setting.count_predator):
            if __class__.CreateCoordsCreatures.coords:
                x, y = __class__.CreateCoordsCreatures.coords.pop()
                predator = Predator(x, y, Setting.speed, Setting.hp, Setting.pred_strength)
                CreatingObjects.creating_objects.append(predator)
            else:
                break
