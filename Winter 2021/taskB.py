numOfPeople = int(input())
numOfCuts = 0

if numOfPeople % 2 == 0:
    numOfCuts = numOfPeople / 2
else:
    numOfCuts = numOfPeople / 2 + 1

for i in range(64):
    if (numOfPeople == 2 ** i):
        numOfCuts = i
        break

print(int(numOfCuts))
