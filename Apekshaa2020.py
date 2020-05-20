print(" __________________________________")
print("|         ~~~ APEKSHAA ~~~         |\n|        ~ TECHNICAL QUIZ ~        |\n|               2020               |\n|                                  |\n|                                  |\n|      THE DIGITAL SCOREBOARD      |\n|           PROGRAMMED BY          |\n|     ->  ~~ 'VIRINCHI' ~~  <-     |\n|             III-CSE              |")
print(" __________________________________")
start = input("\n\n\nLet's Start the quiz do we ?\n\n\n")

lst = [["R-2","A","B","C","D","E","F"],["Q1",0,0,0,0,0,0],["Q2",0,0,0,0,0,0],["Q3",0,0,0,0,0,0],["Q4",0,0,0,0,0,0]]
for i in lst:
    print("\t\t".join(str(x) for x in i))
print()
marksA=0
marksB=0
marksC=0
marksD=0
marksE=0
marksF=0

def r2(x,y,z):
    del lst[x][y]
    lst[x].insert(y, z)
    for i in lst:
        print("\t\t".join(str(x) for x in i))
    print()

#Round-2 Question-1
r2q1A = int(input("Enter marks for Team A Q1 : "))
r2(1,1, r2q1A)
marksA= marksA + r2q1A
r2q1B = int(input("Enter marks for Team B Q1 : "))
r2(1,2,r2q1B)
marksB= marksB + r2q1B
r2q1C = int(input("Enter marks for Team C Q1 : "))
r2(1,3,r2q1C)
marksC= marksC + r2q1C
r2q1D = int(input("Enter marks for Team D Q1 : "))
r2(1,4,r2q1D)
marksD= marksD + r2q1D
r2q1E = int(input("Enter marks for Team E Q1 : "))
r2(1,5,r2q1E)
marksE= marksE + r2q1E
r2q1F = int(input("Enter marks for Team F Q1 : "))
r2(1,6,r2q1F)
marksF= marksF + r2q1F

#Round-2 Question-2
r2q2A = int(input("Enter marks for Team A Q2 : "))
r2(2,1, r2q2A)
marksA= marksA + r2q2A
r2q2B = int(input("Enter marks for Team B Q2 : "))
r2(2,2,r2q2B)
marksB= marksB + r2q2B
r2q2C = int(input("Enter marks for Team C Q2 : "))
r2(2,3,r2q2C)
marksC= marksC + r2q2C
r2q2D = int(input("Enter marks for Team D Q2 : "))
r2(2,4,r2q2D)
marksD= marksD + r2q2D
r2q2E = int(input("Enter marks for Team E Q2 : "))
r2(2,5,r2q2E)
marksE= marksE + r2q2E
r2q2F = int(input("Enter marks for Team F Q2 : "))
r2(2,6,r2q2F)
marksF= marksF + r2q2F

#round-2 Question-3
r2q3A = int(input("Enter marks for Team A Q3 : "))
r2(3,1, r2q3A)
marksA= marksA + r2q3A
r2q3B = int(input("Enter marks for Team B Q3 : "))
r2(3,2,r2q3B)
marksB= marksB + r2q3B
r2q3C = int(input("Enter marks for Team C Q3 : "))
r2(3,3,r2q3C)
marksC= marksC + r2q3C
r2q3D = int(input("Enter marks for Team D Q3 : "))
r2(3,4,r2q3D)
marksD= marksD + r2q3D
r2q3E = int(input("Enter marks for Team E Q3 : "))
r2(3,5,r2q3E)
marksE= marksE + r2q3E
r2q3F = int(input("Enter marks for Team F Q3 : "))
r2(3,6,r2q3F)
marksF= marksF + r2q3F

#Round-2 Question-4
r2q4A = int(input("Enter marks for Team A Q4 : "))
r2(4,1, r2q4A)
marksA= marksA + r2q4A
r2q4B = int(input("Enter marks for Team B Q4 : "))
r2(4,2,r2q4B)
marksB= marksB + r2q4B
r2q4C = int(input("Enter marks for Team C Q4 : "))
r2(4,3,r2q4C)
marksC= marksC + r2q4C
r2q4D = int(input("Enter marks for Team D Q4 : "))
r2(4,4,r2q4D)
marksD= marksD + r2q4D
r2q4E = int(input("Enter marks for Team E Q4 : "))
r2(4,5,r2q4E)
marksE= marksE + r2q4E
r2q4F = int(input("Enter marks for Team F Q4 : "))
r2(4,6,r2q4F)
marksF= marksF + r2q4F

print("Toatl\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(marksA, marksB, marksC, marksD, marksE, marksF))

dict_teams1={
    lst[0][1]:marksA,
    lst[0][2]:marksB,
    lst[0][3]:marksC,
    lst[0][4]:marksD,
    lst[0][5]:marksE,
    lst[0][6]:marksF
}

elim_lst = []
elim_lst.append(input("Enter  First ELIMINATED Team : "))
elim_lst.append(input("Enter  Second ELIMINATED Team : "))
index1 = lst[0].index(elim_lst[0])
index2 = lst[0].index(elim_lst[1])-1
for i in range(5):
    del lst[i][index1]
    del lst[i][index2]
del dict_teams1[elim_lst[0]]
del dict_teams1[elim_lst[1]]
for i in lst:
    print("\t\t".join(str(x) for x in i))


lst2 = [["R-3"],["Q1",0,0,0,0],["Q2",0,0,0,0],["Q3",0,0,0,0],["Q4",0,0,0,0],["Q5",0,0,0,0],["Q6",0,0,0,0],["Q7",0,0,0,0],["Q8",0,0,0,0],["Q9",0,0,0,0],["Q10",0,0,0,0]]
for i in lst2:
    print("\t\t".join(str(x) for x in i))
def r3(x,y,z):
    del lst2[x][lst[0].index(y)]
    lst2[x].insert(lst[0].index(y), z)
    for i in lst:
        print("\t\t".join(str(x) for x in i))
    for i in lst2:
        print("\t\t".join(str(x) for x in i))

r3q1B = input("Who's first ? : ")
r3q1M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q1B)]]=dict_teams1[lst[0][lst[0].index(r3q1B)]]+r3q1M
r3(1,r3q1B,r3q1M)
r3q2B = input("Who's First ? : ")
r3q2M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q2B)]]=dict_teams1[lst[0][lst[0].index(r3q2B)]]+r3q2M
r3(2,r3q2B,r3q2M)
r3q3B = input("Who's First ? : ")
r3q3M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q3B)]]=dict_teams1[lst[0][lst[0].index(r3q3B)]]+r3q3M
r3(3,r3q3B,r3q3M)
r3q4B = input("Who's First ? : ")
r3q4M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q4B)]]=dict_teams1[lst[0][lst[0].index(r3q4B)]]+r3q4M
r3(4,r3q4B,r3q4M)
r3q5B = input("Who's First ? : ")
r3q5M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q5B)]]=dict_teams1[lst[0][lst[0].index(r3q5B)]]+r3q5M
r3(5,r3q5B,r3q5M)
r3q6B = input("Who's First ? : ")
r3q6M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q6B)]]=dict_teams1[lst[0][lst[0].index(r3q6B)]]+r3q6M
r3(6,r3q6B,r3q6M)
r3q7B = input("Who's First ? : ")
r3q7M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q7B)]]=dict_teams1[lst[0][lst[0].index(r3q7B)]]+r3q7M
r3(7,r3q7B,r3q7M)
r3q8B = input("Who's First ? : ")
r3q8M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q8B)]]=dict_teams1[lst[0][lst[0].index(r3q8B)]]+r3q8M
r3(8,r3q8B,r3q8M)
r3q9B = input("Who's First ? : ")
r3q9M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q9B)]]=dict_teams1[lst[0][lst[0].index(r3q9B)]]+r3q9M
r3(9,r3q9B,r3q9M)
r3q10B = input("Who's First ? : ")
r3q10M = int(input("Marks ? : "))
dict_teams1[lst[0][lst[0].index(r3q10B)]]=dict_teams1[lst[0][lst[0].index(r3q10B)]]+r3q10M
r3(10,r3q10B,r3q10M)
for i,j in dict_teams1.items():
    print("{} - {} ".format(i,j))

finalists =[]
finalists.append(input("Enter FIRST FINALIST."))
finalists.append(input("Enter SECOND FINALIST."))
eliminators =[i for i in lst[0] if i not in finalists]
del dict_teams1[eliminators[1]]
del dict_teams1[eliminators[2]]
print("Let's see who among TEAM-{} & TEAM-{} will complete the program in given time".format(finalists[0],finalists[1]))
print("Oh! By the way let's take the names of Team Members of both teams ...")
team1 = []
team2 = []
print("Enter names of Team - {}\n".format(finalists[0]))
for i in range(3):
    team1.append(input())
print("Enter names of Team - {}\n".format(finalists[1]))
for i in range(3):
    team2.append(input())
print("Done !")
print("Now let's see the marks...")
final1 = int(input("Enter  marks for Team-{} in Final Round: ".format(finalists[0])))
dict_teams1[lst[0][lst[0].index(finalists[0])]]=dict_teams1[lst[0][lst[0].index(finalists[0])]]+final1
final2 = int(input("Enter  marks for Team-{} in Final Round: ".format(finalists[1])))
dict_teams1[lst[0][lst[0].index(finalists[1])]]=dict_teams1[lst[0][lst[0].index(finalists[1])]]+final2
for i,j in dict_teams1.items():
    print("{} - {} ".format(i,j))
print("Time to declare the WINNER of 2020 APEKSHA's Technical Quiz . . .")
if dict_teams1[finalists[0]]>dict_teams1[finalists[1]]:
    print("Winner of Apekshaa's 2020 Technical Quiz . . . TEAM {} ".format(finalists[0]))
    print()
    print("Congratulations...TEAM {} ".format(finalists[0]))
    print("Winners . . .")
    for i in range(3):
        print(team1[i])
elif dict_teams1[finalists[0]]<dict_teams1[finalists[1]]:
    print("Winner of Apekshaa's 2020 Technical Quiz . . . TEAM {} ".format(finalists[1]))
    print("Congratulations...TEAM {} ".format(finalists[1]))
    print("Winners . . .")
    for i in range(3):
        print(team2[i])
elif dict_teams1[finalists[0]]==dict_teams1[finalists[1]]:
    print("Time for a Tie-Breaker Question.")
    tie_b = input("Quiz Master! Please ask a Tie-Breaker and announce the Winner . . . ")
    if tie_b==finalists[0]:
        print("Winner of Apekshaa's 2020 Technical Quiz . . . TEAM {} ".format(finalists[0]))
        print("Congratulations...TEAM {} ".format(finalists[0]))
        print("Winners . . .")
        for i in range(3):
            print(team2[i])
        input()
    elif tie_b==finalists[1]:
        print("Winner of Apekshaa's 2020 Technical Quiz . . . TEAM {} ".format(finalists[1]))
        print("Congratulations...TEAM {} ".format(finalists[1]))
        print("Winners . . .")
        for i in range(3):
            print(team2[i])
        input()
    else:
        print("Please Announce the WINNERS...")
else:
    print("Please Announce the WINNERS...")