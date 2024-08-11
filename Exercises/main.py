import random

entrys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = []
for i in range(1,4):
    choice = random.choice(entrys)
    my_ticket.append(choice)
print(f'My ticket is {my_ticket}.')

winners = []
for i in range(1,6):
    winner = random.choice(entrys)
    entrys.remove(winner)
    winners.append(winner)

print(f'The winners of this lottery are {winners}.')

win_count = 0
for i in my_ticket:
    if i not in winners:
        print('I did not win the lottery.')
        break
    else:
        win_count += 1
        if win_count == 3:
            print("I won the lottery!")
            break