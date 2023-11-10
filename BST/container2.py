class Node:
    def __init__( self, item ):
        self.mL = None
        self.mR = None
        self.mItem = item

class Container:

    def __init__( self ):
        self.mRoot = None

    def Insert( self, item ):
        if self.Exists( item ):
            return False
        n = Node( item )
        self.mRoot = self.InsertR( n, self.mRoot )
        return True

    def InsertR( self, n, current ):
        if current is None:
            return n
        if n.mItem < current.mItem:
            current.mL = self.InsertR( n, current.mL)
        elif n.mItem > current.mItem:
            current.mR = self.InsertR( n, current.mR)
        return current

    def Exists( self, item ):
        return self.ExistsR( item, self.mRoot )

    def ExistsR( self, item, current ):
        if current is None:
            return False
        elif item < current.mItem:
            return self.ExistsR( item, current.mL )
        elif item > current.mItem:
            return  self.ExistsR( item, current.mR )
        else:
            return True

    def __iter__( self ):
        yield from self.IterRecursive( self.mRoot )
    
    def IterRecursive( self, current ):
        if current is not None:
            yield from self.IterRecursive( current.mL )
            yield current.mItem
            yield from self.IterRecursive( current.mR)

    def Delete( self, item ):
        if not self.Exists( item ):
            return False
        self.mRoot = self.DeleteR( item, self.mRoot )
        return True

    def DeleteR( self, item, current) :
        if item < current.mItem:
            current.mL = self.DeleteR( item, current.mL )
        elif item > current.mItem:
            current.mR = self.DeleteR( item, current.mR )
        else:
            if current.mL is None and current.mR is None:
                return None
            elif current.mL is not None and current.mR is None:
                return current.mL
            elif current.mL is None and current.mR is not None:
                return current.mR
            else:
                successor = current.mR
                while successor.mL:
                    successor = successor.mL
                current.mItem = successor.mItem
                current.mR = self.DeleteR( successor.mItem, current.mR )
        return  current

    def Retrieve( self, item ):
        if not self.Exists( item ):
            return False
        else:
            return self.RetrieveR( item, self.mRoot )

    def RetrieveR( self, item, current):
        if item < current.mItem:
            return self.RetrieveR( item, current.mL )
        elif item > current.mItem:
            return self.RetrieveR( item, current.mR )
        else:
            return current.mItem

    def Size( self ):
        return self.SizeR( self.mRoot);
    
    def SizeR( self, current ):
        if not current: 
            return 0
        else: 
            return 1 + self.SizeR( current.mL ) + self.SizeR( current.mR )
        

