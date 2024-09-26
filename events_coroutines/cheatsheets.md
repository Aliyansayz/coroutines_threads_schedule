### Python `asyncio` Cheatsheet

`asyncio` is a Python library for writing concurrent code using the `async` and `await` syntax. It's useful for I/O-bound tasks where you want to handle multiple events or tasks in parallel without blocking.

---

https://chatgpt.com/share/66f548c6-4688-8010-80d3-d341891f57d2

### Python `asyncio` Basic Functions Cheatsheet

`asyncio` provides tools for writing asynchronous, concurrent code. Here are the core functions you'll frequently use in `asyncio`:

---

### 1. **`asyncio.run(coro)`**
Runs the given coroutine and automatically manages the event loop for you.

- **Usage**:
    ```python
    import asyncio

    async def main():
        print("Hello, World!")

    asyncio.run(main())
    ```

- **Explanation**: Runs the `main()` coroutine and closes the event loop once complete.

---

### 2. **`async def`**
Defines a coroutine function. This function must be awaited or scheduled to run within an event loop.

- **Usage**:
    ```python
    async def fetch_data():
        return "Data fetched"

    # Call with 'await'
    data = await fetch_data()
    ```

- **Explanation**: A coroutine function is similar to a regular function but designed to work asynchronously.

---

### 3. **`await`**
Pauses the execution of a coroutine until the awaited task completes.

- **Usage**:
    ```python
    async def task():
        await asyncio.sleep(1)
        print("Task complete!")
    ```

- **Explanation**: Allows a coroutine to wait for another coroutine or asynchronous operation to complete without blocking the entire program.

---

### 4. **`asyncio.sleep(seconds)`**
Pauses the coroutine for the specified number of seconds.

- **Usage**:
    ```python
    import asyncio

    async def delayed_hello():
        print("Waiting...")
        await asyncio.sleep(3)
        print("Hello after 3 seconds")

    asyncio.run(delayed_hello())
    ```

- **Explanation**: Used to simulate delays or pauses in the execution of a coroutine.

---

### 5. **`asyncio.gather(*coros)`**
Runs multiple coroutines concurrently and returns the results once all have completed.

- **Usage**:
    ```python
    async def task_1():
        await asyncio.sleep(1)
        return "Task 1 done"

    async def task_2():
        await asyncio.sleep(2)
        return "Task 2 done"

    async def main():
        results = await asyncio.gather(task_1(), task_2())
        print(results)

    asyncio.run(main())
    ```

- **Explanation**: Executes multiple coroutines at once and waits for them all to finish. It’s great for running independent tasks concurrently.

---

### 6. **`asyncio.create_task(coro)`**
Schedules the execution of a coroutine and returns a task object. The coroutine runs concurrently with other tasks.

- **Usage**:
    ```python
    async def task():
        await asyncio.sleep(1)
        print("Task finished")

    async def main():
        task1 = asyncio.create_task(task())
        task2 = asyncio.create_task(task())
        await task1
        await task2

    asyncio.run(main())
    ```

- **Explanation**: `create_task()` allows you to run coroutines in the background while doing other work.

---

### 7. **`asyncio.Queue()`**
Creates a queue for handling asynchronous producer-consumer scenarios.

- **Usage**:
    ```python
    async def producer(queue):
        await queue.put("Item produced")
    
    async def consumer(queue):
        item = await queue.get()
        print(f"Consumed: {item}")
        queue.task_done()

    async def main():
        queue = asyncio.Queue()
        await asyncio.gather(producer(queue), consumer(queue))

    asyncio.run(main())
    ```

- **Explanation**: `Queue` is useful when working with tasks that need to share data, such as producers and consumers.

---

### 8. **`asyncio.wait_for(coro, timeout)`**
Waits for a coroutine to complete, raising a `TimeoutError` if it exceeds the given timeout.

- **Usage**:
    ```python
    async def long_task():
        await asyncio.sleep(5)
        return "Task complete"

    async def main():
        try:
            result = await asyncio.wait_for(long_task(), timeout=3)
            print(result)
        except asyncio.TimeoutError:
            print("Task timed out")

    asyncio.run(main())
    ```

- **Explanation**: Limits the time a coroutine is allowed to run. If the timeout is exceeded, an exception is raised.

---

### 9. **`asyncio.Event()`**
An event synchronization primitive to coordinate coroutines. One coroutine can set the event, and others can wait for it to be triggered.

- **Usage**:
    ```python
    import asyncio

    async def waiter(event):
        print("Waiting for the event...")
        await event.wait()
        print("Event triggered!")

    async def setter(event):
        await asyncio.sleep(2)
        event.set()

    async def main():
        event = asyncio.Event()
        await asyncio.gather(waiter(event), setter(event))

    asyncio.run(main())
    ```

- **Explanation**: It is used to signal between coroutines that some event has happened.

---

### 10. **`asyncio.shield(coro)`**
Prevents a coroutine from being canceled when wrapping it with `asyncio.shield()`.

- **Usage**:
    ```python
    async def task():
        await asyncio.sleep(5)
        print("Task completed")

    async def main():
        coro = task()
        try:
            await asyncio.shield(coro)
        except asyncio.CancelledError:
            print("Task shielded from cancellation")

    asyncio.run(main())
    ```

- **Explanation**: Protects a coroutine from being canceled by another operation or task.

---

### 11. **`asyncio.current_task()`**
Returns the currently running task.

- **Usage**:
    ```python
    import asyncio

    async def show_current_task():
        print(f"Current task: {asyncio.current_task()}")

    asyncio.run(show_current_task())
    ```

- **Explanation**: Useful for debugging or identifying the active task.

---

### 12. **`asyncio.run_coroutine_threadsafe(coro, loop)`**
Schedules the coroutine to run in a specified event loop from a different thread.

- **Usage**:
    ```python
    import asyncio
    import threading

    async def hello():
        print("Hello from asyncio")

    def run():
        loop = asyncio.new_event_loop()
        asyncio.run_coroutine_threadsafe(hello(), loop)

    thread = threading.Thread(target=run)
    thread.start()
    ```

- **Explanation**: Schedules coroutines to run in a different thread’s event loop.

---

### 13. **`asyncio.Future()`**
A low-level primitive representing a computation that hasn’t completed yet.

- **Usage**:
    ```python
    import asyncio

    async def set_future(future):
        await asyncio.sleep(2)
        future.set_result("Future result!")

    async def main():
        future = asyncio.Future()
        await asyncio.gather(set_future(future), future)
        print(future.result())

    asyncio.run(main())
    ```

- **Explanation**: Represents a result that will be available in the future, used in more advanced scenarios.

---

These basic functions provide a solid foundation for building asynchronous applications in Python using `asyncio`. Whether handling I/O-bound tasks or coordinating concurrent coroutines, `asyncio` provides the necessary tools.

___________________________________________________________________________________________________________________

### Python `asyncio` Intermediate Functions Cheatsheet

This cheatsheet covers more advanced features of Python's `asyncio` library for managing asynchronous tasks, synchronization primitives, and handling concurrency patterns in real-world applications.

---

### 1. **`asyncio.Task()`**
A `Task` object wraps a coroutine and allows it to be run in the background concurrently with other tasks.

- **Usage**:
    ```python
    import asyncio

    async def background_task():
        await asyncio.sleep(3)
        print("Background task completed")

    async def main():
        task = asyncio.create_task(background_task())
        print("Main task running")
        await task

    asyncio.run(main())
    ```

- **Explanation**: A `Task` schedules a coroutine to run concurrently, returning control to the event loop until awaited.

---

### 2. **`asyncio.as_completed()`**
Returns an iterator that yields tasks as they complete, regardless of their order.

- **Usage**:
    ```python
    import asyncio

    async def task(n):
        await asyncio.sleep(n)
        return f"Task {n} done"

    async def main():
        tasks = [task(3), task(1), task(2)]
        for completed_task in asyncio.as_completed(tasks):
            result = await completed_task
            print(result)

    asyncio.run(main())
    ```

- **Explanation**: Used to handle multiple tasks and process their results as they finish, rather than waiting for all to complete at once.

---

### 3. **`asyncio.wait()`**
Waits for multiple tasks with different completion criteria: `FIRST_COMPLETED`, `FIRST_EXCEPTION`, or `ALL_COMPLETED`.

- **Usage**:
    ```python
    import asyncio

    async def task_1():
        await asyncio.sleep(2)
        return "Task 1 complete"

    async def task_2():
        await asyncio.sleep(3)
        return "Task 2 complete"

    async def main():
        tasks = [task_1(), task_2()]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for t in done:
            print(await t)

    asyncio.run(main())
    ```

- **Explanation**: You can specify whether to wait for the first task to finish or wait for all tasks to complete.

---

### 4. **`asyncio.Condition()`**
Used for complex thread-safe interactions between coroutines, such as waiting for certain conditions.

- **Usage**:
    ```python
    import asyncio

    async def consumer(cond):
        print("Waiting for condition...")
        async with cond:
            await cond.wait()
            print("Condition met!")

    async def producer(cond):
        await asyncio.sleep(2)
        async with cond:
            print("Setting condition")
            cond.notify_all()

    async def main():
        cond = asyncio.Condition()
        consumer_task = asyncio.create_task(consumer(cond))
        producer_task = asyncio.create_task(producer(cond))

        await asyncio.gather(consumer_task, producer_task)

    asyncio.run(main())
    ```

- **Explanation**: `Condition` allows coroutines to wait for a certain condition to be met before they proceed.

---

### 5. **`asyncio.Semaphore()`**
Limits the number of concurrent tasks, useful for controlling resource usage.

- **Usage**:
    ```python
    import asyncio

    async def limited_task(sem, n):
        async with sem:
            await asyncio.sleep(1)
            print(f"Task {n} complete")

    async def main():
        sem = asyncio.Semaphore(2)
        tasks = [limited_task(sem, i) for i in range(5)]
        await asyncio.gather(*tasks)

    asyncio.run(main())
    ```

- **Explanation**: A semaphore is used to limit the number of concurrent tasks that can run, controlling access to resources.

---

### 6. **`asyncio.Lock()`**
Ensures that only one coroutine can access a critical section of code at any time.

- **Usage**:
    ```python
    import asyncio

    async def critical_section(lock, task_id):
        print(f"Task {task_id} waiting for lock")
        async with lock:
            print(f"Task {task_id} acquired lock")
            await asyncio.sleep(2)
            print(f"Task {task_id} released lock")

    async def main():
        lock = asyncio.Lock()
        tasks = [critical_section(lock, i) for i in range(3)]
        await asyncio.gather(*tasks)

    asyncio.run(main())
    ```

- **Explanation**: Use a lock to ensure that only one coroutine executes a critical section at a time.

---

### 7. **`asyncio.StreamReader` and `asyncio.StreamWriter`**
These are used for managing network streams, often in client-server applications.

- **Usage**:
    ```python
    import asyncio

    async def handle_client(reader, writer):
        data = await reader.read(100)
        message = data.decode()
        print(f"Received: {message}")

        writer.write(data)
        await writer.drain()
        writer.close()

    async def main():
        server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
        async with server:
            await server.serve_forever()

    asyncio.run(main())
    ```

- **Explanation**: Used to handle low-level TCP connections in an asynchronous way for both reading and writing data.

---

### 8. **`asyncio.gather()` vs `asyncio.wait()`**
Both can be used to schedule coroutines, but `gather()` is used when you want all tasks to run, whereas `wait()` provides more control over the timing and exceptions.

- **Usage**:
    ```python
    # asyncio.gather example
    results = await asyncio.gather(task1(), task2())

    # asyncio.wait example
    done, pending = await asyncio.wait([task1(), task2()], return_when=asyncio.FIRST_COMPLETED)
    ```

- **Explanation**: `gather()` is simpler and collects results, whereas `wait()` allows you to wait for one task to finish or all tasks to complete.

---

### 9. **`asyncio.TimeoutError`**
Raised when a task exceeds the allowed time limit.

- **Usage**:
    ```python
    import asyncio

    async def slow_task():
        await asyncio.sleep(5)

    async def main():
        try:
            await asyncio.wait_for(slow_task(), timeout=2)
        except asyncio.TimeoutError:
            print("Task timed out")

    asyncio.run(main())
    ```

- **Explanation**: Use `asyncio.wait_for()` to impose a time limit on a task, which will raise `TimeoutError` if the time exceeds the specified timeout.

---

### 10. **`asyncio.subprocess`**
Run subprocesses asynchronously. You can use `asyncio.create_subprocess_exec` to launch processes and communicate with them asynchronously.

- **Usage**:
    ```python
    import asyncio

    async def run_command():
        proc = await asyncio.create_subprocess_exec(
            'ls', '-l',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()
        print(f"stdout: {stdout.decode()}")
        print(f"stderr: {stderr.decode()}")

    asyncio.run(run_command())
    ```

- **Explanation**: Use `create_subprocess_exec` to launch external commands and handle their output asynchronously.

---

### 11. **`asyncio.run_coroutine_threadsafe()`**
Runs a coroutine in an event loop from a different thread. 

- **Usage**:
    ```python
    import asyncio
    import threading

    async def hello():
        print("Hello from async coroutine")

    def run_in_thread():
        loop = asyncio.new_event_loop()
        asyncio.run_coroutine_threadsafe(hello(), loop)

    thread = threading.Thread(target=run_in_thread)
    thread.start()
    ```

- **Explanation**: This is useful when you need to run an `asyncio` coroutine from a non-async thread (e.g., a GUI thread).

---

### 12. **`asyncio.shield()`**
Prevents a task from being canceled by other operations, such as a timeout.

- **Usage**:
    ```python
    import asyncio

    async def long_task():
        await asyncio.sleep(5)
        print("Task completed")

    async def main():
        try:
            await asyncio.wait_for(asyncio.shield(long_task()), timeout=2)
        except asyncio.TimeoutError:
            print("Timeout, but task was shielded from cancellation")

    asyncio.run(main())
    ```

- **Explanation**: `shield()` is useful when you want to protect certain coroutines from being canceled, ensuring that they run to completion.

---

These intermediate functions and concepts provide more powerful ways to manage tasks, synchronization, and concurrency in Python's `asyncio` library. They offer greater flexibility and control for handling real-world asynchronous programming challenges.

__________________________________________________________________________________________________________________________________


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
