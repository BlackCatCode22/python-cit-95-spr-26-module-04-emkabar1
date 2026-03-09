fhand = open('mbox-short.txt')

for line in fhand:
    words = line.split()
    # guardian pattern in a compound logical expression
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
