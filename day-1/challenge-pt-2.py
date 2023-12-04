file = open('./day-1/input.txt', 'r')

calibration = 0

digit_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def translateDigiName(line):
  for num, word in enumerate(digit_names):
    line = line.replace(word, f"{word}{num}{word}")
  return line

for line in file:
  digits = [char for char in translateDigiName(line) if char.isnumeric()]

  calibration += int(digits[0]+digits[-1])
  
print(calibration)
