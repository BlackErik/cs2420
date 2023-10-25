from graphics import *

class Stack:
    def __init__( self ):
        self.mA = [] 

    def Push( self, item ):
        self.mA.append( item )

    def Pop( self ):
        x = self.mA.pop()
        return x

    def Top( self ):
        return self.mA[ -1 ]

    def IsEmpty( self ):
        if len(self.mA) == 0:
            return True
        else:
            return False

def infixToPostfix( infix ):
    postfix = ""
    s = Stack()
    for c in infix:
        if c in "0123456789":
            postfix += c
        elif c == 'x':
            postfix += c
        elif c in "+-":
            if not s.IsEmpty():
                while s.Top() in "+-*/":
                    postfix += s.Pop()
            s.Push( c )
        elif c in "*/":
            if not s.IsEmpty():
                if s.Top() == "*" or s.Top() == "/":
                    postfix += s.Pop()
            s.Push( c )
        elif c == '(':
            s.Push( c )
        elif c == ')':
            while s.Top() != '(':
                postfix += s.Pop()
            s.Pop()
    while not s.IsEmpty():
        postfix += s.Pop()
    return postfix

def evaulatePostfix( postfix, x ):
    s = Stack()
    for c in postfix:
        if c in "0 1 2 3 4 5 6 7 8 9":
            s.Push( float( c ) )
        elif c == 'x':
            s.Push( x )
        elif c == '*' :
            rhs = s.Pop()
            lhs = s.Pop()
            s.Push( lhs * rhs )
        elif c == '/':
            rhs = s.Pop()
            lhs = s.Pop()
            s.Push( lhs / rhs )
        elif c == '-':
            rhs = s.Pop()
            lhs = s.Pop()
            s.Push( lhs - rhs )
        elif c == '+':
            rhs = s.Pop()
            lhs = s.Pop()
            s.Push( lhs + rhs )
    return s.Pop()

def printInstructions():
    print( "Enter single digit values only, * / + - ( ) only allowed")

def main():
    printInstructions()
    function = input( "Enter Expression: " ) 
    postfix = infixToPostfix( function )
    pts = []
    xlow = -10
    ylow = -10
    xhigh = 10
    yhigh = 10
    x = xlow
    while x <= xhigh:
        y = evaulatePostfix( postfix, x )
        pts.append( [ x, y ] )
        x += .1
    win = GraphWin( "Graphing Calculator", 500, 500 )
    win.setCoords( xlow, ylow, xhigh, yhigh )
    for i in range( len( pts ) -1 ):
        x = pts[ i ][ 0 ]
        y = pts[ i ][ 1 ]
        x2 = pts[ i + 1 ][ 0 ]
        y2 = pts[ i + 1 ][ 1 ]
        line = Line( Point( x, y ), Point( x2, y2 ) )
        line.draw( win )
    win.getMouse()
    win.close()

main()