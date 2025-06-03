'''

You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

 

Example 1:

Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)
Example 2:

Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)
Example 3:

Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.

'''

from collections import deque

def maxTasks(tasks, workers, pills, strength):
    # Sort tasks and workers
    tasks.sort()
    workers.sort()

    def canComplete(mid):
        task_deque = deque(tasks[:mid])  # Consider the first `mid` tasks
        available_workers = deque(workers)
        remaining_pills = pills

        while task_deque:
            current_task = task_deque.pop()
            # Try to assign a worker without a pill
            while available_workers and available_workers[-1] >= current_task:
                available_workers.pop()
                break
            else:
                # Try to use a pill on the weakest worker who can handle the task
                if remaining_pills > 0:
                    while available_workers and available_workers[0] + strength < current_task:
                        available_workers.popleft()
                    if available_workers and available_workers[0] + strength >= current_task:
                        available_workers.popleft()
                        remaining_pills -= 1
                    else:
                        return False  # No workers can handle this task
                else:
                    return False  # No pills left and no workers available
        return True

    # Binary search over the number of tasks
    left, right, result = 0, min(len(tasks), len(workers)), 0
    while left <= right:
        mid = (left + right) // 2
        if canComplete(mid):
            result = mid  # Update result to the maximum feasible `mid`
            left = mid + 1  # Try for more tasks
        else:
            right = mid - 1  # Try for fewer tasks

    return result