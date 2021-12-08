import sys

noOfIncrm = 0
tempList = []
sumsList = []
for i in range(3):
    tempList.append(int(sys.stdin.readline()))
sumsList.append(sum(tempList))

for reading in sys.stdin:
    if reading == '\n': break
    tempList.pop(0)
    tempList.append(int(reading))
    
    sumsList.append(sum(tempList))
    if sumsList[1] > sumsList[0]: noOfIncrm += 1
    sumsList.pop(0)

print(noOfIncrm)
