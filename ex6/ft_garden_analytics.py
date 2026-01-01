class Plant:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def grow(self):
        self._height += 1
        print(f"{self._name} grew 1cm")

    def __str__(self):
        return f"- {self._name}: {self._height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self._color = color
        self._blooming = True

    def __str__(self):
        return (
            f"- {self._name}: {self._height}cm, {self._color}"
            f"flowers (blooming)"
            )


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self._points = points

    def __str__(self):
        return (
            f"- {self._name}: {self._height}cm, {self._color} "
            f"flowers (blooming), Prize points: {self._points}"
        )


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant._name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self, stats_helper):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant)

        regular, flowering, prize = stats_helper.count_types(self.plants)
        print()
        print(f"Plants added: {len(self.plants)},", end="")
        print(f"Total growth: {len(self.plants)}cm")
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )


class GardenManager:
    gardens = []

    class GardenStats:
        def count_types(plants):
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize
        count_types = staticmethod(count_types)

    def add_garden(self, garden):
        self.gardens.append(garden)

    def total_gardens(cls):
        return len(cls.gardens)
    total_gardens = classmethod(total_gardens)

    def create_garden_network(cls):
        scores = {}
        for garden in cls.gardens:
            score = 0
            for plant in garden.plants:
                score += plant._height
                if isinstance(plant, PrizeFlower):
                    score += plant._points
            scores[garden.owner] = score
        return scores
    create_garden_network = classmethod(create_garden_network)

    def validate_height(height):
        return height >= 0
    validate_height = staticmethod(validate_height)


print("=== Garden Management System Demo ===")
print()
manager = GardenManager()
alice = Garden("Alice")
bob = Garden("Bob")

manager.add_garden(alice)
manager.add_garden(bob)

alice.add_plant(Plant("Oak Tree", 100))
alice.add_plant(FloweringPlant("Rose", 25, "red"))
alice.add_plant(PrizeFlower("Sunflower", 80, "yellow", 10))
print()
bob.add_plant(Plant("tomato", 91))

bob.grow_all()
alice.grow_all()
print()
alice.report(GardenManager.GardenStats)
print()
print("Height validation test:", GardenManager.validate_height(10))

scores = GardenManager.create_garden_network()
print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")

print("Total gardens managed:", GardenManager.total_gardens())
