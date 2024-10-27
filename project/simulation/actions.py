from project.entity.Creatures.herbivore import Herbivore
from project.entity.Creatures.Predator import Predator
from project.entity.Static_objects.Grass import Grass
from project.entity.Static_objects.Rock import Rock
from project.entity.Static_objects.Tree import Tree
from project.simulation.creatingObjects import CreatingObjects
from project.setting import Setting
from random import shuffle


class Actions:
    '''Список действий, исполняемых перед стартом симуляции или на каждом ходу '''


    class CreateCoordsCreatures:
        coords = [(i,j) for j in range(Setting.height) for i in range(Setting.width)]
        shuffle(coords)
        # Отображение распределенных координат в случайном порядке
        # print(coords)


    def creature(self):
        self.create_object('Grss', Setting.count_grass)
        self.create_object('Rock', Setting.count_rock)
        self.create_object('Tree', Setting.count_tree)
        self.create_object('Herb', Setting.count_herbivore, Setting.speed, Setting.hp)
        self.create_object('Pred', Setting.count_predator, Setting.speed, Setting.hp, Setting.pred_strength)

    @staticmethod
    def create_object(object_type, count, *args):
        for i in range(count):
            x, y = __class__.CreateCoordsCreatures.coords.pop() \
            # Создание объекта в зависимости от переданного типа
            if object_type == 'Grss':
                obj = Grass(x, y)
                CreatingObjects.grasses.append(obj)
            elif object_type == 'Rock':
                obj = Rock(x, y)
            elif object_type == 'Tree':
                obj = Tree(x, y)
            elif object_type == 'Herb':
                obj = Herbivore(x, y, *args)
            elif object_type == 'Pred':
                obj = Predator(x, y, *args)
            else:
                raise ValueError(f"Unknown object type: {object_type}")

            CreatingObjects.creating_objects.append(obj)

            # Добавляем в движущиеся существа, если это травоядное или хищник
            if object_type in ['Herb', 'Pred']:
                CreatingObjects.moving_creatures.append(obj)
