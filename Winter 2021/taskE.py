n = int(input())
lunch = 0
listLunch = []
minSum = 0 # переменная для суммы обедов > 100
coupons = 0 # переменная для вырезания обедов из списка на которые можно потратить купон

for i in range(n):
    lunch = int(input())
    if (lunch <= 100):
        listLunch.append(lunch)
    if lunch > 100:
        coupons += 1
        minSum += lunch

listLunch.sort(reverse=True)

print(sum(listLunch[coupons:], minSum))