#coding=utf-8
from sparseGraph import SparseGraph
from readGraph import ReadGraph
from component import Component
from dijkstra import Dijkstra

def testDijkstra():
    filename = "testG1.txt"
    sparG = SparseGraph(5, True)
    ReadGraph(sparG, filename)
    #sparG.show()

    dij = Dijkstra(sparG, 0)
    for i in range(sparG.V()):
        if(dij.hasPathTo(i)):
            dij.showPath(i)
        else:
            print "No Path To %d " % i

testDijkstra()

