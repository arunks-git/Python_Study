class generator_example():
    def __init__(self):
        self.number = 0

    def __next__(self):  # dunder method for next function and makes this an itrator(which is used to get value)
        if self.number < 10:
            current = self.number
            self.number += 1
            return current

        else:
            raise StopIteration()

g1 = generator_example()
print(next(g1))
print(next(g1))