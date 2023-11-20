import student
import container
import time

def main():

    #Insert
    timeStart = time.time()
    bag = container.Container( 300000 )
    fin = open( "FakeNamesMedium.txt")

    fails = 0 
    for line in fin:
        words = line.split()
        s = student.Student(words[0],words[1],words[2],words[3],words[4])
        if bag.Insert( s ) == False:
            # print("Error. ", words[1], " not inserted. Duplicate.")
            fails += 1
    print( fails )
    timeEnd = time.time()
    print( "Insert time was, ", timeEnd - timeStart, " seconds." )
    print( "" )
    fin.close()

    #Traverse
    timeStart = time.time()
    totalAge = 0 
    for item in bag:
        totalAge += int( item.mAge )
    timeEnd = time.time()
    print("Average age: ", totalAge / bag.Size())
    print("Traverse time was, ", timeEnd-timeStart, " seconds.")
    print( "" )

    #Delete
    timeStart = time.time()
    fin = open("DeleteNamesMedium.txt")
    fails = 0
    for line in fin:
        ssn = line.strip()
        s2 = student.Student( "", "", ssn, "", "" )
        if bag.Delete( s2 ) == False:
            # print( "Error Deleting. SSN: ", ssn, "Not Found" )
            fails +=1
    print( fails )
    timeEnd = time.time()

    print( "Delete time was, ", timeEnd - timeStart, " seconds." )
    print( "" )
    fin.close()

    #Retrieve
    timeStart = time.time()
    totalAge = 0
    retrievedStudents = []
    fin = open("RetrieveNamesMedium.txt")
    fails = 0
    for line in fin:
        ssn = line.strip()
        s2 = student.Student( "", "", ssn, "", "" )
        s3 = bag.Retrieve( s2 )
        if bag.Retrieve( s2 ):
            totalAge += int( s3.mAge )
            retrievedStudents.append( s3 )
        else:
            # print( "Error Retrieving. SSN: ", ssn, "Not Found" )
            fails += 1
    print( fails )
    print( "Average age: ", totalAge / len(retrievedStudents) )
    timeEnd = time.time()
    print( "Retrieve time was, ", timeEnd - timeStart, " seconds." )
    fin.close()


main()
