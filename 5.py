with open('pyat.txt', 'w+') as file_obj:
    line = input('набери цифры через пробел: ')
    file_obj.writelines(line)
    n = line.split()
print(sum(map(int, n)))
