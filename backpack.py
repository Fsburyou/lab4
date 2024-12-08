import numpy as np

def backpack(items, capacity):
    dp = [0] * (capacity + 1)
    things = [None] * (capacity + 1)

    for i in range(len(items)):
        size = items[i][0]
        points = items[i][1]

        for weight in range(capacity, size - 1, -1):
            if dp[weight - size] + points > dp[weight]:
                dp[weight] = dp[weight - size] + points
                things[weight] = items[i]

    cur = capacity
    ans = []
    while cur > 0 and things[cur]:
        ans += things[cur]
        cur -= things[cur][0]

    return ans[::-1]


if __name__ == '__main__':
    items = [[3, 25, 'r'], [2, 15, 'p'], [2, 15, 'a'],
             [2, 20, 'm'], [1, 5, 'i'], [1, 15, 'k'],
             [3, 20, 'x'], [1, 25, 't'], [1, 15, 'f'],
             [2, 20, 's'], [2, 20, 'c']]
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    capacity = 9
    ans = backpack(items, capacity)

    points = 10
    capacity = 8
    pr = []
    for i in range(int(len(ans) / 3)):
        if capacity - ans[i * 3 + 2] >= 0:
            points += ans[i * 3 + 1]
            capacity -= ans[i * 3 + 2]
            pr += ans[i * 3]
        else:
            continue
    pr += ['d']

    for i in range(len(items)):
        if items[i][2] not in pr:
            points -= items[i][1]

    pr = np.array(pr)
    pr = pr.reshape(2,-1)
    print(pr)
    print('Points:', points)
    #max_value = knapsack(items, capacity)
    #print(max_value)