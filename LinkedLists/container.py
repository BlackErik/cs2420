class Node:
    def __init__( self, item, n ):
        self.mItem = item
        self.mNext = n

class Container:

    def __init__( self ):
        self.mFirst = None

    def Insert( self, item ):
        if self.Exists( item ):
            return False
        n = Node( item, None )
        n.mNext = self.mFirst
        self.mFirst = n

    def Exists( self, item ):
        current = self.mFirst
        while current is not None:
            if current.mItem == item:
                return True
            current = current.mNext
        return False

    def __iter__( self ):
        current = self.mFirst
        while current is not None: 
            yield current.mItem
            current = current.mNext

    def Delete( self, item ):
        if not self.Exists( item ):
            return False

        current = self.mFirst

        if self.mFirst.mItem == item:
            self.mFirst = self.mFirst.mNext
            return True

        while current is not None:
            if current.mNext.mItem == item:
                current.mNext = current.mNext.mNext
                return True
            current = current.mNext
        return False

    def Retrieve( self, item ):
        current = self.mFirst
        while current is not None:
            if current.mItem == item:
                return current.mItem
            current = current.mNext
        return False

    def Size( self ):
        current = self.mFirst
        count = 0
        while current is not None:
            count += 1
            current = current.mNext
        return count
    
        
