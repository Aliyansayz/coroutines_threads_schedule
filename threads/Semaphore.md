## Semaphore

A Semaphore limits the number of threads that can access a resource at the same time.

```python
import threading
import time

sem = threading.Semaphore(3)

def task():
    sem.acquire()
    print(f"{threading.current_thread().name} acquired semaphore")
    time.sleep(2)
    print(f"{threading.current_thread().name} releasing semaphore")
    sem.release()

threads = []
for i in range(6):
    thread = threading.Thread(target=task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

