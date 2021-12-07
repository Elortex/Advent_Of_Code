import sys
posX = 0
posY = 0
for command in sys.stdin:
    if command == '\n': break
    tempCommand = command.split()
    if tempCommand[0] == 'down': posY += int(tempCommand[1])
    elif tempCommand[0] == 'up': posY -= int(tempCommand[1])
    else: posX += int(tempCommand[1])

print(posX)
print(posY)
print(posY*posX)