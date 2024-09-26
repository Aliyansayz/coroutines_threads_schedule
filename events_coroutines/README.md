`asyncio` is a powerful library in Python that allows you to write concurrent code using the `async` and `await` syntax. It is often used for I/O-bound and high-level structured network code, where you want to handle multiple events or tasks in parallel without blocking the execution.

Here are several examples of event-driven programming using `asyncio`:

### 1. **Multiple Coroutines Running Concurrently**
This example demonstrates running multiple coroutines concurrently using `asyncio.gather()`. Each coroutine represents an event that will be triggered after a delay.

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

**Explanation**:
- `event_1`, `event_2`, and `event_3` are three asynchronous functions.
- Each event has a different delay, simulating asynchronous actions that complete at different times.
- `asyncio.gather()` allows running all these events concurrently. All the events start at the same time, but they complete as their respective delays elapse.

### 2. **Using an Event Loop with Timers**
This example demonstrates how to schedule tasks to run after a delay using `loop.call_later()`.

```python
import asyncio

def event_trigger(message):
    print(f"Event triggered: {message}")

async def main():
    loop = asyncio.get_event_loop()
    
    # Schedule the event triggers with delays
    loop.call_later(1, event_trigger, "Event 1 after 1 second")
    loop.call_later(2, event_trigger, "Event 2 after 2 seconds")
    loop.call_later(3, event_trigger, "Event 3 after 3 seconds")
    
    # Sleep to allow the events to trigger
    await asyncio.sleep(4)

asyncio.run(main())
```

**Explanation**:
- `loop.call_later()` schedules events to be triggered after a specified number of seconds.
- Each event will print a message after its delay.
- The main coroutine sleeps for 4 seconds to ensure all events can complete.

### 3. **Handling Asynchronous Events with `asyncio.Queue()`**
An `asyncio.Queue` is a useful way to handle events asynchronously. In this example, one coroutine puts events into the queue, and another coroutine consumes those events.

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

    # Start producer and consumer tasks
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    # Wait for the producer to finish
    await producer_task

    # Wait until all tasks are done
    await queue.join()

    # Cancel the consumer task since it's in an infinite loop
    consumer_task.cancel()

asyncio.run(main())
```

**Explanation**:
- The `producer()` coroutine produces events and puts them into the queue.
- The `consumer()` coroutine consumes events from the queue and processes them.
- `queue.task_done()` indicates that a task from the queue has been processed.
- The consumer is in an infinite loop, so after the producer finishes, we cancel the consumer.

### 4. **Using `asyncio.Event` to Trigger an Event**
`asyncio.Event()` is a synchronization primitive that can be used to trigger an event from one coroutine that other coroutines wait on.

```python
import asyncio

async def waiter(event):
    print("Waiting for event to be triggered...")
    await event.wait()  # Wait until event is set
    print("Event has been triggered!")

async def setter(event):
    await asyncio.sleep(2)  # Simulate a delay
    print("Triggering the event...")
    event.set()  # Trigger the event

async def main():
    event = asyncio.Event()

    # Start waiter and setter tasks
    waiter_task = asyncio.create_task(waiter(event))
    setter_task = asyncio.create_task(setter(event))

    # Wait for both tasks to complete
    await asyncio.gather(waiter_task, setter_task)

asyncio.run(main())
```

**Explanation**:
- `event.wait()` causes the `waiter()` coroutine to pause until `event.set()` is called.
- `setter()` triggers the event after a 2-second delay.
- This is useful in situations where one part of the program must wait for another part to signal completion or readiness.

### 5. **Timeout Handling with `asyncio.wait_for()`**
You can use `asyncio.wait_for()` to limit the time a coroutine can wait for an event.

```python
import asyncio

async def long_running_task():
    await asyncio.sleep(5)
    return "Task complete!"

async def main():
    try:
        result = await asyncio.wait_for(long_running_task(), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("The task took too long!")

asyncio.run(main())
```

**Explanation**:
- The `long_running_task()` coroutine takes 5 seconds to complete.
- `asyncio.wait_for()` imposes a 3-second timeout. If the task does not complete within this time, a `TimeoutError` is raised.

### 6. **Simulating Event Streams with `async for`**
This example demonstrates how you can simulate an event stream and process events as they occur using an asynchronous generator.

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

**Explanation**:
- `event_stream()` is an asynchronous generator that yields events.
- `async for` is used to consume these events one by one as they are produced.

---

These examples show how `asyncio` enables event-driven, concurrent programming in Python. 
Whether you're handling I/O-bound tasks, scheduling time-based events, or responding to asynchronous triggers, `asyncio` provides powerful tools for working with such patterns.
