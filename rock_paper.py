import random
a = ['rock' , 'paper' , 'scissors']


print("\nWelcome to the Rock Paper Scissors Game!\nHere you will compete with the computer")
print("\nChoose any [R]ock , [P]aper , [S]cissors")

name = input("\nPlease enter your name: ")

comp_point = 0;
user_point = 0;
i = 0

while i<5:
    user = input("\nYour Input: ")
    comp = a[random.randrange(0,2)]
    print("Comp input: ",comp,'\n')
    if comp == a[0] and user.lower() == 'r':
        print("Tie no points\n")
    if comp == a[0] and user.lower() == 'p':
        print(name," one point\n")
        user_point += 1
    if comp == a[0] and user.lower() == 's':
        print("Comp one point\n")
        comp_point += 1
    if comp == a[1] and user.lower() == 'r':
        print("Comp one point\n")
        comp_point += 1
    if comp == a[1] and user.lower() == 'p':
        print("Tie no points\n")
    if comp == a[1] and user.lower() == 's':
        print(name," one point\n")
        user_point += 1
    if comp == a[2] and user.lower() == 'r':
        print(name," one point\n")
        user_point += 1
    if comp == a[2] and user.lower() == 'p':
        print("Comp one point\n")
        comp_point += 1
    if comp == a[2] and user.lower() == 's':
        print("Tie no points\n")
    i += 1


print(name," points: ",user_point,"\nComp points: ",comp_point)
if user_point > comp_point:
    print("Whoaa! You win by ",user_point-comp_point," points!!!")
elif user_point == comp_point:
    print("Tie Match")
else:
    print("Comp wins by ",comp_point-user_point," points")
