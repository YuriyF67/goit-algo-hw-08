import heapq


def min_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second

        heapq.heappush(cables, cost)

        total_cost += cost

    return total_cost


cables = [1, 2, 3, 7, 10, 11, 14]
print("Мinimun cost to connect cables:", min_cost(cables))
