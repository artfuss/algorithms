'''
bipartite graph
hopkroft karp algorithm
maximum matching
'''

from collections import deque
from collections import defaultdict

NIL = 0
INF = -1

def bfs():
    Q = deque()
    for i in xrange(1,n+1):
        if match[i]==NIL:
            dist[i] = 0
            Q.append(i)
        else:
            dist[i] = INF
    dist[NIL] = INF
    while Q:
        u = Q.popleft()
        if u!=NIL:
            l = len(G[u])
            for i in xrange(l):
                v = G[u][i]
                if dist[match[v]]==INF:
                    dist[match[v]] = dist[u] + 1
                    Q.append(match[v])
    return dist[NIL]!=INF


def dfs(u):
    if u!=NIL:
        l = len(G[u])
        for i in xrange(l):
            v = G[u][i]
            if dist[match[v]]==dist[u]+1:
                if(dfs(match[v])):
                    match[v] = u
                    match[u] = v
                    return True
        dist[u] = INF
        return False
    return True

def hopcroft_karp():
    matching = 0
    # match[] is assumed NIL for all vertex in G
    while(bfs()):
        for i in xrange(1,n+1):
            if match[i]==NIL and dfs(i):
                matching += 1
    return matching



'''
Initialize the following before calling hopkroft_karp:
n: number of nodes on left side, nodes are numbered 1 to n
m: number of nodes on right side, nodes are numbered n+1 to n+m
G = NIL[0] ? G1[G[1---n]] ? G2[G[n+1---n+m]]
(u,v) and (v,u) both should be added to G
Example:
n = 4
m = 4
match = [NIL for _ in xrange(n+m+1)]
dist = [INF for _ in xrange (n+m+1)]
G = defaultdict(list)
    G[NIL] = []
    G[1] = [6]
    G[2] = [5,6,7]
    G[3] = [6]
    G[4] = [6,7,8]
    G[5] = [2]
    G[6] = [1,2,3,4]
    G[7] = [2,4]
    G[8] = [4]
'''
