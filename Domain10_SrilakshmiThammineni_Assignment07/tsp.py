from itertools import combinations

def traveling_salesman(dist):
    n = len(dist)
    all_visited = (1 << n) - 1
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u): 
                for v in range(n):
                    if not (mask & (1 << v)): 
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v],
                                              dp[mask][u] + dist[u][v])
    min_cost = float('inf')
    for i in range(1, n):
        min_cost = min(min_cost, dp[all_visited][i] + dist[i][0])

    return min_cost



dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum cost of TSP route:", traveling_salesman(dist_matrix))
