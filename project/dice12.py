import random 
 
attempt=4
flag=0
dice1=random.randint(1,6)
dice2=random.randint(1,6)


while(attempt!=0):
      num=int(input("Enter total number of both the dice: "))
      if((dice1+dice2)==num):
            flag=1
            print("you win!!! The number is: ",dice1+dice2)
            break
      else:
            print("You are wrong... lose your chance")
            attempt-=1

if flag==0:
    print("you lose, the number was: ",dice1+dice2)
