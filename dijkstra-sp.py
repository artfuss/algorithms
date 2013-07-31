'''
single source shortest path
with non-negative edge weights
may contain cycles
'''

def dijkstra(g,w,s):
  INF = 99999999
  dist = defaultdict(lambda: INF)
  dist[s] = 0
  Q = []
  hpush(Q,(dist[s],s))
  #for u in G:
    #hpush(Q,(dist[u],u))
  while Q:
    du,u = hpop(Q)
    if du == INF: break
    for v in g[u]:
      alt = du + w[(u,v)]
      if alt < dist[v]:
        dist[v] = alt
        hpush(Q,(dist[v],v))
  return dist
  
'''
  e.g.
  g= {1:[2],2[3]} #defaultdict(lsit)
  w = {(1,2):5,(2,3):7} #defaultdict(tuple)
  print dijkstra(g,w,1)[2] #prints the sp from 1->2
'''
