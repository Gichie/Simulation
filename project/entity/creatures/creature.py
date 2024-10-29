from project.entity.entity import Entity
from abc import abstractmethod
from project.setting import Setting

class Creature(Entity):
    def __init__(self, x,y, speed: int, hp: int, engry: int):
        super().__init__(x,y)
        self.speed = speed
        self.full_hp = hp
        self.hp = hp
        self.engry = engry
        self.setting = Setting()

    @abstractmethod
    def make_move(self):
        pass