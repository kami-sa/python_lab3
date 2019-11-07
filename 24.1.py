matrix = []
num_list = []
while True:
    num = input()
    if num != '':
        matrix.append(num)
    else:
        break
for i in range(len(matrix)):
    for j in matrix[i].split():
        num_list.append(int(j))
print (not all(num_list))
