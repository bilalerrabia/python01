class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def print(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self):
        self._height += 1

    def age(self):
        self._age += 1

    def get_info(self):
        return self._height, self._age


def simulate_week(plants):
    print("=== Day 1 ===")
    for plant in plants:
        plant.print()

    for _ in range(6):
        for plant in plants:
            plant.grow()
            plant.age()

    print("=== Day 7 ===")
    for plant in plants:
        plant.print()

    print("Growth this week:")
    for plant in plants:
        print(f"{plant._name}: +6cm")

plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]

simulate_week(plants)
