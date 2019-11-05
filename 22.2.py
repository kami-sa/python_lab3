def partial_sums(*args):
    array = []
    sum = 0
    array.append(0)
    array.append(args[0])
    for i in range(2, len(args)):
        # array.append(args[i-2] + args[i-1])
        for j in range(i+1):
            sum += args[j]
        array.append(sum)
        sum = 0

    return array;


# print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))