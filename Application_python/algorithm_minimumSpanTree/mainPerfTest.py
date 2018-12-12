#coding=utf-8
from denseGraph import DenseGraph
from sparseGraph import SparseGraph
from readGraph import ReadGraph
from component import Component
from path import Path
from shortestPath import ShortestPath
from lazyPrimMST import LazyPrimMST
from primMST import PrimMST
from kruskalMST import KruskalMST
import time

filenames = ["testG2.txt","testG3.txt","testG4.txt"]
vertexes = [250,1000,10000]
for i in range(len(filenames)):
    file = filenames[i]
    sparG = SparseGraph(vertexes[i], False)
    ReadGraph(sparG, file)
    #sparG.show()
    print "****%d File:%s****" % (i, file)
    print "...lazyPrimMST:"
    beginT1 = time.time()
    lpMST = LazyPrimMST(sparG)
    mst = lpMST.mstEdges()
    print "The MST weight is :",lpMST.result()
    endT1 = time.time()
    print "Total Time = %s " % (endT1-beginT1)

    print "...PrimMST:"
    beginT2 = time.time()
    primMST = PrimMST(sparG)
    mst = primMST.mstEdges()
    print "Test PrimMST："
    print "The MST weight is :",primMST.result()
    endT2 = time.time()
    print "Total Time = %s " % (endT2-beginT2)

    print "...PrimMST:"
    beginT3 = time.time()
    kruskalMST = KruskalMST(sparG)
    mst = kruskalMST.mstEdges()
    print "Test kruskaMST："
    print "The MST weight is :",kruskalMST.result()
    endT3 = time.time()
    print "Total Time = %s " % (endT3-beginT3)
