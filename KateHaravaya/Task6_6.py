'''Task6_6. A singleton is a class that allows only a single instance of itself
 to be created and gives access to that created instance.
Implement singleton logic inside your custom class using a method to initialize class instance.'''

class Sun:
    inst_val = None
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @staticmethod
    def inst():
        if Sun.inst_val is None:
            Sun.inst_val = Sun("Sun", 696340)

        return Sun.inst_val


t = Sun.inst()
s = Sun.inst()
print(s is t)
