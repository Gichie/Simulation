import threading

from project.setting import Setting
from project.simulation.actions import Actions
from project.simulation.creating_objects import CreatingObjects
from project.simulation.creature_moves import CreatureMove
from project.simulation.map import Map
from project.simulation.render import Render


class Simulation:
    def __init__(self):
        """Инициализация симуляции, создание карты и объектов, установка паузы"""
        setting = Setting()
        Actions(setting).creature()

        self.map = Map(setting.width, setting.height).map
        self.render = Render(setting.width, setting.height, self.map)
        self.creature_move = CreatureMove(self.map, self.render, setting)
        self.pause_event = threading.Event()  # Флаг для управления паузой
        self.render.display()

    def start_simulation(self) -> None:
        """Запуск основного цикла симуляции с контролем паузы и потоком для команд"""
        self.pause_event.set()  # Устанавливаем событие для старта

        # Запускаем поток для отслеживания ввода команд
        threading.Thread(target=self.wait_for_commands, daemon=True).start()

        while CreatingObjects.moving_creatures:
            self.pause_event.wait()  # Ожидание до установки флага
            self.next_step()

    def next_step(self, num_steps=1) -> None:
        """Симуляция и рендеринг одного хода или переданное количество ходов для всех существ"""
        for _ in range(num_steps):
            self.creature_move.moves()

    def pause(self) -> None:
        '''Приостанавливаем симуляцию'''
        print("Симуляция приостановлена.")
        self.pause_event.clear()

    def resume(self) -> None:
        '''Возобновляем симуляцию'''
        print("Симуляция возобновлена.")
        self.pause_event.set()

    def wait_for_commands(self) -> None:
        '''Отслеживаем ввод команд для управления симуляцией'''
        while True:
            command = input("Введите команду ('pause' или 'resume'): ").strip().lower()
            if command == "pause":
                self.pause()
            elif command == "resume":
                self.resume()
            else:
                print("Неизвестная команда. Попробуйте 'pause' или 'resume'.")


if __name__ == '__main__':
    sim = Simulation()
    sim.start_simulation()
