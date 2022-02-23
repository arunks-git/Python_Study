class generator_itertor():
    def __init__(self):
        self.number = 0

    def __next__(self):  # dunder method for next function and makes this an itrator(which is used to get value)
        if self.number < 10:
            current = self.number
            self.number += 1
            return current

        else:
            raise StopIteration()

class generator_iterable():  # dunder method which makes it iterable (which is used to go over all the values)
    def __iter__(self):
        return generator_itertor()

class iterable_example1():  # another way to which makes it iterable (which is used to go over all the values)
    def __init__(self):
        self.x = [ '1' , '2']
    def __len__(self):             # dunder method for next function
        return len(self.x)
    def __getitem__(self , i):      # dunder method for next function
        return self.x[i]


g1 = generator_itertor()
print(next(g1))
print(next(g1))  #  calling next value and acting as interator
g2 = generator_iterable()
print(sum(g2)) # going through all the value and adding up.

for y in iterable_example1():
    print(y)

number = [ x for x in [ 1 , 2 , 3 , 4 ,5 ]]   #  list Comprehension
number_gen = (x for x in [ 1 , 2 , 3 , 4 ,5 ])   #  generator Comprehension

print(number)
print(next(number_gen))