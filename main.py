from animal import Animal, Cat, Dog

my_cat = Cat("Spark")
my_dog = Dog("Minnie")

neighbors_dog = Dog("Blacky")
neighbors_cat = Cat("Rudy")

my_dog.dog_sees(neighbors_dog)
my_cat.cat_sees(neighbors_dog)