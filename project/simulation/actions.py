from project.entity.creatures.herbivore import Herbivore
from project.entity.creatures.predator import Predator
from project.entity.static_objects.grass import Grass
from project.entity.static_objects.rock import Rock
from project.entity.static_objects.tree import Tree
from project.simulation.creating_objects import CreatingObjects
from project.setting import Setting
from random import shuffle


class Actions:
    '''Список действий, исполняемых перед стартом симуляции или на каждом ходу '''
    def __init__(self, setting: Setting):
        self.setting = setting
        self.coords = self.create_coords_creatures()

    def create_coords_creatures(self):
        coords = [(i,j) for j in range(self.setting.height) for i in range(self.setting.width)]
        shuffle(coords)
        return coords
        # Отображение распределенных координат в случайном порядке

    def creature(self):
        self.create_object('Grss', self.setting.count_grass)
        self.create_object('Rock', self.setting.count_rock)
        self.create_object('Tree', self.setting.count_tree)
        self.create_object('Herb', self.setting.count_herbivore)
        self.create_object('Pred', self.setting.count_predator)

    def create_object(self, object_type, count):
        for i in range(count):
            x, y = self.coords.pop()
            # Создание объекта в зависимости от переданного типа
            if object_type == 'Grss':
                obj = Grass(x, y)
            elif object_type == 'Rock':
                obj = Rock(x, y)
            elif object_type == 'Tree':
                obj = Tree(x, y)
            elif object_type == 'Herb':
                speed = self.setting.determines_speed()
                hp = self.setting.determines_health(object_type)
                obj = Herbivore(x, y, speed, hp)
            elif object_type == 'Pred':
                speed = self.setting.determines_speed()
                hp = self.setting.determines_health(object_type)
                strengh = self.setting.determines_strength(object_type)
                obj = Predator(x, y, speed, hp, strengh)
            else:
                raise ValueError(f"Unknown object type: {object_type}")

            CreatingObjects.creating_objects.append(obj)

            # Добавляем в движущиеся существа, если это травоядное или хищник
            if object_type in ['Herb', 'Pred']:
                CreatingObjects.moving_creatures.append(obj)
