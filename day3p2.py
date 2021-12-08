import sys

DIAGNOSTC_LEN = 12
gammaRate = []
epsilonRate = []
digitCollector = [0] * DIAGNOSTC_LEN 

for diagnReading in sys.stdin:
    if diagnReading == '\n': break

    for i in range(DIAGNOSTC_LEN):
        if diagnReading[i] == '1': digitCollector[i] += 1
        elif diagnReading[i] == '0': digitCollector[i] -= 1

for i in range(DIAGNOSTC_LEN):
    if digitCollector[i] > 0: 
        gammaRate.append('1')
        epsilonRate.append('0')

    elif digitCollector[i] < 0:
        gammaRate.append('0')
        epsilonRate.append('1')

gammaRateConv = int(''.join(gammaRate), 2)
epsilonRateConv = int(''.join(epsilonRate), 2)

print(gammaRateConv*epsilonRateConv)