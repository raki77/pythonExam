import threading
import time
import random

def function():
    a = []
    for i in range(1000):
        a.append(random.random())
        time.sleep(0.001)
    print(f"min: {min(a):.2f}, max: {max(a):.2f}")

start = time.time()
function()
function()
print("single end time : ", time.time() - start)

start = time.time()
th1 = threading.Thread(target=function)
th2 = threading.Thread(target=function)

th1.start()
th2.start()

th1.join()
th2.join()

print("thread end time : ", time.time() - start)
 