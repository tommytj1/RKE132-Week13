class Animal:
    def __init__(self, pet_name):
        self.name = pet_name
        self.ears = 2
        self.legs = 4

    def sees(self, other):
        print(f"{self.name} sees {other.name}.")


class Cat(Animal):
    def __init__(self, cat_name):
        super().__init__(cat_name)
        self.hunger = 0

    def meow(self):
        print(f"{self.name}: Meow!")

    def sleep(self):
        print(f"{self.name} is sleeping.")

        self.hunger = self.hunger + 1

        if self.hunger >= 10:
            print(f"{self.name} wakes up hungry!")
            self.meow()

    def hisses(self):
        print(f"{self.name}: Hiss!")

    def scared_meow(self):
        print(f"{self.name}: Woof! SZSZHZ!")

    def cat_sees(self, other):
        super().sees(other)
        
        if isinstance(other, Dog):
            self.scared_meow()
        else:
            self.hisses()

class Dog(Animal):
    def __init__(self, dog_name):
        super().__init__(dog_name)
        
    def bark(self):
        print(f"{self.name}: Woof!")

    def wag_the_tail(self):
        print(f"{self.name} is wagging its tail.")

    def dog_sees(self, other):
        super().sees(other)

        if isinstance(other, Cat):
            self.bark()
        else:
            self.wag_the_tail()