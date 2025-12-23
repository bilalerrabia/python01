class Plant:
    def __init__(self, name: str, age: int, height: int):
        self._name = name
        self._age = age
        self._height = height


class Flower(Plant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self._color = color
    def bloom(self):
        print(f"{self._name} is blooming beautifully!")
    def print(self):
        print(f"{self._name} (Flower): {self._height}cm, {self._age} days, {self._color} color")


class Tree(Plant):
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self._trunk_diameter = trunk_diameter
    def produce_shade(self):
        print(f"{self._name} provides 78 square meters of shade")
    def print(self):
        print(f"{self._name} (Tree): {self._height}cm, {self._age} days, {self._trunk_diameter}cm diamentre")


class Vegetable(Plant):
    def __init__(self, name, age, height, harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self._nutritional_value = nutritional_value
        self._harvest_season = harvest_season
    def print(self):
        print(f"{self._name} (Vegetable): {self._height}cm, {self._age} days, {self._harvest_season} ")
        print(f"{self._name} is rich in {self._nutritional_value}")


roses = [
    ("Rose", 30, 25, "red"),
    ("Helio", 35, 10, "yellow")
]
trees = [
    ("Oak", 1825, 500, 50),
    ("Sequoia", 365, 500, 40)
]
vegetables = [
    ("Tomato", 90, 80, "summer harvest","vitamin C"),
    ("Corn", 100, 210, "Late summer to early fall", "vitamin B")
]
i = 0
for rose in roses:
    roses[i] = Flower(rose[0], rose[1], rose[2], rose[3])
    i += 1
i = 0
for tree in trees:
    trees[i] = Tree(tree[0], tree[1], tree[2], tree[3])
    i += 1
i = 0
for vegetable in vegetables:
    vegetables[i] = Vegetable(vegetable[0], vegetable[1], vegetable[2], vegetable[3],vegetable[4])
    i += 1


print("=== Garden Plant Types ===\n")
roses[0].print()
roses[0].bloom()
print()
trees[0].print()
trees[0].produce_shade()
print()
vegetables[0].print()
print()
