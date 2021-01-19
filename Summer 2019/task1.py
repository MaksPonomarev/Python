"Найти минимальное расстоение между двумя точками на расстоянии 100 метров"

amountMovement = int(input())
minDistance = 100
actualDistance = 0

for i in range(0, amountMovement - 1):
    actualDistance = minDistance + int(input()) + int(input())
    if (actualDistance < minDistance):
        minDistance = actualDistance

print(minDistance)