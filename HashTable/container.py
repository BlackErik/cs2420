import math

def isPrime(size):
    if size==2:
        return True
    s = int(math.sqrt(size))
    for i in range(2,s+1):
        if size%i==0:
            return False
    return True
    
class Container:

    def __init__(self, num_items):
        self.mTableSize = 2*num_items + 1
        while not isPrime(self.mTableSize):
            self.mTableSize += 2
        self.mTable = []
        for i in range(self.mTableSize):
            self.mTable.append(None)

    def Insert( self, item ):
        if not self.Exists( item ):
            key = hash( item )
            index = key % self.mTableSize
            while self.mTable[ index ]:
                index += 1
                if index >= self.mTableSize:
                    index = 0
            self.mTable[index] = item
            return True
        return False

            

    def Exists( self, item ):
        key = hash(item)
        index = key % self.mTableSize
        while True:
            if self.mTable[index] is None:
                return False
            if self.mTable[index] and self.mTable[index] == item: 
                return True
            index += 1
            if index >= self.mTableSize:
                index = 0

    def __iter__( self ):
        for item in self.mTable:
            if item:
                yield item
        return

    def Delete( self, item ):
        if not self.Exists( item ):
            return False
        key = hash( item )
        index = key % self.mTableSize
        while True:
            if self.mTable[index] and self.mTable[index] == item:
                self.mTable[index] = False
                return True
            else:
                index += 1
                if index >= self.mTableSize:
                    index = 0
        

    def Retrieve( self, item ):
        key = hash(item)
        index = key % self.mTableSize
        while True:
            if self.mTable[index] is None:
                return None
            if self.mTable[index] and self.mTable[index] == item:
                return self.mTable[index]
            index += 1
            if index >= self.mTableSize:
                index = 0

    def Size( self ):
        count = 0
        for item in self.mTable:
            if item:
                count += 1
        return count
