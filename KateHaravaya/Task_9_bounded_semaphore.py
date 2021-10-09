'''Task 9. Optional
Try different synchronization primitives and fix deadlock
in [dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem).'''

import random
from threading import BoundedSemaphore, Thread
from time import sleep

def philosophers_life(id, num_ph, forks):
    name = f"Philosopher{id}"

    time_to_wait_range_begin = 0.5
    time_to_wait_range_end = 1

    while True:
        left_fork_id = id
        right_fork_id = id - 1 if id > 0 else num_ph - 1

        # taking forks
        forks[left_fork_id].acquire()

        # if we want to see a deadlock then uncomment next line
        #sleep(0.2)

        forks[right_fork_id].acquire()

        print(f"Philosopher {id} is eating")
        sleep(random.uniform(time_to_wait_range_begin, time_to_wait_range_end))

        # putting fork
        forks[left_fork_id].release()
        forks[right_fork_id].release()

        print(f"Philosopher {id} is thinking")
        sleep(random.uniform(time_to_wait_range_begin, time_to_wait_range_end))


def dinning_problem(num_philosophers):
    forks = []
    for i in range(num_philosophers):
        new_fork = BoundedSemaphore(1)
        forks.append(new_fork)

    # Creating philosophers
    threads = []
    for i in range(num_philosophers):
        thread = Thread(target=philosophers_life, args=(i, num_philosophers, forks,))
        thread.start()
        threads.append(thread)

dinning_problem(5)