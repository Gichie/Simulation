from project.simulation.actions import Actions
from project.simulation.map import Map
from project.setting import Setting
from project.simulation.render import Render
from project.simulation.creature_moves import CreatureMove
from project.simulation.creating_objects import CreatingObjects
import threading


class Simulation:
    def __init__(self):
        setting = Setting()
        Actions(setting).creature()
        self.map = Map(setting.width, setting.height).map
        print(CreatingObjects.moving_creatures)
        self.render = Render(setting.width, setting.height, self.map)
        self.creature_move = CreatureMove(self.map, self.render)
        self.pause_event = threading.Event()  # Флаг для паузы
        self.render.display()

    def start_simulation(self):
        '''Метод, запускающий бесконечный цикл симуляции и рендеринга'''

        # Устанавливаем паузу по умолчанию как "неактивную"
        self.pause_event.set()

        # Запускаем поток для отслеживания ввода команд
        threading.Thread(target=self.wait_for_commands, daemon=True).start()

        while CreatingObjects.moving_creatures:
                self.pause_event.wait()
                self.next_step()

    def next_step(self):
        '''Метод для симуляции и рендеринга одного хода для всех существ'''
        self.creature_move.moves()

    def pause(self):
        '''Приостанавливаем симуляцию'''
        print("Симуляция приостановлена.")
        self.pause_event.clear()

    def resume(self):
        '''Возобновляем симуляцию'''
        print("Симуляция возобновлена.")
        self.pause_event.set()

    def wait_for_commands(self):
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
    #sim.next_step()
    sim.start_simulation()
