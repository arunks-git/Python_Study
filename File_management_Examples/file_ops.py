
def file_read():
    with open("../testing.txt", 'r') as filename:
        print(filename.read())


def file_write():
    x = input ("Enter data to write : ")
    with open("../testing.txt", 'w') as filename:
        filename.write(x)