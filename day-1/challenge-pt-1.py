file = open('./day-1/input.txt', 'r')

calibration = 0

for line in file:
  lineNumber = ''.join(filter(str.isdigit, line))
  firstNumber = int(lineNumber[-1])
  lastNumber = int(lineNumber[len(lineNumber) - 1])
  calibration += int(str(firstNumber) + str(lastNumber))

print(calibration)
