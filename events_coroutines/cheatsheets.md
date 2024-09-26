### Python `asyncio` Cheatsheet

`asyncio` is a Python library for writing concurrent code using the `async` and `await` syntax. It's useful for I/O-bound tasks where you want to handle multiple events or tasks in parallel without blocking.

---

https://chatgpt.com/share/66f548c6-4688-8010-80d3-d341891f57d2

### 1. **Multiple Coroutines Running Concurrently**

Run multiple coroutines simultaneously using `asyncio.gather()`.

```python
import asyncio

async def event_1():
    await asyncio.sleep(1)
    print("Event 1 occurred")

async def event_2():
    await asyncio.sleep(2)
    print("Event 2 occurred")

async def event_3():
    await asyncio.sleep(3)
    print("Event 3 occurred")

async def main():
    await asyncio.gather(event_1(), event_2(), event_3())

asyncio.run(main())
```

- **`asyncio.gather()`** runs tasks concurrently.
- Each coroutine (`event_1`, `event_2`, `event_3`) waits a different amount of time before completing.

---

### 2. **Using an Event Loop with Timers**

Use `loop.call_later()` to schedule tasks with delays.

```python
import asyncio

def event_trigger(message):
    print(f"Event triggered: {message}")

async def main():
    loop = asyncio.get_event_loop()
    
    # Schedule event triggers with delays
    loop.call_later(1, event_trigger, "Event 1 after 1 second")
    loop.call_later(2, event_trigger, "Event 2 after 2 seconds")
    loop.call_later(3, event_trigger, "Event 3 after 3 seconds")
    
    await asyncio.sleep(4)

asyncio.run(main())
```

- **`loop.call_later()`** schedules a function to be called after a delay.
- Use `await asyncio.sleep()` to allow the events to execute.

---

### 3. **Handling Events with `asyncio.Queue()`**

A queue allows multiple tasks to share and process data asynchronously.

```python
import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        event = f"Event {i+1}"
        await queue.put(event)
        print(f"Produced: {event}")

async def consumer(queue):
    while True:
        event = await queue.get()
        print(f"Consumed: {event}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await queue.join()
    consumer_task.cancel()

asyncio.run(main())
```

- **`asyncio.Queue()`** is useful for coordinating producer-consumer workflows.
- `queue.task_done()` signals task completion.

---

### 4. **Using `asyncio.Event` to Trigger Events**

`asyncio.Event()` synchronizes coroutines by allowing one coroutine to trigger an event that other coroutines wait on.

```python
import asyncio

async def waiter(event):
    print("Waiting for event...")
    await event.wait()
    print("Event triggered!")

async def setter(event):
    await asyncio.sleep(2)
    print("Triggering the event...")
    event.set()

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())
```

- **`event.wait()`** pauses execution until **`event.set()`** is called in another coroutine.
- Useful for synchronizing operations between tasks.

---

### 5. **Timeout Handling with `asyncio.wait_for()`**

Control how long a coroutine can wait for an event.

```python
import asyncio

async def long_task():
    await asyncio.sleep(5)
    return "Task complete!"

async def main():
    try:
        result = await asyncio.wait_for(long_task(), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("Task took too long!")

asyncio.run(main())
```

- **`asyncio.wait_for()`** adds a timeout to the execution of a coroutine.
- A `TimeoutError` is raised if the task exceeds the specified time.

---

### 6. **Simulating Event Streams with `async for`**

Create an asynchronous event stream using an async generator and handle events as they occur.

```python
import asyncio

async def event_stream():
    for i in range(5):
        await asyncio.sleep(1)
        yield f"Event {i+1}"

async def event_handler():
    async for event in event_stream():
        print(f"Handling {event}")

asyncio.run(event_handler())
```

- **`async for`** allows you to consume events from an asynchronous generator.
- Use **`yield`** within asynchronous generators to provide values as they are generated.

---

### Key Concepts in `asyncio`:

1. **`async def`**: Defines an asynchronous function (coroutine).
2. **`await`**: Pauses the coroutine until the awaited task completes.
3. **`asyncio.run()`**: Runs an event loop for the provided coroutine.
4. **`asyncio.gather()`**: Runs multiple coroutines concurrently.
5. **`asyncio.Queue()`**: A thread-safe queue used for asynchronous task communication.
6. **`asyncio.Event()`**: A synchronization primitive used to manage and wait for events between coroutines.
7. **`asyncio.sleep()`**: Pauses execution of a coroutine for a specified number of seconds.
8. **`async for`**: Used to iterate over asynchronous generators.

---

With `asyncio`, you can build highly efficient event-driven and concurrent programs, especially useful for I/O-bound operations like network requests or database interactions.
