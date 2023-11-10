class Node:
    def __init__(self,item):
        self.L = None
        self.R = None
        self.mItem = item

class BST:

    def __init__(self):
        self.mRoot = None

    def Insert(self,item):
        if self.Exists(item):
            return False
        node = Node(item)
        self.mRoot = self.InsertRecurse(node,self.mRoot)
        return True
    
    def InsertRecurse(self,node,current):
        if current is None:
            return node
        if node.mItem < current.mItem:
            current.L = self.InsertRecurse(node,current.L)
        if node.mItem > current.mItem:
            current.R = self.InsertRecurse(node,current.R)
        return current
    
    def Exists(self,item):
        return self.ExistsRecurse(item,self.mRoot)
    
    def ExistsRecurse(self,item,current):
        if current is None:
            return False
        elif item < current.mItem:
            return self.ExistsRecurse(item,current.L)
        elif item > current.mItem:
            return self.ExistsRecurse(item,current.R)
        else:
            return True
    
    def __iter__(self):
        yield from self.IterRecursive(self.mRoot)
    
    def IterRecursive(self,current):
        if current is not None:
            yield from self.IterRecursive(current.L)
            yield current.mItem
            yield from self.IterRecursive(current.R)

    def Delete(self,item):
        if not self.Exists(item):
            return False
        self.mRoot = self.DeleteRecurse(item,self.mRoot)
        return True

    def DeleteRecurse(self,item,current):
        if item < current.mItem:
            current.L = self.DeleteRecurse(item,current.L)
        if item > current.mItem:
            current.R = self.DeleteRecurse(item,current.R)
        else:
            if current.L is None and current.R is None:
                return None
            elif current.L is not None and current.R is None:
                return current.L
            elif current.L is None and current.R is not None:
                return current.R
            else:
                nextItem = current.R
                while nextItem.L:
                    nextItem = nextItem.L
                current.mItem = nextItem.mItem
                current.R = self.DeleteRecurse(nextItem.mItem, current.R)
        return current

    def Size(self):
        return self.SizeRecurse(self.mRoot)
        
    def SizeRecurse(self,current):
        if not current:
            return 0
        else:
            return 1 + self.SizeRecurse(current.L)+self.SizeRecurse(current.R)
    
    def Retrieve(self,item):
        if not self.Exists(item):
            return False
        return self.RetrieveRecurse(item,self.mRoot)
    
    def RetrieveRecurse(self,item,current):
        if item < current.mItem:
            return self.RetrieveRecurse(item,current.L)
        elif item > current.mItem:
            return self.RetrieveRecurse(item,current.R)
        else:
            return current.mItem
