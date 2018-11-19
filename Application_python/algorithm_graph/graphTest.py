#coding=utf-8
from denseGraph import *
from sparseGraph import *
from readGraph import *
from component import *
from path import *
from shortestPath import *

def readGraphTest():
    filename = "testGraph.txt"
    sparG = SparseGraph(13,False)
    ReadGraph(sparG,filename)
    sparG.show()

    denG = DenseGraph(13,False)
    ReadGraph(denG,filename)
    denG.show()



def componentTest():
    filename = "testGraph.txt"
    sparG1 = SparseGraph(13,False)
    ReadGraph(sparG1,filename)
    sparComp1 = Component(sparG1)
    print "testGraph1,Component Count:",sparComp1.ccount

    filename = "testGraph2.txt"
    sparG2 = SparseGraph(7,False)
    ReadGraph(sparG2,filename)
    sparComp2 = Component(sparG2)
    print "testGraph2,Component Count:",sparComp2.ccount


def pathTest():
    filename = "testGraph2.txt"
    sparG2 = SparseGraph(7,False)
    ReadGraph(sparG2,filename)
    sparG2.show()

    dfs = Path(sparG2,0)
    print "DFS:",
    dfs.showPath(4)

    bfs = ShortestPath(sparG2,0)
    print "BFS:",
    bfs.showPath(4)


#componentTest()
pathTest()
