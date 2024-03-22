First :
Use function to check if 3 numbers in a list of any of the two players their sum equals 15 
Or no 
By defining winCheck(list)
And use nested loop :
For I in range (I+1 , len(list))
 For K in range (K+1 , len(list))
 For J in range (J+1 , len(list))
 If list [I] +list [K] +list[J] equals 15 or not 
Display numbers =[1,2,3,4,5,6,7,8,9] which are available in our game
make a list for player_1 to put the chosen numbers in it 
make a list for player_2 to put the chosen numbers in it
while True:
 Display the turn for the (First_player_turn)
 Use function (len(numbers) == 0) 
 To Check there is any number in [numbers] or no as if there is no any number and in [numbers]
 And no one won , the program display (“draw”) then break
 If there is any number in [numbers]
 (Display / print) a message that ask the user to enter a number from [numbers]
 The (First_player) will choose a number that will be added to [player_1] and removed from[numbers]
 I used (try and except function in while loop ) in this program to prevent the player from choosing a 
 Letter or a symbol Which is not included in [numbers] and use if condition to prevent the player from 
 Choosing number not included in [numbers] ] by printing a message that ask the player to re_enter a 
 Number by giving him a chance to re-enter a number from [Numbers] if the choice is correct 
 From the beginning or the player re-enter a number in [numbers] then Break 
 Use function winCheck and len(player_1) >=3 to check that the sum of 3 numbers from the chosen 
 Equals 15 or not and the number of element in [player_1]>=3 to prevent the case of the sum of only 
 Two Numbers = 15 and if True (print/display) “First_player wins” then break
 Display the turn for the (Second_player_turn)
 Use function (len(numbers) == 0) 
 To Check there is any number in [numbers] or no as if there is no any number and in [numbers]
 And no one won , the program display (“draw”) then break
 If there is any number in [numbers]
 (Display / print) a message that ask the user to enter a number from [numbers]
 The (Second_player) will choose a number that will be added to [player_1] and removed from 
 [numbers]
 I used (try and except function in while loop ) in this program to prevent the player from choosing a 
 Letter or a symbol Which is not included in [numbers] and use if condition to prevent the player from 
 Choosing number not included in [numbers] by printing a message that ask the player to re_enter a 
 Number by giving him a chance to re-enter a number from [Numbers] if the choice is correct from 
 Beginning or he re_enter a number in [numbers] then break 
 Use function winCheck and len(player_2) >=3 to check that the sum of 3 numbers from the chosen 
 Equals 15 or not and the number of element in [player_2]>=3 to prevent the case of the sum of only 
 Two Numbers = 15 and if True (print/dissplay) “Second_player wins” then break
