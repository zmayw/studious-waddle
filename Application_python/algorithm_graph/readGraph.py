#coding=utf-8

class ReadGraph:

    def __init__(self, graph, file):
        self.graph = graph
        graphfile = open(file)
        data = graphfile.readlines()
        header = data[0].split()
        V = int(header[0])
        E = int(header[1])

        if V != self.graph.V():
            raise Exception,"V is not except value."

        for i in range(E):
            line = data[i+1].split()
            a,b = int(line[0]),int(line[1])
            self.outOfRang(a,V)
            self.outOfRang(b,V)
            graph.addEdge(a,b)


    def outOfRang(self,x,len,begin_index=0):
        if ( x < begin_index or x>= len):
            raise "The node is out of range(0-%d)" % len

