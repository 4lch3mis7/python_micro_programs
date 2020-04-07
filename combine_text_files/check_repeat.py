filename = 'stripped.txt'

file = open(filename, 'rb')
wordlist = file.readlines()
repeated = []
count = 0

for i, word in enumerate(wordlist):
    c = wordlist.count(word)
    if c > 1:
        repeated.append(word)
        print(c, word)
    else:
        print(f'[+] {i} \twords scanned, no repetition found.')

print("Words repeated =", repeated)


