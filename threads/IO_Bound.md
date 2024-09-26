### **I/O Bound:**
I/O-bound tasks, such as reading and writing to files or making network requests, often involve waiting for input/output operations.

```python
import threading
import time

def io_bound_task():
    print(f"{threading.current_thread().name} starting I/O-bound task")
    time.sleep(2)  # Simulating I/O delay
    print(f"{threading.current_thread().name} finished I/O-bound task")

threads = []
for i in range(5):
    thread = threading.Thread(target=io_bound_task)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

In this I/O-bound example, each thread simulates a time delay representing an I/O operation. 

These code snippets should provide a good foundation for understanding threading phenomena in Python.
