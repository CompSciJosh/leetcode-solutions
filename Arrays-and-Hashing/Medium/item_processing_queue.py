# Joshua Jackson
# Similar Problem No. 1: "Task Scheduler" (#621)
# Similar Problem No. 2: "Single-Threaded CPU" (#1834)
# Similar Problem No. 3: "Design Circular Queue" (#622)
# Similar Problem No. 4: "Design Circular Deque" (#641)
# Similar Problem No. 5: "Number of Recent Calls" (#933)
# Language: Python
# Difficulty: Medium

"""
This problem has elements of round-robin scheduling with varying time requirements.
It combines queue processing with simulation, which makes it an interesting hybrid problem.

Start with "Task Scheduler" (#621) and "Single-Threaded CPU" (#1834) as they involve the most similar concepts of
processing items in a specific order with time tracking.

Description:
There are N clients who have ordered N handmade items.
The K-th client ordered exactly one item that takes T[K] hours to make.
There is only one employee who makes items for clients, and they work in the following manner:
	* spend one hour making the first item;
	* if the item is finished, the employee delivers it to the client immediately;
    * if the item is not finished, they put it after the N-th item for further work;
    * the employee starts making the next item.

For example for T = [3, 1, 2], the employee spends 6 hours making items in the following order: [1, 2, 3, 1, 3, 1].
The first client waited 6 hours for their item, the second client received their item after 2 hours and the third client after 5 hours. What is the total time that clients need to wait for all ordered items? For the above example, the answer is 6 + 2 + 5 = 13.

As the result may be large, return its last nine digits without leading zeros (in other words, return the result modulo 10**9).

Write a function:

def solution(T);

that, given an array of integers T of length N, returns the total time that the clients need to wait (modulo 10**9).

Examples:
    1. Given T = [3, 1, 2], the function should return 13 as explained above.
    2. Given T = [1, 2, 3, 4], the function should return 24.
        * The employee prepares the items in the following order: 1, 2, 3, 4, 2, 3, 4, 3, 4, 4.
        * The first client waited for 1 hour, the second client for 5 hours, the third client for 8 hours, and the fourth client for 10 hours.
        * The total waiting time of all clients is 1 + 5 + 8 + 10 = 24 hours.
    3. Given T = [7, 7, 7], the function should return 60.
    4. Given T = [10000], the function should return 10000.

Write an efficient algorithm for the following assumptions:
	* N is an integer within the range [1..100,000];
	* each element of array T is an integer within the range [1..10,000].

Note: Place code in 'solution.py' file and place test input in the file 'test-input.txt'
"""

"""*************** Code Below ***************"""
""" 
Beginning of Solution
"""

def solution(T):
    """
    Calculate the total waiting time for clients to receive their items.

    Args:
        T: List of integers where T[K] is the time required to make item K

    Returns:
        The total waiting time modulo 10^9
    """
    n = len(T)
    # Create a queue of items to process (item_index, remaining_time)
    queue = [(i, T[i]) for i in range(n)]

    total_wait_time = 0  # Total time all clients need to wait
    current_hour = 0  # Current processing hour

    while queue:
        current_hour += 1
        item_index, remaining_time = queue.pop(0)

        remaining_time -= 1

        if remaining_time == 0:
            # Item is completed, client waits from 0 to current_hour
            total_wait_time += current_hour
        else:
            # Item is not finished, put it back at the end of the queue
            queue.append((item_index, remaining_time))

    # Return the result modulo 10^9
    return total_wait_time % (10 ** 9)


# Test cases
test_cases = [
    [3, 1, 2],  # Example 1: Should return 13
    [1, 2, 3, 4],  # Example 2: Should return 24
    [7, 7, 7],  # Example 3: Should return 60
    [10000],  # Example 4: Should return 10000
]

for idx, test in enumerate(test_cases):
    result = solution(test)
    print(f"Test case {idx + 1}: {result}")