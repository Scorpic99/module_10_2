import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.counter = 0

    def timer(self):
        army = 100
        while army > 0:
            time.sleep(1)
            self.counter += 1
            army -= self.power
            print(f'{self.name}, сражается {self.counter} день(дня)..., осталось {army} воинов. ')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.timer()
        print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')




