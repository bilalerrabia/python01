class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def print(self):
        print(f"Created: {self._name} ({self._height}cm, {self._age} days)")


def ft_plant_factory(plants):
    result = []
    for plant in plants:
        result.append(Plant(plant[0], plant[1], plant[2]))
    return result

plants = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
]
result = ft_plant_factory(plants)
print("=== Plant Factory Output ===")
for plant in result:
    plant.print()
print(f"\nTotal plants created: {len(result)}")
