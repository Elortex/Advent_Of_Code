import sys

DIAGNOSTC_LEN = 12
oxGenRat = []
co2ScrubRat = []
tempReadingsList = []

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


oxGenDigitStack = 0
co2ScrubDigitStack = 0
for digitNo in range(1, len(oxGenRat[0]) - 1):
    
    for i in range(len(oxGenRat)):
        print(i, ' ', digitNo)
        if i == len(oxGenRat): break
        if oxGenRat[i][digitNo - 1] != mostCommon:
            oxGenRat.pop(i)
            continue
        else:
            if oxGenRat[i][digitNo] == '1': oxGenDigitStack += 1
            else: oxGenDigitStack -= 1
    if oxGenDigitStack > 0: mostCommon = '1'
    else: mostCommon = '0'

    for j in range(len(co2ScrubRat) - 1):
        if j == len(co2ScrubRat): break
        if co2ScrubRat[j][digitNo - 1] != leastCommon: 
            co2ScrubRat.pop(j)
            continue
        else:
            if co2ScrubRat[j][digitNo] == '1': co2ScrubDigitStack += 1
            else: co2ScrubDigitStack -= 1
    if co2ScrubDigitStack > 0: leastCommon = '0'
    else: leastCommon = '1'

#oxRatingConv = int(''.join(oxGenRat), 2)
#co2RatingConv = int(''.join(co2ScrubRat), 2)

#print(oxRatingConv*co2RatingConv)
print(oxGenRat, co2ScrubRat)