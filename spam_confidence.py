fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

count = 0
total = 0

for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'): continue

    pos = line.find(':')
    value = float(line[pos + 1:])

    total += value
    count += 1

if count > 0:
    avg = total / count
    print('Average spam confidence:', avg)
