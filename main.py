import random
from amperka_pico_lcd_1n14in import lcd_1n14in


def draw_edge(in_lcd):
    in_lcd.hline(10, 10, 220, in_lcd.blue)
    in_lcd.hline(10, 125, 220, in_lcd.blue)
    in_lcd.vline(10, 10, 115, in_lcd.blue)
    in_lcd.vline(230, 10, 115, in_lcd.blue)
    in_lcd.show()


def draw_edge_ttt(in_lcd):
    in_lcd.hline(10, 10, 220, in_lcd.blue)
    in_lcd.hline(10, 125, 220, in_lcd.blue)
    in_lcd.vline(10, 10, 115, in_lcd.blue)
    in_lcd.vline(230, 10, 115, in_lcd.blue)
    # field
    in_lcd.hline(90, 45, 60, in_lcd.green)
    in_lcd.hline(90, 65, 60, in_lcd.green)
    in_lcd.hline(90, 85, 60, in_lcd.green)
    in_lcd.hline(90, 105, 60, in_lcd.green)
    in_lcd.vline(90, 45, 60, in_lcd.green)
    in_lcd.vline(110, 45, 60, in_lcd.green)
    in_lcd.vline(130, 45, 60, in_lcd.green)
    in_lcd.vline(150, 45, 60, in_lcd.green)
    in_lcd.show()


def draw_menu(in_lcd, in_menu, in_menu_position):
    in_lcd.fill(in_lcd.white)
    draw_edge(in_lcd)
    in_lcd.text("Choose a game", 60, 20, in_lcd.blue)
    y = 30
    count_number = 1
    for element_menu in in_menu:
        prefix = '  '
        if count_number == in_menu_position:
            prefix = '* '
        in_lcd.text(prefix + element_menu, 60, y + count_number * 20, in_lcd.red)
        count_number = count_number + 1
    in_lcd.show()


def draw_snake_menu(in_lcd, user_points=0, in_game_over=False):
    in_lcd.fill(in_lcd.white)
    draw_edge(in_lcd)
    in_lcd.text("SNAKE", 100, 20, in_lcd.blue)
    in_lcd.text("Press KEY0 for start", 40, 60, in_lcd.red)
    if in_game_over:
        in_lcd.text("GAME OVER", 80, 80, in_lcd.red)
        in_lcd.text("SCORE " + str(user_points), 90, 100, in_lcd.green)
    in_lcd.show()
    return 1


def game_snake(in_lcd, position_x, position_y, user_points, position_food_x, position_food_y):
    in_lcd.fill(in_lcd.white)
    draw_edge(in_lcd)
    in_lcd.text("@", position_y, position_x, in_lcd.red)
    if position_food_x > 0 and position_food_y > 0:
        in_lcd.text("*", position_food_y, position_food_x, in_lcd.blue)
    in_lcd.text("points " + str(user_points), 5, 1, in_lcd.green)
    in_lcd.show()
    return 2


def draw_bc_menu(in_lcd, in_game_over=False):
    in_lcd.fill(in_lcd.white)
    draw_edge(in_lcd)
    in_lcd.text("Bulls & Cows", 80, 20, in_lcd.blue)
    in_lcd.text("Press KEY0 for start", 40, 60, in_lcd.red)
    if in_game_over:
        in_lcd.text("You win!!1", 80, 100, in_lcd.green)
    in_lcd.show()
    return 1


def game_bc(in_lcd, users_numbers, in_position, in_bulls=0, in_cows=0):
    in_lcd.fill(in_lcd.white)
    draw_edge(in_lcd)
    in_lcd.text("Press KEY3 for checking", 30, 20, in_lcd.green)
    in_lcd.text("you numbers", 70, 30, in_lcd.green)
    count_numbers = 1
    y = 20
    for u_element in users_numbers:
        if u_element == -1:
            in_lcd.text(" ", 70 + y * count_numbers, 40, in_lcd.blue)
        else:
            in_lcd.text(str(u_element), 70 + y * count_numbers, 60)
        count_numbers = count_numbers + 1
    in_lcd.text("^", 70 + y * in_position, 80, in_lcd.red)
    in_lcd.text("bulls " + str(in_bulls) + " & cows " + str(in_cows), 60, 100, in_lcd.green)
    in_lcd.show()
    return 2


def draw_ttt_menu(in_lcd, in_player_win=0):
    in_lcd.fill(in_lcd.white)
    draw_edge(in_lcd)
    in_lcd.text("Tic-Tac-Toe", 80, 20, in_lcd.blue)
    in_lcd.text("Press KEY0 for start", 40, 60, in_lcd.red)
    if in_player_win == 1:
        in_lcd.text("WIN x", 100, 100, in_lcd.green)
    elif in_player_win == 2:
        in_lcd.text("WIN o", 100, 100, in_lcd.green)
    elif in_player_win == 3:
        in_lcd.text("DRAW", 100, 100, in_lcd.green)
    in_lcd.show()
    return 1


def game_ttt(in_lcd, in_field, in_current_player, field_position):
    in_lcd.fill(in_lcd.white)
    draw_edge_ttt(in_lcd)
    player = ""
    if in_current_player == 1:
        player = "x"
    elif in_current_player == 2:
        player = "o"
    in_lcd.text("Player " + player, 90, 20, in_lcd.blue)
    position_y = 50
    step_y = 0
    position_x = 95
    step_x = 0
    for current_element in range(9):
        if current_element == 3 or current_element == 6:
            step_y = step_y + 1
            step_x = 0
        if current_element == field_position:
            in_lcd.text(player, position_x + step_x * 20, position_y + step_y * 20, in_lcd.blue)
        else:
            in_lcd.text(in_field[current_element], position_x + step_x * 20, position_y + step_y * 20, in_lcd.green)
        step_x = step_x + 1
    in_lcd.show()
    return 2


def comp_num_create():
    nums = []
    k = random.randint(1, 9)
    nums.append(k)
    for current_position in range(3):
        not_found_num = True
        while not_found_num:
            k = random.randint(0, 9)
            if k is not nums:
                nums.append(k)
                not_found_num = False
    return nums


def next_free_field(game_field, field_position):
    free_field = -1
    for current_element in range(field_position, 9):
        if game_field[current_element] == "*":
            free_field = current_element
            break
    if free_field == -1:
        for current_element in range(0, field_position - 1):
            if game_field[current_element] == "*":
                free_field = current_element
                break
    return free_field


def check_winner(game_field, player):
    player_logo = ""
    if player == 1:
        player_logo = "x"
    elif player == 2:
        player_logo = "o"
    if game_field[0] == player_logo and game_field[1] == player_logo and game_field[2] == player_logo:
        return player
    elif game_field[3] == player_logo and game_field[4] == player_logo and game_field[5] == player_logo:
        return player
    elif game_field[6] == player_logo and game_field[7] == player_logo and game_field[8] == player_logo:
        return player
    elif game_field[0] == player_logo and game_field[3] == player_logo and game_field[6] == player_logo:
        return player
    elif game_field[1] == player_logo and game_field[4] == player_logo and game_field[7] == player_logo:
        return player
    elif game_field[2] == player_logo and game_field[5] == player_logo and game_field[8] == player_logo:
        return player
    elif game_field[0] == player_logo and game_field[4] == player_logo and game_field[8] == player_logo:
        return count
    elif game_field[2] == player_logo and game_field[4] == player_logo and game_field[6] == player_logo:
        return player
    return 0


lcd = lcd_1n14in.LCD_1n14in()
lcd.set_brightness(32768)
lcd.fill(lcd.white)
lcd.show()

random.seed()

menu_position = 1
in_game = 0
game_start = 0
# snake game vars
pos_x = 40
pos_y = 60
points = 0
create_food = True
pos_food_x = 0
pos_food_y = 0
direction = 2
# bulls & cows game vars
c_nums = [0, 0, 0, 0]
u_nums = [0, 0, 0, 0]
position = 1
bulls = 0
cows = 0
# tic-tac-toe game vars
field = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
current_player = 1
field_pos = 0

menu = ['Snake', 'Bulls & Cows', 'Tic-Tac-Toe']

draw_edge(lcd)
draw_menu(lcd, menu, menu_position)

while True:

    redraw = False

    # SNAKE
    if in_game == 1:

        # main menu
        if game_start == 0:
            game_start = draw_snake_menu(lcd)
        # start game from main menu
        elif game_start == 1:
            if not lcd.key0.value():
                game_start = game_snake(lcd, pos_x, pos_y, points, pos_food_x, pos_food_y)
        # game logic
        elif game_start == 2:

            # direction
            if not lcd.key3.value():
                direction = direction + 1
                if direction > 4:
                    direction = 1

            if not lcd.key1.value():
                direction = direction - 1
                if direction < 1:
                    direction = 4

            # move to direction
            if direction == 2:
                pos_y = pos_y + 10
            elif direction == 1:
                pos_x = pos_x - 10
            elif direction == 3:
                pos_x = pos_x + 10
            elif direction == 4:
                pos_y = pos_y - 10

            # check edges
            game_over = False
            if pos_y > 230 or pos_y < 10:
                game_over = True
            elif pos_x > 120 or pos_x < 10:
                game_over = True

            # food logic
            if pos_x == pos_food_x and pos_y == pos_food_y:
                create_food = True
                points = points + 10

            if create_food:
                pos_food_x = round(random.randint(20, 110), -1)
                pos_food_y = round(random.randint(20, 220), -1)
                create_food = False

            # update screen
            if not game_over:
                game_start = game_snake(lcd, pos_x, pos_y, points, pos_food_x, pos_food_y)
            else:
                # snake game vars reset
                game_start = draw_snake_menu(lcd, points, game_over)
                pos_x = 40
                pos_y = 60
                points = 0
                create_food = True
                pos_food_x = 0
                pos_food_y = 0
                direction = 2

    elif in_game == 2:

        if game_start == 0:
            game_start = draw_bc_menu(lcd)

        # start game from main menu
        elif game_start == 1:
            if not lcd.key0.value():
                c_nums = comp_num_create()
                game_start = game_bc(lcd, u_nums, position)

        elif game_start == 2:

            update_lcd = False
            game_over = False

            if not lcd.key1.value():
                position = position + 1
                update_lcd = True
            if position > 4:
                position = 1

            if not lcd.key0.value():
                user_num = u_nums[position - 1]
                user_num = user_num + 1
                if user_num > 9:
                    user_num = 0
                u_nums[position - 1] = user_num
                update_lcd = True

            if not lcd.key3.value():
                bulls = 0
                cows = 0
                count = 0
                for element in u_nums:
                    if element == c_nums[count]:
                        bulls = bulls + 1
                    count = count + 1
                for i in range(4):
                    for j in range(4):
                        if i == j:
                            continue
                        if u_nums[i] == c_nums[j]:
                            cows = cows + 1
                if bulls == 4 and cows == 0:
                    game_over = True
                update_lcd = True

            # update
            if update_lcd:
                if game_over:
                    game_start = draw_bc_menu(lcd, game_over)
                    c_nums = [0, 0, 0, 0]
                    u_nums = [0, 0, 0, 0]
                    position = 1
                    bulls = 0
                    cows = 0
                else:
                    game_start = game_bc(lcd, u_nums, position, bulls, cows)

    elif in_game == 3:

        if game_start == 0:
            game_start = draw_ttt_menu(lcd)

        # start game from main menu
        elif game_start == 1:
            if not lcd.key0.value():
                game_start = game_ttt(lcd, field, current_player, field_pos)

        elif game_start == 2:

            update_lcd = False
            player_win = 0
            game_end = False

            if not lcd.key3.value():
                # field_pos = field_pos + 1
                # if field_pos > 8:
                #    field_pos = 0
                field_pos = next_free_field(field, field_pos + 1)
                if field_pos == -1:
                    game_end = True
                update_lcd = True

            if not lcd.key1.value():
                if current_player == 1:
                    field[field_pos] = "x"
                    player_win = check_winner(field, current_player)
                    current_player = 2
                elif current_player == 2:
                    field[field_pos] = "o"
                    player_win = check_winner(field, current_player)
                    current_player = 1
                field_pos = next_free_field(field, field_pos + 1)
                update_lcd = True

            if game_end:
                player_win = check_winner(field, 1)
                if player_win == 0:
                    player_win = check_winner(field, 2)

            # update
            if update_lcd:
                if player_win == 0 and field_pos != -1:
                    game_start = game_ttt(lcd, field, current_player, field_pos)
                else:
                    if player_win == 0 and field_pos == -1:
                        player_win = 3
                    game_start = draw_ttt_menu(lcd, player_win)
                    print(player_win)
                    print(field_pos)
                    field = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
                    current_player = 1
                    field_pos = 0

    else:
        if not lcd.key0.value():
            menu_position = menu_position - 1
            if menu_position < 1:
                menu_position = len(menu)
            redraw = True

        if not lcd.key1.value():
            menu_position = menu_position + 1
            if menu_position > len(menu):
                menu_position = 1
            redraw = True

        if not lcd.key3.value():
            in_game = menu_position
            redraw = False

    if not lcd.key2.value() and in_game > 0:
        in_game = 0
        game_start = 0
        redraw = True
        menu_position = 1

    if redraw and in_game == 0:
        draw_menu(lcd, menu, menu_position)
