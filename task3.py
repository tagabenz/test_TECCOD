"""
Создать класс Point, который представляет собой точку в двумерном пространстве. 
Класс должен иметь методы для инициализации координат точки, 
вычисления расстояния до другой точки, а также для получения и изменения координат.
"""

class Point():
    def __init__(self, x,y):
        self.x=x
        self.y=y

    def set_cords(self, x, y):  
        self.x=x
        self.y=y

    def get_cords(self):
        return self.x, self.y

    def distance(self, to):
        return f"{self.x-to.x}, {self.y-to.y}"

    