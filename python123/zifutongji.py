f = open("data.txt",encoding='utf-8')
cc = 0
d = {}
for i in range(26):
    d[chr(ord('a')+i)] = 0
for line in f:
    for c in line:
        d[c] = d.get(c, 0) + 1
        cc += 1
for i in range(26):
    print("{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]))
