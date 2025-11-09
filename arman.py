def findWaitingTime(processes):
    n = len(processes)
    rt = [p[1] for p in processes]  # Remaining burst times
    wt = [0] * n
    complete = 0
    t = 0

    while complete < n:
        # Find process with minimum remaining time at current time
        idx = -1
        min_rt = float('inf')
        for i in range(n):
            if processes[i][2] <= t and rt[i] > 0 and rt[i] < min_rt:
                min_rt = rt[i]
                idx = i

        if idx == -1:
            t += 1
            continue

        rt[idx] -= 1
        if rt[idx] == 0:
            complete += 1
            wt[idx] = t + 1 - processes[idx][1] - processes[idx][2]
            if wt[idx] < 0:
                wt[idx] = 0
        t += 1

    return wt


def findTurnAroundTime(processes, wt):
    return [processes[i][1] + wt[i] for i in range(len(processes))]


def findavgTime(processes):
    wt = findWaitingTime(processes)
    tat = findTurnAroundTime(processes, wt)

    print("PID\tBurst\tArrival\tWaiting\tTurnaround")
    for i, p in enumerate(processes):
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage waiting time = {sum(wt)/len(wt):.2f}")
    print(f"Average turnaround time = {sum(tat)/len(tat):.2f}")


if __name__ == "__main__":
    processes = [
        [11, 6, 1],
        [21, 8, 1],
        [31, 7, 2],
        [41, 3, 3]
    ]
    findavgTime(processes)
