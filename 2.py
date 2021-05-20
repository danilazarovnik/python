my_file = open('dva.txt', 'r')
content = my_file.readlines()
print('Количество строк в файле - ', len(content))

my_file = open('dva.txt', 'r')
l = 0
for line in my_file:
    l += 1
    print('Количество слов в строке', l, ': ', len(line.split()))
