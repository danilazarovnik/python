class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self._length * self._width * self.weigth * self.tickness / 1000
        print(f'Нужно {intake} тонн асфальта для строительства дороги')


road_to_village = Road(20000, 6)
road_to_village.intake()
