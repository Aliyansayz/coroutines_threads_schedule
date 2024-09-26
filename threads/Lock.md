## Lock
A Lock ensures that only one thread accesses a shared resource at a time.

```python
import threading

lock = threading.Lock()

def print_numbers():
    with lock:
        for i in range(5):
            print(f"{threading.current_thread().name} -> {i}")

thread1 = threading.Thread(target=print_numbers, name="Thread 1")
thread2 = threading.Thread(target=print_numbers, name="Thread 2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()


```
