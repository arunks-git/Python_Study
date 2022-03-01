# This is example of generator function usage
# testing again on git
def example():
    i = 0
    while i < 10:
        yield i   # yield returns current value and remembers it when the function is called again
        i +=1

x = example()
print(next(x)) #next calls the current value in generator function.
print(next(x))
print(next(x))