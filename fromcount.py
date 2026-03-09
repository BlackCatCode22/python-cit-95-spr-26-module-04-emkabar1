fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    print(words[1])
    count += 1

print('There were', count, 'lines in the file with From as the first word')
