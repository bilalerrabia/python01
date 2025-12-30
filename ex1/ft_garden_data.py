
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def print(self):
        print(f"{self._name}: {self._height}cm, {self._age} days old")


print("=== Garden Plant Registry ===")
plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)

plant1.print()
plant2.print()
plant3.print()
