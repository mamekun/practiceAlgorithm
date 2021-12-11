'''
743. Network Delay Time
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
'''

from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(list)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1


s = Solution()

times1 = [[2,1,1],[2,3,1],[3,4,1]] # (source node, target node, weight)
n1 = 4 # number of nodes
k1 = 2 # start node

times2 = [[1,2,1]]
n2 = 2
k2 = 1

times3 = [[1,2,1]]
n3 = 2
k3 = 2

print(s.networkDelayTime(times1, n1, k1))
print(s.networkDelayTime(times2, n2, k2))
print(s.networkDelayTime(times3, n3, k3))