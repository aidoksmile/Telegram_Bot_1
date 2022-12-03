import telebot
import model

API_TOKEN = "5951902081:AAE2LAVrSGhejcpHRDle5JXmT8yK4pD0WLs"
bot = telebot.TeleBot(API_TOKEN)
game_status = False
player = 0
sign = ['X', 'O']
n = 3
x_chat_id = ""
board = list(range(1, 10))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Сыграем в крестики-нолики?\n")
    global game_status
    global x_chat_id
    if game_status: 
        return
    board = list(range(1, 10))
    bot.send_message(message.chat.id, model.Draw_board(board))
    bot.send_message(message.chat.id, f"\nИгорки ходят по очереди в своих телеграмах.\nНапишите номер ячейки")
    game_status = True
    x_chat_id = message.chat.id

@bot.message_handler(commands=['help'])
def help_message(message):
    message_text = "Для начала игры нажмите /start\n"
    message_text += "Для вызова справки по командам нажмите /help"
    bot.send_message(message.chat.id, message_text)

@bot.message_handler()
def game_message(message):
    global game_status
    if game_status == False:
        bot.send_message(message.chat.id, "Для начала игры нажмите /start\n")
        return
    player_symbol = int(message.text)
    sign = "0"
    if message.chat.id == x_chat_id:
        sign = "X"
    input_ans = model.Player_input(board, player_symbol, sign)
    print (input_ans)
    if input_ans is not None:
        bot.send_message(message.chat.id, input_ans)
        return
    if model.Check_win(board):
        bot.send_message(message.chat.id, "Win!")
        game_status = False
        return 
    bot.send_message(message.chat.id, model.Draw_board(board))

print("Бот работает")
bot.polling()
