data_to_check = set(input("Enter the data to be checked (with , ) : ").split(','))
print(data_to_check)

# sample_file = open('samples.txt' , 'r')
# x = set(line.strip() for line in sample_file.readlines())
# sample_file.close()

with open ('../samples.txt', 'r') as sample_file:
    x = set(line.strip() for line in sample_file.readlines())

y = x.intersection(data_to_check)
print(y)

with open('../common.txt', 'w') as common_values:
    for value in y:
        common_values.write(f'{value}\n')


#common_values = open('common.txt' , 'w')
#for value in y:
#    common_values.write(f'{value}\n')
#common_values.close()

