import time
"""
print("Counting down:")
for i in range(10, 0, -1):
    print(i, end='\r')
    time.sleep(0.5)
print("Blast off!")
"""

dummyInput = input('t\r')
time.sleep(0.5)
dummyInput = input('te\r')
time.sleep(0.5)
dummyInput = input('tes', end='\r')
time.sleep(0.5)
dummyInput = input('test', end='\r')
time.sleep(0.5)
dummyInput = input('test1')