import sys
noOfIncrm = 0
prevReading = int(sys.stdin.readline())
for reading in sys.stdin:
    if reading == '\n': break
    currReading = int(reading)
    if currReading > prevReading: noOfIncrm += 1
    prevReading = currReading
print(noOfIncrm)
