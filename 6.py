subj = {}
with open('shest.txt', 'r') as init_f:
    lines = init_f.readlines()
    for line in lines:
        data = line.replace('(', ' ').split()
        subj[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
print(subj)
