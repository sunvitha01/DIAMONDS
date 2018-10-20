import random
import getpass
def distribution_of_cards(suits,ranks):
	pack = []
	for r in ranks:
		pack.append(suits + " - " + r)
	return pack
 
def selection_of_suit(selected):
	if selected in suits:
		suits.remove(selected)
	return distribution_of_cards(selected,ranks)
 
def to_convert_into_inttype(num):
	if num == 'A':
		return 1
	elif num == 'J':
		return 11
	elif num == 'Q':
		return 12
	elif num == 'K':
		return 13
	else:
		return int(num)

def random_selection(list):
	num = random.choice(list)
	list.remove(num)
	return num
 
def distribution_of_diamond_for_2_players(computer_num,player_num,diamond_num):
	if computer_num == player_num:
		diamonds_of_computer.append(diamond_num / 2)
		diamonds_of_player.append(diamond_num / 2)
		return ("Diamond is equally divided")
	elif player_num > computer_num :
		diamonds_of_player.append(diamond_num)
		return ("Diamond goes to player")
	else :
		diamonds_of_computer.append(diamond_num)
		return ("Diamond goes to computer")

def declaring_winner_for_2_players(diamonds_of_player,diamonds_of_computer):
	total_diamonds_of_player = sum(diamonds_of_player)
	total_diamonds_of_computer = sum(diamonds_of_computer)
	if total_diamonds_of_player > total_diamonds_of_computer:
		return ("Total number of diamonds = ", total_diamonds_of_player,"winner is player")
	elif total_diamonds_of_player < total_diamonds_of_computer:
		return ("Total number of diamonds = ", total_diamonds_of_computer,"Winner is computer")
	else :
		return ("Total number of diamonds = ", total_diamonds_of_computer,"draw")

def distribution_of_diamond_for_3_players(computer_num, player1_num, player2_num, diamond_num):
	maxm = max(computer_num, player1_num, player2_num, diamond_num)
	if computer_num == player1_num and player1_num == player2_num:
		diamonds_of_computer.append(diamond_num / 3)
		diamonds_of_player1.append(diamond_num / 3)
		diamonds_of_player2.append(diamond_num / 3)
		return ("Diamond is equally divided among 3")
	elif computer_num == player1_num:
		diamonds_of_computer.append(diamond_num / 2);
		diamonds_of_player1.append(diamond_num / 2);
		return ("Diamond is equally divided between computer and player1")
	elif computer_num == player2_num:
		diamonds_of_computer.append(diamond_num / 2);
		diamonds_of_player2.append(diamond_num / 2);
		return ("Diamond is equally divided between computer and player2")
	elif player1_num == player2_num:
		diamonds_of_player2.append(diamond_num / 2);
		diamonds_of_player1.append(diamond_num / 2);
		return ("Diamond is equally divided between player1 and player2")
	elif maxm == computer_num:
		diamonds_of_computer.append(diamond_num)
		return ("Diamond goes to computer")
	elif maxm == player1_num:
		diamonds_of_player1.append(diamond_num)
		return ("Diamond goes to player1")
	else:
		diamonds_of_player2.append(diamond_num)
		return ("Diamond goes to player2")

def declaring_winner_for_3_players(diamonds_of_player1,diamonds_of_player2,diamonds_of_computer):
	total_diamonds_of_player1 = sum(diamonds_of_player1)
	total_diamonds_of_player2 = sum(diamonds_of_player2)
	total_diamonds_of_computer = sum(diamonds_of_computer)
	maxm = max(total_diamonds_of_player1,total_diamonds_of_player2,total_diamonds_of_computer)
	if (total_diamonds_of_player1 == total_diamonds_of_player2) and (total_diamonds_of_player2 == total_diamonds_of_computer):
		return ("Total number of diamonds = ", total_diamonds_of_computer,"draw")
	elif (maxm == total_diamonds_of_computer) and (maxm == total_diamonds_of_player1):
		return ("Total number of diamonds = ", total_diamonds_of_computer,"draw between player1 and computer")
	elif (maxm == total_diamonds_of_computer) and (maxm == total_diamonds_of_player2):
		return ("Total number of diamonds = ", total_diamonds_of_computer,"draw between player2 and computer")
	elif (maxm == total_diamonds_of_player1) and (maxm == total_diamonds_of_player2):
		return ("Total number of diamonds = ", total_diamonds_of_player1,"draw between player1 and player2")
	elif maxm == total_diamonds_of_computer:
		return ("Total number of diamonds = ", total_diamonds_of_computer,"Winner is computer")
	elif maxm == total_diamonds_of_player1:
		return ("Total number of diamonds = ", total_diamonds_of_player1,"Winner is player1")
	else:
		return ("Total number of diamonds = ", total_diamonds_of_player2,"Winner is player2")

print(" ")
ranks = ['A', '2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K']
suits = ['C', 'H', 'S','D']
n = (input("Enter number of players : "))
diamond_card = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
computer = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
print("Enter the values in between 1-13\nA=1 J=11 Q=12 K=13")
i = 0


if n == 2:
	diamonds_of_computer = []
	diamonds_of_player = []
	selected = (input("Choose the type of suit : "))
	print(selection_of_suit(selected))
	print(" ")
	print("chosen by computer - ",selection_of_suit(random.choice(suits)))
	print(" ")
	while i < 13:
		diamonds = (random_selection(diamond_card))
		print("Diamond card : ",diamonds); 
		diamond_num = to_convert_into_inttype(diamonds)
		computer_player = random_selection(computer)
		player = getpass.getpass("Enter the selected card : ")
		computer_num = to_convert_into_inttype(computer_player)
		player_num = to_convert_into_inttype(player)
		print(distribution_of_diamond_for_2_Players(computer_num, player_num, diamond_num))
		print(" ")
		i += 1

	print(declaring_winner_for_2_players(diamonds_of_player,diamonds_of_computer))



if n == 3:
	diamonds_of_computer = []
	diamonds_of_player1 = []
	diamonds_of_player2 = []
	player1 = input("Choose the type of suit by player1 : ")
	player2 = input("Choose the type of suit by player2 : ")
	print(selection_of_suit(player1))
	print(" ")
	print(selection_of_suit(player2))
	print(" ")
	print("chosen by computer - ",selection_of_suit(random.choice(suits)))
	print(" ")
	while i < 13:
		diamonds = (random_selection(diamond_card))
		print "Diamond card : ",diamonds; 
		diamond_num = to_convert_into_inttype(diamonds)
		computer_player = random_selection(computer)
		player1 = getpass.getpass("Enter the card player 1 : ")
		player2 = getpass.getpass("Enter the card player 2 : ")
		computer_num = to_convert_into_inttype(computer_player)
		player1_num = to_convert_into_inttype(player1)
		player2_num = to_convert_into_inttype(player2)
		print(distribution_of_diamond_for_3_players(computer_num, player1_num, player2_num, diamond_num))
		print(" ")
		i += 1

	print(declaring_winner_for_3_players(diamonds_of_player1,diamonds_of_player2,diamonds_of_computer))

