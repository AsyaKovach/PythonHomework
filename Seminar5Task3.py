#Создайте программу для игры в ""Крестики-нолики"".

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")

def take_input(gamer_token):
    valid = False
    while not valid:
        gamer_answer = input("Куда поставим " + gamer_token+"? ")
        try:
            gamer_answer = int(gamer_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if gamer_answer >= 1 and gamer_answer <= 9:
            if (str(board[gamer_answer-1]) not in "XO"):
                board[gamer_answer-1] = gamer_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

board = list(range(1,10))
main(board)