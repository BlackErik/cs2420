import random
import math
import sys

class Counter: 
    def __init__( self ):
        self.compares = 0

def BubbleSort( A, c ):
    changes = True;
    while changes == True:
        changes = False;
        for i in range( 0, len( A ) - 1 ):
            c.compares += 1
            if A[ i ] > A[ i + 1 ]:
                A[ i ], A[ i + 1 ] = A[ i + 1 ], A[ i ]
                changes = True
    return A

def ShakerSort( A, c ):
    changes = True;
    while changes == True:
        changes = False;
        for i in range( 0, len( A ) - 1 ):
            c.compares += 1
            if A[ i ] > A[ i + 1 ]:
                A[ i ], A[ i + 1 ] = A[ i + 1 ], A[ i ]
                changes = True
        for i in range(len(A) - 2, 0, -1):
            c.compares += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                changes = True
    return A

def CountingSort( A, c ):
    c.compares = len( A )
    B = [0] * len(A)
    for i in A:
        B[i]+=1
    k = 0
    for i in range(len(B)):
        v = i
        count = B[i]
        for j in range(count):
            A[k] = v
            k +=1
    return A

def MergeSort( A, c ):
    if len( A ) <= 1:
        return
    L = A[ 0:len(A)//2 ]
    R = A[ len(A)//2:len(A) ]
    MergeSort( L, c )
    MergeSort( R, c )
    i = j = k = 0
    while i < len( L ) and j < len( R ):
        c.compares += 1
        if L[ i ] <= R[ j ]:
            A[ k ] = L[ i ]
            k+=1
            i+=1
        else: 
            A[ k ] = R[ j ]
            k+=1 
            j+=1
    while i < len( L ):
        A[ k ] = L[ i ]
        k+=1
        i+=1 
    while j < len( R ):
        A[ k ] = R[ j ]
        k+=1
        j+=1

def QuickSortRecursive( A, c, low, high, mod ):
    if high - low <= 0:
        return
    if mod == True:
        mid = ( low + high ) // 2
        A[ low ], A[ mid ] = A[ mid ], A[ low ]
    lmgt = low + 1
    for i in range ( low + 1, high + 1 ):
        c.compares += 1
        if A[ i ] < A[ low ]:
            A[ i ], A[ lmgt ] = A[ lmgt ], A[ i ]
            lmgt+=1
    PivotIndex = lmgt - 1
    A[ low ], A[ PivotIndex ] = A[ PivotIndex ], A[ low ]
    QuickSortRecursive( A, c,  low, PivotIndex - 1, mod )
    QuickSortRecursive( A, c, PivotIndex +1, high, mod )

def QuickSort( A, c ):
    QuickSortRecursive( A, c, 0, len( A ) - 1, False )
    
def ModifiedQuickSort( A, c ):
    QuickSortRecursive( A, c, 0, len( A ) - 1, True )

def CreateRandomList( size ):
    A = []
    for i in range(size):
        r = random.randrange(0,size)
        A.append(r)
    return A

def CreateMostlySortedList( size ):
    A = []
    for i in range(size):
        r = random.randrange(0,size)
        A.append(r)
    A.sort()
    A[ 0 ], A[ len( A ) - 1 ] = A[ len( A ) - 1 ], A[ 0 ]
    return A

def main():
    sys.setrecursionlimit(5000)

    print("    Bubble   Shaker   Counting   Merge   Quick    MQuick")
    SortingAlgorithms = [BubbleSort, ShakerSort, CountingSort, MergeSort, QuickSort, ModifiedQuickSort ]
    for s in range(3, 13): # for each row
        size = 2 ** s
        print(s, end="\t")
        for sort in SortingAlgorithms:
            A = CreateRandomList(size)
            # A = CreateMostlySortedList(size)
            B = A[:]
            B.sort()
            c = Counter()
            sort(A, c)
            x = math.log(c.compares,2)
            print("%02.2f" % (x),end="\t")

            if A!=B:
                print("error")
        print()



main()
    