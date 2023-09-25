import random
import time

def createRandomList():
    random_list = []
    for i in range( 50 ):
        random_list.append(i)
    random.shuffle( random_list )
    return random_list

def answerSyntax( num ):
    if num < 10 :
        return str(2 ** num)
    elif 10 <= num < 20 :
        secondDigit = str( num )[1]
        num = int( secondDigit )
        return str( 2 ** num ) + 'k'
    elif 20 <= num < 30:
        secondDigit = str( num )[1]
        num = int( secondDigit )
        return str( 2 ** num ) + 'm'
    elif 30 <= num < 40:
        secondDigit = str( num )[1]
        num = int( secondDigit )
        return str( 2 ** num ) + 'b'
    elif 40 <= num < 50:
        secondDigit = str( num )[1]
        num = int( secondDigit )
        return str( 2 ** num ) + 't'

def main():
    random_list = createRandomList()
    timeStart = time.time()
    for i in range( len( random_list ) ):
        prompt = "What is 2 ** %d? " %( random_list[ i ] )
        user_input = input( prompt )
        while user_input != answerSyntax( random_list[ i ] ):
            user_input = input( "Wrong! Try Again: ")
    timeEnd = time.time()

    print("")
    print( "Your total time was", round( timeEnd - timeStart, 2 ), "seconds.")

        

main()

        