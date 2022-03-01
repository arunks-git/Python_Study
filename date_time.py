from datetime import datetime , timezone
print(datetime.now(timezone.utc))
x = datetime.now()

print(x.strftime('%d-%m-%Y %H:%M:%S'))

y = input('Enter date in dd-mm format :')
y = datetime.strptime(y , '%d-%m-%Y')

print(y)