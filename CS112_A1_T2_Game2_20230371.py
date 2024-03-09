# File: CS112_A1_T2_2_20230371.py
# purpose: the description of the (Number scrabble) game is that the two
#  players will play against each other in collecting agroup of numbers with condition to give the two players chance to re-enter a number 
#  from the list of the available numbers even if nagative number
#  or zero or letter and the player who collects atleast three numbers their sum equals 15 or more than
#  three numbers but the sum of any three numbers of them equals 15
# Author:Mahmoud khairy morsy 
# ID:20230371


# Function to check if 3 numbers in the list sum to 15
def winCheck(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            for k in range(j + 1, len(list)):
                if list[i] + list[j] + list[k] == 15:
                    return True
    return False
# list of available numbers
numbers=[1,2,3,4,5,6,7,8,9]
player_1=[]
player_2=[]
# Display the avilable numbers for the players
print ("available numbers",numbers)
while True:
#  display the turn for the first player
    print("first_player_turn")
# check the presence of available numbers or not as if there is no more [numbers] in the list and no one won , it will be drew
    if ((len(numbers)) == 0 ):
        print("drew")
        break
# let the first player to choose number from [numbers] and prevent the user the chance if he enters a wrong number or letter
    while True:
      try:
        choice=int(input("choose number from numbers "))
# if the choice not in [numbers] print the following message for the first player
        if (choice not in numbers):
            print(" choice is incorrect please enter  number from ",numbers)
        else:
            break
      except ValueError:
            print("wrong choice , please enter an integer number from ", numbers)
# if the choice is in [numbers] , add the choice to [player_1] , then display the taken numbers by the first_player in [player_1] and remove it from [numbers] and then display the rest available numbers in [numbers]
    player_1.append(choice)
    print("first_player= ", player_1)
    numbers.remove(choice)
    print(numbers)
#check if the sum of the of only three numbers taken by the user equal 15
    if winCheck(player_1) and len(player_1) >= 3:
        print("first_player wins")
        break
# Display the turn for the second player 
    print("second_player_turn")
# check the presence of available numbers or not as if there is no more [numbers] in the list and no one won , it will be drew
    if ((len(numbers)) == 0 ):
        print("drew")
        break
# let the second player to choose number from [numbers] and prevent the user the chance if he enters a wrong number or letter
    while True:
      try:    
        choice2=int(input("choose number from numbers "))
# if the choice not in [numbers] print the following message for the first player
        if(choice2 not in numbers ):
            print("choice2 is incorrect please enter number from ",numbers)
        else:
            break
      except ValueError:
          print("wrong choice , please enter an integer number from ", numbers)
 #if the choice is in [numbers] add the choice to [player_1] , then display the taken numbers by the second_player in [player_2] and remove it from [numbers] and then display the rest available numbers in [numbers]
    player_2.append(choice2)
    print("second_player" , player_2)
    numbers.remove(choice2)
    print(numbers)
    if winCheck(player_2) and len(player_2) >=3 :
        print("second player wins")
        break
