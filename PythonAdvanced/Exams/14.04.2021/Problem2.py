def print_output(name, throws):
    print(f'{name} won the game with {throws} throws!')


players = input().split(', ')
dartboard = list()

for i in range(0, 7):
    current_row = input().split(' ')
    dartboard.append(current_row)

first_player_points = 501
second_player_points = 501
index = 1
first_player_throws = 0
second_player_throws = 0

while True:
    current_player = ""
    is_first_player = True
    if index % 2 == 0:
        current_player = players[1]
        is_first_player = False
        second_player_throws += 1
    else:
        current_player = players[0]
        first_player_throws += 1
    throw_data = input()[1:-1].split(', ')
    row = int(throw_data[0])
    col = int(throw_data[1])
    index += 1

    try:
        target = dartboard[row][col]
        points = 0
        if target == "D":
            points = 2 * (int(dartboard[0][col]) +
                          int(dartboard[row][0]) +
                          int(dartboard[row][len(dartboard) - 1]) +
                          int(dartboard[len(dartboard) - 1][col]))
        elif target == "T":
            points = 3 * (int(dartboard[0][col]) +
                          int(dartboard[row][0]) +
                          int(dartboard[row][len(dartboard) - 1]) +
                          int(dartboard[len(dartboard) - 1][col]))
        elif target == "B":
            if is_first_player:
                print_output(current_player, first_player_throws)
            else:
                print_output(current_player, second_player_throws)
            break
        else:
            points = int(dartboard[row][col])

        if is_first_player:
            first_player_points -= points
            if first_player_points <= 0:
                print_output(current_player, first_player_throws)
                break
        else:
            second_player_points -= points
            if second_player_points <= 0:
                print_output(current_player, second_player_throws)
                break

    except IndexError:
        continue
