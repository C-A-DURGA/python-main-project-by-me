""""
1=stone
2=paper
3=scissor

"""

import random 
computer= random.choice([1,2,3])
youStr =(input(" Enter your choice\n s for stone \n p for paper \n ss for scissor:\t"))
youDict={"s":1,"p":2,"ss":3}
reverseDict={1:"Stone",2:"paper",3:"Scissor"}

you=youDict[youStr]

print(f"You chose {reverseDict[you]},Computer chose {reverseDict[computer]}")
if (computer==you):
    print ("It's a draw")
else:
    if(computer==1 and you==2):
        print("You won")
    elif(computer==2 and you==1):
        print("Computer won")
    elif(computer==3 and you==2):
        print("Computer won")
    elif(computer==2 and you==3):
        print("You won")
    elif(computer==1 and you ==3):
        print("Computer won")
    elif(computer==3 and you==1):
        print("You won")
