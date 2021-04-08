range_ = [int(i) for i in input('Введи последовательность чисел через пробел: \n').split()]
z = (int(input('Введи еще одно число: \n')))
range_.append(z)
for i in range(len(range_)):
    for j in range(len(range_) - i - 1):
        if range_[j] > range_[j + 1]:
            range_[j], range_[j + 1] = range_[j + 1], range_[j]


def binary_search(range_, z, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if range_[middle] == z:
        return middle
    elif z < range_[middle]:
        return binary_search(range_, z, left, middle - 1)
    else:
        return binary_search(range_, z, middle + 1, right)


i_z = (binary_search(range_, z, 0, len(range_)))

if i_z == 0:
    print('Слева нет числа')
elif i_z == len(range_):
    print('Справа нет числа')
else:
    print(i_z - 1, i_z + 1)
