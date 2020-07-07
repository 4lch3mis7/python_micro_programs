from math import ceil

def progbar(total, current):
    t = 40
    c = current/total*t
    percent = current/total*100
    print('\r<' + '='*ceil(c) + ' '*ceil(t-c) + '>', str(ceil(percent))+'% ', end='') 


total = 500000
for current in range(total):
    progbar(total, current)

