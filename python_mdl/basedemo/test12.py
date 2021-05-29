import time;

tick = time.time()
print(tick)

starttime = time.clock()

print('----',starttime)

localtime = time.localtime(time.time())

print(localtime)
print(time.localtime())

time2 = time.asctime(localtime)

print(time2)

time3 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print(time.localtime())

print(time3)

endtime = time.clock()

print('----',endtime)

print(endtime-starttime)

