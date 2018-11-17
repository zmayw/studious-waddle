#coding=utf-8
from denseGraph import *
from sparseGraph import *
from readGraph import *

def main():
    filename = "testGraph.txt"
    sparG = SparseGraph(13,False)
    ReadGraph(sparG,filename)
    sparG.show()

    denG = DenseGraph(13,False)
    ReadGraph(denG,filename)
    denG.show()

main()