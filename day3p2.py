import sys

oxGenRat = []
co2ScrubRat = []

digitStack = 0
for diagnReading in sys.stdin:
    if diagnReading == '\n': break
    if diagnReading[0] == '0': digitStack -= 1
    elif diagnReading[0] == '1': digitStack += 1

    oxGenRat.append(diagnReading)
co2ScrubRat = oxGenRat.copy()

if digitStack < 0: 
    mostCommon = '0'
    leastCommon = '1'
else: 
    mostCommon = '1'
    leastCommon = '0'


for digitNo in range(1, len(oxGenRat[0]) - 1):
    oxGenDigitStack = 0
    co2ScrubDigitStack = 0

    for i in range(len(oxGenRat)):
        
        while i < len(oxGenRat) and oxGenRat[i][digitNo - 1] != mostCommon:
            if len(oxGenRat) == 1: break
            oxGenRat.pop(i)

        if i >= len(oxGenRat): break
        if oxGenRat[i][digitNo] == '1': oxGenDigitStack += 1
        else: oxGenDigitStack -= 1
    if oxGenDigitStack < 0: mostCommon = '0'
    else: mostCommon = '1'

    for j in range(len(co2ScrubRat)):
        
        while j < len(co2ScrubRat) and co2ScrubRat[j][digitNo - 1] != leastCommon:
            if len(co2ScrubRat) == 1: break
            co2ScrubRat.pop(j)
            
        if j >= len(co2ScrubRat): break
        if co2ScrubRat[j][digitNo] == '1': co2ScrubDigitStack += 1
        else: co2ScrubDigitStack -= 1
    if co2ScrubDigitStack < 0: leastCommon = '1'
    else: leastCommon = '0'


if oxGenRat[0][-2] == '1': oxGenRes = oxGenRat[0]
else: oxGenRes = oxGenRat[1]

if co2ScrubRat[0][-2] == '0': co2ScrubRes = co2ScrubRat[0]
else: co2ScrubRes = co2ScrubRat[1]

oxGenRes = int(''.join(oxGenRes), 2)
co2ScrubRes = int(''.join(co2ScrubRes), 2)

print(oxGenRes*co2ScrubRes)