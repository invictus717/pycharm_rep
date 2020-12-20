f=open("sensor-data-1k.txt", "r")
avg,cnt = 0,0
for line in f:
  ls = line.split()
  cnt+=1
  avg+=eval(ls[4])
print("{:.2f}".format(avg/cnt))