#!/usr/bin/env python

#
# Segment trees for range minimum query
# O(N) for preprocess
# O(logN) for query
# O(4*N) space

def init(st,l,b,e,n):
	if b>e: return
	if b==e: st[n]=l[b]
	else:
		init(st,l,b,(b+e)/2,2*n)
		init(st,l,(b+e)/2+1,e,2*n+1)
		st[n] = min(st[2*n],st[2*n+1])
def query(st,b,e,n,i,j):
	if b>=i and e<=j: return st[n]
	if i>e or j<b: return -1
	l = query(st,b,(b+e)/2,2*n,i,j)
	r = query(st,(b+e)/2+1,e,2*n+1,i,j)
	if l==-1:return r
	if r==-1:return l
	return min(l,r)
	
#	
# testcase
#
import timeit
import random
x=range(1,1000)
random.shuffle(x)
st=[0]*(4*len(x)+1)
init(st,x,0,len(x)-1,1)
def func():
	query(st,0,len(x)-1,1,0,len(x)-1)
tt = timeit.Timer("func()","from __main__ import func")
print "N = %d, t = %f" % (i,tt.timeit(5))



#
# plot
#

#from pylab import *
