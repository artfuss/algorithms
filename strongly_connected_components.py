'''
tarjan's algorithm for finding strongly connected components of 
a directed graph.
Applications:
1. creatind a subcomponents graph
2. finding all cycles in the graph
3. transitive closure of a graph
reference:
http://www.ics.uci.edu/~eppstein/161/960220.html#sca
http://en.wikipedia.org/wiki/Tarjan%E2%80%99s_strongly_connected_components_algorithm
''' 

def tarjan_recursive(g):
  S = []
  S_set = set()
  index = {}
  lowlink = {}
  ret = []

  def visit(v):
    index[v] = len(index)
    lowlink[v] = index[v]
    S.append(v)
    S_set.add(v)
    for w in g.get(v,()):
      if w not in index:
        visit(w)
        lowlink[v] = min(lowlink[w], lowlink[v])
      elif w in S_set:
        lowlink[v] = min(lowlink[v], index[w])
    if lowlink[v] == index[v]:
      scc = []
      w = None
      while v != w:
        w = S.pop()
        scc.append(w)
        S_set.remove(w)
      ret.append(scc)

  for v in g:
      if not v in index:
        visit(v)
  return ret
  
'''
g = {1: [2, 3], 2: [4], 3: [4, 6], 4: [5], 5: [2]}
print tarjan_recursive(g)
'''
