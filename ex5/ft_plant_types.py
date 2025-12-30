class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color

    def bloom(self):
        print(f"{self._name} is blooming beautifully!")

    def print(self):
        print(f"{self._name} (Flower): {self._height}cm,", end="")
        print(f" {self._age} days, {self._color} color")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self._name} provides ", end="")
        shade = int(3.14 * self._trunk_diameter * self._trunk_diameter / 100)
        print(f"{shade} ", end="")
        print("square meters of shade")

    def print(self):
        print(f"{self._name} (Tree): {self._height}cm, ", end="")
        print(f"{self._age} days, {self._trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def print(self):
        print(f"{self._name} (Vegetable): {self._height}cm, ", end="")
        print(f"{self._age} days, {self._harvest_season} harvest")

    def print_value(self):
        print(f"{self._name} is rich in {self._nutritional_value}")


def subject_exemple(plants):
    print("=== Garden Plant Types ===")
    print()
    plants[0].print()
    plants[0].bloom()
    print()
    plants[2].print()
    plants[2].produce_shade()
    print()
    plants[4].print()
    plants[4].print_value()


flowers = [
    ("Rose", 25, 30, "red"),
    ("Iris", 25, 30, "perpule")
]
trees = [
    ("Oak", 500, 1825, 50),
    ("Pine", 700, 1500, 55)
]
vegetables = [
    ("Tomato", 80, 90, "summer", "vitamin C"),
    ("Apple", 80, 90, "summer", "vitamin C")
]

plants = []
for name, height, age, color in flowers:
    plants.append(Flower(name, height, age, color))

for name, height, age, trunk_diameter in trees:
    plants.append(Tree(name, height, age, trunk_diameter))

for name, height, age, harvest_season, nutritional_value in vegetables:
    plants.append(
        Vegetable(
            name,
            height,
            age,
            harvest_season,
            nutritional_value))

subject_exemple(plants)
