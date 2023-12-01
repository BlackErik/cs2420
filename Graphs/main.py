from Graph import Graph

def main():
    fin = open("Graph.txt", "r")
    NumVertices = int( fin.readline() )
    G = Graph( NumVertices )
    NumEdges = int( fin.readline() )
    for e in range( NumEdges ):
        line = fin.readline()
        words = line.split()
        G.AddEdge( int( words[0]), int(words[1] ))
    NumTests = int( fin.readline() )
    for t in range( NumTests ):
        line = fin.readline()
        words = line.split()
        path = G.FindPath( int(words[0]), int( words[1] ))
        if path == None:
            print( "There is no path from pont", words[0], "to point", words[1])
        else:
            print( "The path from point", words[0], "to point", words[1], "is", path )

main()