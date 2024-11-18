from abc import ABC, abstractmethod

# Base Class (Abstraction)
class Fruit(ABC):
    def __init__(self, name, color, taste):
        self.__name = name  # Encapsulated attribute
        self.__color = color
        self.__taste = taste

    def get_details(self):  # Encapsulated Method
        return f"{self.__name} is {self.__color} and tastes {self.__taste}."

    def set_details(self, name, color, taste):
        self.__name = name
        self.__color = color
        self.__taste = taste

    @abstractmethod
    def special_feature(self):
        pass


# Derived Class (Inheritance and Polymorphism)
class Apple(Fruit):
    def __init__(self, variety, color, taste):
        super().__init__("Apple", color, taste)
        self.variety = variety

    def special_feature(self):  # Polymorphism
        return f"{self.variety} apples are great for making pies."

    def get_details(self):  # Overriding method
        return f"An apple is {self._Fruit__color}, tastes {self._Fruit__taste}, and is a {self.variety} variety."


class Mango(Fruit):
    def __init__(self, region, color, taste):
        super().__init__("Mango", color, taste)
        self.region = region

    def special_feature(self):  # Polymorphism
        return f"Mangoes from {self.region} are known for their sweetness."

    def get_details(self):  # Overriding method
        return f"A mango is {self._Fruit__color}, tastes {self._Fruit__taste}, and is from the {self.region} region."


# Main Program
if __name__ == "__main__":
    apple = Apple("Fuji", "Red", "Sweet")
    mango = Mango("Alphonso", "Yellow", "Sweet")

    # Encapsulation Example
    print(apple.get_details())
    print(apple.special_feature())
    print(mango.get_details())
    print(mango.special_feature())

    # Polymorphism Example
    fruits = [apple, mango]
    for fruit in fruits:
        print(fruit.get_details())
