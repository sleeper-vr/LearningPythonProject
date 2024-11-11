from math import trunc


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor):
                print(floor)

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return  self.number_of_floors == other.number_of_floors
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return  self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return  self.number_of_floors < other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return  self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return  self.number_of_floors <= other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return  self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return  self.number_of_floors > other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return  self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return  self.number_of_floors >= other
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return  self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return  self.number_of_floors != other
        else:
            return NotImplemented

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return NotImplemented

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        return self + value

    def __sub__(self, value):
        if isinstance(value, House):
            self.number_of_floors -= value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors -= value
            return self
        else:
            return NotImplemented

    def __isub__(self, other):
        return self - other

    def __rsub__(self, other):
        return other - self.number_of_floors

    def __mul__(self, value):
        if isinstance(value, House):
            self.number_of_floors *= value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors *= value
            return self
        else:
            return NotImplemented

    def __truediv__(self, value):
        if isinstance(value, House):
            self.number_of_floors = trunc(self.number_of_floors/value.number_of_floors)
            return self
        elif isinstance(value, int):
            self.number_of_floors = trunc(self.number_of_floors/value)
            return self
        else:
            return NotImplemented


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)