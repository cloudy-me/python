from itertools import cycle
import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for el in cycle(self.__color):
            print(el)
            if el == 'red':
                time.sleep(7)
            elif el == 'yellow':
                time.sleep(2)
            else:
                time.sleep(1)


traffic = TrafficLight()
traffic.running()
