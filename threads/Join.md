# join():

The join() method ensures that the main thread waits for the child thread to complete before proceeding.

```python
import threading
import time

def long_task():
    time.sleep(3)
    print("Task finished")

thread = threading.Thread(target=long_task)
thread.start()

print("Waiting for the thread to finish...")
thread.join()
print("Thread has finished. Proceeding.")

```
