import student
import container
import time

def main():
    timeStart = time.time()
    bag = container.Container()
    fin = open( "FakeNames.txt")
    for line in fin:
        words = line.split()
        s = student.Student(words[0],words[1],words[2],words[3],words[4])
        if bag.Insert( s ) == False:
            print("Error. ", words[1], " not inserted. Duplicate.")
    timeEnd = time.time()
    print( "inserting time was, ", timeEnd - timeStart, " seconds." )
    fin.close()
main()
