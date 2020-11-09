class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def __init__(self, title='Pen'):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def __init__(self, title='Pencil'):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):
    def __init__(self, title='Handle'):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки маркером.')


pen = Pen()
print(pen.title)
pen.draw()

pencil = Pencil()
print(pencil.title)
pencil.draw()

handle = Handle()
print(handle.title)
handle.draw()
