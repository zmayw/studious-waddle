#coding=utf-8
from sparseGraph import SparseGraph
from readGraph import ReadGraph
from component import Component
from dijkstra import Dijkstra
from bellmanFord import BellmanFord

def testBellmanFord():
    filename = "testG2.txt"
    sparG = SparseGraph(5, True)
    ReadGraph(sparG, filename)
    #sparG.show()
    s = 0
    bellmanFord = BellmanFord(sparG, s)
    if bellmanFord.negativeCycle()==True:
        print "The graph contain negative cycle!"
    else:
        for i in range(sparG.V()):
            if (i == s):
                continue

            if bellmanFord.hasPathTo(i):
                bellmanFord.showPath(i)
            else:
                print "No Path To %d " % i

testBellmanFord()

