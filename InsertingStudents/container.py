
class Container:

    def __init__( self ):
        self.mContainer = []

    def Insert( self, x ):
        if self.Exists( x ):
            return False
        self.mContainer.append( x )
        return True

    def Exists( self, x ):
        for item in self.mContainer:
            if x == item: 
                return True
        return False

    def Delete( self, x ):
        if not self.Exists( x ):
            return False
        for i in range( len( self.mContainer )):
            if self.mContainer[ i ] == x:
                self.mContainer.pop( i )
                return True
    
    def Retrieve( self, x ):
        if not self.Exists( x ):
            return False
        for i in range( len( self.mContainer )):
            if self.mContainer[ i ] == x:
                return self.mContainer[ i ]

    def Size( self ):
        return len( self.mContainer )
        

    def __iter__( self ):
        for item in self.mContainer:
            yield item