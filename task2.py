from abc import ABC, abstractmethod

class MyAbstractClass(ABC):

    @abstractmethod
    def __init__(self, width, height):
        pass

    @abstractmethod
    def Textile(self):
        pass


class Clothes(MyAbstractClass):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def Textile(self):
        pass

    def __add__(self, other):
        return self.Textile + other.Textile


class Coat(Clothes):

    @property
    def Textile(self):
        textile = self.width / 6.5 + 0.5
        return textile


class Costume(Clothes):

    @property
    def Textile(self):
        textile = self.height * 2 + 0.3
        return textile


coat = Coat(10, 100)
print(f'For the Coat {round(coat.Textile)} sq. m. of textile is needed')

costume = Costume(10, 100)
print(f'For the Costume {round(costume.Textile)} sq. m. of textile is needed')

print(f'Total textile needed is {round(coat + costume)} sq.m')
