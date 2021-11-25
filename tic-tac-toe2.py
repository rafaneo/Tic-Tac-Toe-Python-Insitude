from array import *
import time
from random import randrange

matrix = [1,2,3],[4,5,6],[7,8,9]
matrix2 = [1,2,3],[4,5,6],[7,8,9]
blist = []
alist = []
count = 0

#####################################################
def tabledes():
    for i in range(3):
        print("+--------+--------+--------+")
        print("|        |        |        |")

        for j in range(len(matrix[i])):
            print("|   ", matrix[i][j], "    ", sep="", end='')
            if (matrix[i][j] == 3 or matrix[i][j] == 6 or matrix[i][j] == 9):
                print(end="|")
        print()
        print("|        |        |        |")

    print("+--------+--------+--------+")


def userinput():
    print("Your Turn")
    a = int(input())
    if a>10 or a <0:
        print("Invalid placement try again")
        userinput()

    alist.append(a)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == a):
                alist.append(a)
                matrix[i][j] = "o"
            elif (matrix2[i][j]==  a and matrix[i][j]=='x'): #Use the seccond table as a refference to the first one, if it exists in the seccond table but not the first then you cant place it there
                print(matrix[i][j])
                print("There is an X there try again")
                userinput()
def computerinput():
    #This code is supposed to take a random value from the computer check if it 1) Has been given by the user , 2) if it was already given by the computer , 3) If it exists in the list
    seen = []
    bnotin = []
    count = 0

    b = randrange(1, 10)
    #####Exclude all numbers given by the user######
    while (b in alist):
        b = randrange(1, 10)
    blist.append(b)

    for i in range(3):
        for j in range(3):
            if (b == matrix[i][j]):
                matrix[i][j] = "x"
                return
            else:
                count+=1
            if count == 9:
                computerinput()

def findwinner():
    #################################################
    #######Player Check #########################
    #######Fix priority #############

    ccount1 = 0
    ccount2 = 0
    ccount3 = 0
    for i in range(3):
        for j in range(3):
            if (matrix[i] == 'o'):
                ccount1 += 1
            if (matrix[i][1] == 'o'):
                ccount2 += 1
            if (matrix[i][2] == 'o'):
                ccount3 += 1
    if ccount1 == 9:
        print("Winner is o with a win in collumn 1")
        gtrue = True
        exit()
    elif ccount2 == 9:
        print("Winner is o with a win in collumn 2")
        gtrue = True
        exit()
    elif ccount3 == 9:
        print("Winner is o with a win in collumn 3")
        gtrue = True
        exit()

    rcount1 = 0
    rcount2 = 0
    rcount3 = 0
    for i in range(3):
        for j in range(3):
            if (matrix[0][j] == 'o'):
                rcount1 += 1
            if (matrix[1][j] == 'o'):
                rcount2 += 1
            if (matrix[2][j] == 'o'):
                rcount3 += 1
    if rcount1 == 9:
        print("Winner is o with a win in row 1")
        gtrue = True
        time.sleep(2)
        exit()
    elif rcount2 == 9:
        print("Winner is o with a win in row 2")
        time.sleep(2)
        gtrue = True
        exit()
    elif rcount3 == 9:
        print("Winner is o with a win in row 3")
        time.sleep(2)
        gtrue = True
        exit()

##############Computer Check####################
    cd1 = []
    cd2 = []
    gtrue = False
    for i in range(3):
        for j in range(3):
            if(i == j ):
                cd1.append(matrix[i][j])
            elif( i + j == 2):
                cd2.append(matrix[i][j])

    if cd1.count("x") == len(cd1): #Count finds the same elements in a list , if the count of same elements are the same as the length then d1 is a winner
        print("Winer is X with a diagonal win from left to right")
        time.sleep(2)
        gtrue = True
        exit()

    if cd2.count("x") ==len(cd2):
        print("Winer is X with a diagonal win from right to left ")
        time.sleep(2)
        gtrue = True
        exit()
        #Delete tables so they can be re-assigned
    del(cd1)
    del(cd2)

    ccount1 = 0
    ccount2 = 0
    ccount3 = 0
    for i in range(3):
        for j in range(3):
            if(matrix[i]=='x' ):
                ccount1+=1
            if(matrix[i][1] == 'x'):
                ccount2+=1
            if (matrix[i][2] == 'x'):
                ccount3+=1
    if ccount1==9 :
        print("Winner is X with a win in collumn 1")
        time.sleep(2)
        gtrue = True
        exit()
    elif ccount2 ==9:
        print("Winner is X with a win in collumn 2")
        time.sleep(2)
        gtrue = True
        exit()
    elif ccount3 == 9:
        print("Winner is X with a win in collumn 3")
        time.sleep(2)
        gtrue = True
        exit()


    rcount1 = 0
    rcount2 = 0
    rcount3 = 0
    for i in range(3):
        for j in range(3):
            if(matrix[0][j]=='x' ):
                rcount1+=1
            if(matrix[1][j] == 'x'):
                rcount2+=1
            if (matrix[2][j] == 'x'):
                rcount3+=1
    if rcount1 == 9:
        print("Winner is X with a win in row 1")
        time.sleep(2)
        gtrue = True
        exit()
    elif rcount2 == 9:
        print("Winner is X with a win in row 1")
        time.sleep(2)
        gtrue = True
        exit()
    elif rcount3 == 9:
        print("Winner is X with a win in row 1")
        time.sleep(2)
        gtrue = True
        exit()

    tie1 = 0
    tie2 = 0
    for i in range(3):
        for j in range(3):
            if (matrix[i][j] == 'o'):
                tie1 += 1
            if (matrix[i][j] == 'x'):
                tie2 += 1
    if (tie1 == 4 and tie2 == 5 and gtrue == False ):
        print("The game has come to a tie")
        exit()


##################################################
print("This is the table , it is numbered from 1-9 when your turn comes choose a number to place the latter O at")
tabledes()
print("The Computer starts first")
matrix[1][1]= "x"
val = True
while(val):
    tabledes()
    userinput()
    tabledes()
    print("Computers's turn")
    computerinput()
    findwinner()


