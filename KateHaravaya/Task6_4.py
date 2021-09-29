'''Task6_4. Create hierarchy out of birds.
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.'''

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f'{self.name} bird can fly'

    def walk(self):
        return f'{self.name} bird can walk'

    def __str__(self):
        return f'{self.name} can fly and walk'


class FlyingBird(Bird):
    def __init__(self, name, ration = 'beetles'):
        self.name = name
        self.ration = ration

    def eat(self):
        return f'{self.name} eats mostly {self.ration}'

class NonFlyingBird(Bird):
    def __init__(self, name, ration = 'seaweed'):
        self.name = name
        self.ration = ration

    def swim(self):
        return f'{self.name} bird can swim'

    def eat(self):
        return f'{self.name} eats mostly {self.ration}'

    def __str__(self):
        return f'{self.name} can walk and swim'

    def fly(self):
        raise AttributeError(f'AttributeError: {self.name} object has no attribute "fly"')

class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration = 'fish and beetles'):
        super().__init__(name, ration)

    def __str__(self):
        return f'{self.name} can walk, swim and fly'

    def eat(self):
        return f'{self.name} eats {self.ration}'

first_ancestor = Bird('Any')
print(str(first_ancestor))
print(first_ancestor.walk())
print(first_ancestor.fly())

fly_bird = FlyingBird("Canary")
print(str(fly_bird))
print(fly_bird.fly())
print(fly_bird.walk())
print(fly_bird.eat())

try:
    non_fly_bird = NonFlyingBird("Penguin", "small fish")
    print(str(non_fly_bird))
    print(non_fly_bird.walk())
    print(non_fly_bird.swim())
    print(non_fly_bird.eat())
    print(non_fly_bird.fly())
except AttributeError as e:
    print(e)

try:

    super_b = SuperBird("Joy")
    print(str(super_b))
    print(super_b.eat())
    print(super_b.walk())
    print(super_b.swim())
    print(super_b.fly())
except AttributeError as e:
    print(e)
print(SuperBird.__mro__)




