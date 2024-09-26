## Race Conditions

```python
import threading

count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def thread_task():
    for _ in range(1000):
        increment()
        decrement()

if __name__ == "__main__":
    threads = []
    for _ in range(10):
        t = threading.Thread(target=thread_task)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(count)  # This will likely not be 0 due to race conditions
```

This code demonstrates a race condition where multiple threads are incrementing and decrementing a shared counter. The result is unpredictable due to the non-deterministic nature of thread execution.

## Deadlocks

```python
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def func1():
    lock1.acquire()
    print("Thread 1 acquired lock1")
    lock2.acquire()
    print("Thread 1 acquired lock2")
    lock2.release()
    lock1.release()

def func2():
    lock2.acquire()
    print("Thread 2 acquired lock2")
    lock1.acquire()
    print("Thread 2 acquired lock1")
    lock1.release()
    lock2.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
```

This code demonstrates a potential deadlock where two threads acquire locks in different orders, leading to a circular wait condition.

## Thread Pools

```python
import concurrent.futures
import time

def task(n):
    time.sleep(2)
    return n * n

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(task, range(10))

    for result in results:
        print(result)
```

This code creates a thread pool with 5 workers and submits tasks to it. The `map` function ensures that the results are returned in the same order as the input.
