#Task 9.1 Implement the [dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem).

import random
from threading import Lock, Thread
from time import sleep

def philosophers_life(id, num_ph, forks):
    name = f"Philosopher{id}"

    time_to_wait_range_begin = 0.5
    time_to_wait_range_end = 1
    time_to_wait_for_right_fork = 1

    while True:
        left_fork_id = id
        right_fork_id = id - 1 if id > 0 else num_ph - 1

        # taking forks
        forks[left_fork_id].acquire()

        # This line I used to illustrate deadlock
        # But now deadlock will not happen because we resolved it further
        sleep(0.2)

        # I try to used timed .acquire method to see if phylosopher can get fork to the right
        # in 1 second, and if phylosopher can not, then he should release his left fork
        # to let someone else eating
        if forks[right_fork_id].acquire(True, time_to_wait_for_right_fork):
            print(f"Philosopher {id} is eating")
            sleep(random.uniform(time_to_wait_range_begin, time_to_wait_range_end))

            # putting fork
            forks[left_fork_id].release()
            forks[right_fork_id].release()

        else:
            forks[left_fork_id].release()

        print(f"Philosopher {id} is thinking")
        sleep(random.uniform(time_to_wait_range_begin, time_to_wait_range_end))


def dinning_problem(num_philosophers):
    forks = []
    for i in range(num_philosophers):
        new_fork = Lock()
        forks.append(new_fork)

    # Creating philosophers
    threads = []
    for i in range(num_philosophers):
        thread = Thread(target=philosophers_life, args=(i, num_philosophers, forks,))
        thread.start()
        threads.append(thread)

dinning_problem(5)