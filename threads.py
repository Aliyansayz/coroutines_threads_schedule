"""
## Glossary of Threading Terms

### Basic Terms
* **Multithreading:** The concurrent execution of multiple parts of a program within a single process.
* **Thread:** The smallest unit of processing that can be scheduled for execution.
* **threading module:** A Python module providing tools for creating and managing threads.

### Intermediate Terms
* **Global Interpreter Lock (GIL):** A mechanism in Python that prevents multiple threads from executing Python bytecode at the same time.
* **Thread synchronization:** Coordinating the actions of multiple threads to prevent race conditions and ensure data consistency.
* **Lock:** A synchronization primitive that allows only one thread to access a shared resource at a time.
* **Semaphore:** A synchronization primitive that controls access to a shared resource by limiting the number of simultaneous users.
* **Event:** A synchronization mechanism that allows one or more threads to wait for a specific condition to occur.
* **join():** A method used to wait for a thread to finish execution before proceeding.
* **I/O bound:** A task that spends most of its time waiting for input or output operations to complete.

**Would you like to delve deeper into specific concepts or explore more advanced topics like race conditions, deadlocks, or thread pools?**


"""


Below are Python code examples demonstrating each of the threading phenomena you requested:

### 1. **Thread Synchronization:**
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

### 2. **Lock:**
A `Lock` ensures that only one thread accesses a shared resource at a time.

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

### 3. **Semaphore:**
A `Semaphore` limits the number of threads that can access a resource at the same time.

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

### 4. **Event:**
An `Event` allows one or more threads to wait for an event to be set before they proceed.

```python
import threading
import time

event = threading.Event()

def waiter():
    print("Waiting for the event to be set...")
    event.wait()
    print("Event is set! Proceeding...")

def setter():
    time.sleep(2)
    print("Setting the event")
    event.set()

thread1 = threading.Thread(target=waiter)
thread2 = threading.Thread(target=setter)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

### 5. **`join()`:**
The `join()` method ensures that the main thread waits for the child thread to complete before proceeding.

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

### 6. **I/O Bound:**
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
