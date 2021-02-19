per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a=list(per_cent.values())
list(map(float,a))
money=int(input("Введи сумму вклада:"))
for i in range(len(a)):
    a[i]*=money/100
b=['%.2f'% elem for elem in a]
c=list(per_cent.keys())
for i in range(len(c)):
    c[i]+=b[i]
print("Заработаете за год:", c)
print("Максимальная сумма, которую вы можете заработать:", max(b))