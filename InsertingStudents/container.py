
class Container:

    def __init__( self ):
        self.mContainer = []

    def Insert( self, x ):
        if self.Exists( x ):
            return False
        self.mContainer.append( x )

    def Exists( self, x ):
        for item in self.mContainer:
            if x == item: 
                return True
        return False


