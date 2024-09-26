## Event

An Event allows one or more threads to wait for an event to be set before they proceed.


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
