n, t = input().split(' ')

floors = list(int(num) for num in input().strip().split())[:int(n)]

numOfEmpl = int(input())
numOfRising = 0

if (int(t) < floors[numOfEmpl - 1] and floors[numOfEmpl - 1] != floors[-1]):
    numOfRising = 0 + floors[numOfEmpl - 1] - 1 + floors[-1] - 1
else:
    numOfRising = 0 + floors[-1] - 1

print(numOfRising)
