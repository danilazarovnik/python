cfcd
l = input('набери текст: ')
while l:
    my_file.writelines(l + '\n')
    l = input('набери текст: ')
    if not l:
        break

my_file = open('test.txt', 'r')
rezult = my_file.readlines()
print(rezult)
my_file.close()
