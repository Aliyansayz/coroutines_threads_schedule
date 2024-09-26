Thread Synchronization

Thread synchronization is often needed to prevent race conditions when multiple threads try to access and modify shared data.


```python
import threading

shared_data = 0
lock = threading.Lock()

def increment():
    global shared_data
    for _ in range(100000):
        lock.acquire()
        shared_data += 1
        lock.release()

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final shared data:", shared_data)


```
