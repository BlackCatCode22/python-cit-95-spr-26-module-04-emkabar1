fhand = open('romeo.txt')

unique_words = []

for line in fhand:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

unique_words.sort()
print(unique_words)
