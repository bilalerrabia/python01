class SecurePlant:
    def __init__(self, name: str):
        self.__name = name
        self.__age = 0
        self.__height = 0
        print(f"Plant created: {self.__name}")

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def print(self):
        print(f"Current plant: {self.__name} ({self.__height}cm,", end="")
        print(f"{self.__age} days)")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


print("=== Garden Security System ===")
plant = SecurePlant("Rose")
plant.set_height(25)
plant.set_age(30)
print()
plant.set_height(-5)
print()
plant.print()
