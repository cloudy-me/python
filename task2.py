class Road:

    def asphalt_weight(self, _length, _width):
        cover = 25
        height = 5
        weight = _length * _width * cover * height
        print(f'Asphalt weight is {_length}m * {_width}m * {cover}kg * {height}cm = {int(weight/1000)}t')


a = Road()
a.asphalt_weight(20, 5000)
