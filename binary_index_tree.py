class bit:
  def __init__(self,freq):
    self.MAX_IDX = len(freq)+1
    self.tree = [0]*self.MAX_IDX
    for i,v in enumerate(freq):
      self.update(i+1,v)
  def update(self,idx, value):
    while idx <= self.MAX_IDX:
        self.tree[idx] += value
        idx += (idx & -idx)
  def find(self,idx):
    val = 0
    while idx:
      val += self.tree[idx]
      idx -= idx & -idx
    return val
  def __str__(self): return ','.join(map(str,self.tree))


'''
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=binaryIndexedTrees
BINARY INDEXED TREE 
Note: BIT index starts from 1...N+1
freq = [1,0,2,1,1,3,0,4,2,5,2,2,3,1,0,2]
b = bit(freq)
for i in xrange(len(freq)):
    print b.find(i+1)
'''
