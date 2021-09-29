'''Task6_1. Implement a Counter class which optionally accepts the start value and the counter stop value. If the start value is not specified the counter should begin with 0. If the stop value is not specified it should be counting up infinitely. If the counter reaches the stop value, print "Maximal value is reached."
Implement to methods: "increment" and "get"
If you are familiar with Exception rising use it to display the "Maximal value is reached." message. '''

class Counter:
    def __init__(self, start = 0, stop = float("inf")):
        self.stop = stop
        self.counter = start

    def increment(self):
        if self.counter == self.stop:
            print("Maximal value is reached.")
        else:
            self.counter += 1

    def get(self):
        return self.counter

a = Counter(start=1, stop=10)
a.increment()
a.increment()
print(a.get())
a.increment()
print(a.get())