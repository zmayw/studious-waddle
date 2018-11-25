#coding=utf-8
from denseGraph import DenseGraph
from sparseGraph import SparseGraph
from readGraph import ReadGraph
from component import Component
from path import Path
from shortestPath import ShortestPath
from lazyPrimMST import LazyPrimMST
from primMST import PrimMST

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


def weightTest():
    filename = "testGraph.txt"
    sparG = SparseGraph(8,False)
    ReadGraph(sparG,filename)
    sparG.show()

    print "**********************"

    densG = DenseGraph(8, False)
    ReadGraph(densG, filename)
    densG.show()

def lazyPrimMSTTest():
    filename = "testGraph.txt"
    sparG = SparseGraph(8,False)
    ReadGraph(sparG,filename)
    #sparG.show()

    lazyPrimMST = LazyPrimMST(sparG)
    mst = lazyPrimMST.mstEdges()
    print "Test lazyPrimMST："
    for i in range(len(mst)):
        print "(%d-%d:%f)" % (mst[i].v(),mst[i].w(),mst[i].weight())
    print ""
    print "The MST weight is :",lazyPrimMST.result()

def primMSTTest():
    filename = "testGraph.txt"
    sparG = SparseGraph(8, False)
    ReadGraph(sparG, filename)
    #sparG.show()

    primMST = PrimMST(sparG)
    mst = primMST.mstEdges()
    print "Test PrimMST："
    for i in range(len(mst)):
        print "(%d-%d:%f)" % (mst[i].v(),mst[i].w(),mst[i].weight())
    print ""
    print "The MST weight is :",primMST.result()


#lazyPrimMSTTest()
primMSTTest()
