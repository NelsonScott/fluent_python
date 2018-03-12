from array import array
# some arrays
size = 10000
floats = array('d', (random() for i in range(size)))

with open('floats.txt', 'w') as f:
    floats.tofile(f)

floats2 = array('d')

with open('floats.txt', 'r') as f:
    floats2.fromfile(f, size)

print floats2 == floats
