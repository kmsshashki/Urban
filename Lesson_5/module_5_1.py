class House:
    def __init__(self, name, count_floors: int):
        self.name = name
        self.number_of_floors = count_floors

    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor < 1:
            return print('Такого этажа не существует')
        for floor in range(1, new_floor + 1):
            print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
