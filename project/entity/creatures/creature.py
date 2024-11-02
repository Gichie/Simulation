from project.entity.entity import Entity
from abc import abstractmethod
from project.entity.static_objects.empty import Empty
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

    def move(self, path_of_animal: list[tuple[int, int]], map: dict[tuple[int, int], 'Creature']) -> None:
        # Существо движется к ближайшей цели(по поиску в ширину) со своей скоростью
        # Получение новой позиции на основе скорости
        target_index = min(self.speed, len(path_of_animal) - 2)
        target_position = path_of_animal[target_index]

        # Обновление позиции и карты
        old_position = (self.x, self.y)
        self.x, self.y = target_position
        map[target_position] = self
        print(f'{self.name} походил {old_position} -> {self.x, self.y}')

        # Обновление старого положения, если оно не пустое
        map[old_position] = Empty(*old_position)

    def __str__(self) -> str:
        return self.name