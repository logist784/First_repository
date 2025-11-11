import math

side = int(input("Укажите сторону: "))


def square(side):
    area = side * side
    if side % 2 != 0:
        area = math.ceil(area)
    return area


print("Площадь квадрата:", square(side))
