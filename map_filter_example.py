li = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8  ]

def fun(x):
    return x**2

def Is_odd(x):
    return x%2 != 0

print(list(map(fun,li)))  # method 1 - using map . Map need variable as a function and iterable

print([fun(x) for x in li])  # method 2 - list

y = list(map(lambda x: x**2 , li))  # method 3 #  using map and lambda function
print(y)

z = list(filter(Is_odd, li))  ## filter function example filter variable 1 is a function that check if odd. It check true or false and add from the iterble ( which is 2nd variable)
print("Odd numbers are : " , z)

a = list(map(fun ,filter(Is_odd, li)))  ## print x**2 if number is odd
print(a)