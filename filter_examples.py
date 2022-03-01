
# exaple of filter function . Filter is a generator


def start_with_r(x):
    return x.startswith('A')

friends = [ 'Arun' , 'Aaron' , 'Binoj' , 'Riju']

y = filter(start_with_r , friends)  # filter needs two aruments , 1. a function that retuns true/false , 2. Iterable ( here a list)

print(next(y))
print(next(y))