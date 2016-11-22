import math
class Shape(object):
    def __init__(self, item):
        self.item = item

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def to_string(self):
        pass

    def draw(self):
        pass

class Rectangular(Shape):
    """"R"""
    def __init__(self, width, lenght):
        super(Rectangular, self).__init__(width)
        self.width = self.item
        self.lenght = lenght

    def get_area(self):
        return self.width * self.lenght

    def get_perimeter(self):
        return 2 * (self.width + self.lenght)

class Circle(Shape):

    def __init__(self, radius):
        super(Circle, self).__init__(radius)
        self.radius = self.item

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):

    def __init__(self, side):
        super(Square, self).__init__(side)
        self.side = self.item

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

class Triangle(Shape):

    def __init__(self, point1, point2, point3):
        super(Triangle, self).__init__(point1)
        self.point1 = Point(self.item)
        self.point2 = Point(point2)
        self.point3 = Point(point3)
        x = self.point1.point

    def get_area(self):
        half_of_perimeter = self.get_perimeter() / 2
        len1_2 = self.point1.get_distance(self.point2.point)
        len2_3 = self.point2.get_distance(self.point3.point)
        len3_1 = self.point3.get_distance(self.point1.point)
        return math.sqrt(half_of_perimeter * (half_of_perimeter - len1_2) * (half_of_perimeter - len2_3) * (half_of_perimeter - len3_1))

    def get_perimeter(self):
        len1_2 = self.point1.get_distance(self.point2.point)
        len2_3 = self.point2.get_distance(self.point3.point)
        len3_1 = self.point3.get_distance(self.point1.point)
        return len1_2 + len2_3 + len3_1

class Point(object):

    def __init__(self, point):
        self.point = point

    def get_distance(self, point2):
        delta_x = abs(self.point[0])
        delta_x = delta_x - abs(point2[0])
        delta_y = abs(self.point[1]) - abs(point2[1])
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

if __name__ =='__main__':
    sq = Square(3)
    rect = Rectangular(2, 4)
    circle = Circle(3)
    triangle = Triangle([0,0], [3,3], [5,5])
    point = Point([1,3])
    print point.get_distance([1,7])
    triangle = Triangle([0, 0], [3, 3], [0, 3])
    triangle.get_perimeter()
    triangle.get_area()
    print triangle.get_perimeter(), triangle.get_area(), sq.get_area()

