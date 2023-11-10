class Node:
    def __init__( self, item ):
        self.mL = None
        self.mR = None
        self.mItem = item

class BST:

    def __init__( self ):
        self.mRoot = None

    def Insert( self, item ):
        if self.Exists( item ):
            return False
        n = Node( item )
        self.mRoot = self.InsertRecurse( n, self.mRoot )
        return True
    
    def InsertRecurse( self, n,current ):
        if current is None:
            return n
        if n.mItem < current.mItem:
            current.mL = self.InsertRecurse( n, current.mL )
        if n.mItem > current.mItem:
            current.mR = self.InsertRecurse( n, current.mR )
        return current
    
    def Exists( self, item ):
        return self.ExistsRecurse( item, self.mRoot )
    
    def ExistsRecurse( self, item,current ):
        if current is None:
            return False
        elif item < current.mItem:
            return self.ExistsRecurse( item, current.mL )
        elif item > current.mItem:
            return self.ExistsRecurse( item, current.mR )
        else:
            return True
    
    def __iter__( self ):
        yield from self.ItermRecursive( self.mRoot )
    
    def ItermRecursive( self, current ):
        if current is not None:
            yield from self.ItermRecursive( current.mL )
            yield current.mItem
            yield from self.ItermRecursive( current.mR )

    def Delete( self, item ):
        if not self.Exists( item ):
            return False
        self.mRoot = self.DeleteRecurse( item, self.mRoot )
        return True

    def DeleteRecurse( self, item,current ):
        if item < current.mItem:
            current.mL = self.DeleteRecurse( item, current.mL )
        if item > current.mItem:
            current.mR = self.DeleteRecurse( item, current.mR )
        else:
            if current.mL is None and current.mR is None:
                return None
            elif current.mL is not None and current.mR is None:
                return current.mL
            elif current.mL is None and current.mR is not None:
                return current.mR
            else:
                nextItem = current.mR
                while nextItem.mL:
                    nextItem = nextItem.mL
                current.mItem = nextItem.mItem
                current.mR = self.DeleteRecurse( nextItem.mItem,  current.mR )
        return current

    def Size( self ):
        return self.SizeRecurse( self.mRoot )
        
    def SizeRecurse( self, current ):
        if not current:
            return 0
        else:
            return 1 + self.SizeRecurse( current.mL )+self.SizeRecurse(current.mR)
    
    def Retrieve( self, item ):
        if not self.Exists( item ):
            return False
        return self.mRetrieveRecurse( item, self.mRoot )
    
    def mRetrieveRecurse( self, item,current ):
        if item < current.mItem:
            return self.RetrieveRecurse( item, current.mL )
        elif item > current.mItem:
            return self.RetrieveRecurse( item, current.mR )
        else:
            return current.mItem
