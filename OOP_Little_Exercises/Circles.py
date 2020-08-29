# Python Exercise: A class constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circles:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = (self.radius ** 2) * 3.14
        return area

    def circumference(self):
        return self.radius * 2

if __name__ == '__main__':
    circle = Circles(3)
    print(f'area: {circle.area()}')
    print(f'circumference: {circle.circumference()}')