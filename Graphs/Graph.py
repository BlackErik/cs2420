class MyQueue:
    def __init__( self ):
        self.queue = []
        return
    
    def Enqueue( self, item ):
        self.queue.append(item)
        return
    
    def Dequeue( self ):
        self.queue.reverse()
        item = self.queue.pop()
        self.queue.reverse()
        return item

    def IsEmpty( self ):
        if len( self.queue ) == 0:
            return True
        return False

class Graph:
    def __init__( self, NumVertices ):
        self.mNeighbors = []
        for i in range ( NumVertices ):
            self.mNeighbors.append([])
    
    def AddEdge( self, v0, v1 ):
        self.mNeighbors[v0].append(v1)
    
    def IsEdge( self, v0, v1 ):
        return v1 in self.mNeighbors[v0]

    def GetNeighbors( self, v ):
        return self.mNeighbors[v]

    def FindPath( self, v0, v1 ):
        Q = MyQueue()
        From = []
        for i in range( len( self.mNeighbors)):
            From.append( -1 )
        Q.Enqueue( v0 )
        From[ v0 ] = v0
        while not Q.IsEmpty():
            c = Q.Dequeue()
            if c == v1:
                path = [c]
                while From[c] != c:
                    c = From[c]
                    path.append(c)
                path.reverse()
                return path
            for neighbor in self.mNeighbors[c]:
                if From[neighbor] == -1:
                    Q.Enqueue( neighbor)
                    From[neighbor] = c
        return None

        