from time import sleep
import datetime
import telepot

def handle(msg):
    
    # now = datetime.datetime.now()  # Getting date and time
    chat_id = msg['chat']['id']  # Receiving the message from telegram
    command = msg['text']  # Getting text from the message
    if command[0] == '/':
        command = command[1:]
    command_link = command+".txt.txt"
    if command == 'start':
        
        bot.sendMessage(chat_id, 'jsnd,fsnda,k')

    else:
        bot.sendMessage(chat_id, f"Thanks for joining with us")
    print(chat_id)
# Insert your telegram token below
bot = telepot.Bot("5560402365:AAG_FKCA_N_tF-WRw5PM1vfOkDREVZ4esSk")
bot.message_loop(handle)

while True:
    sleep(10)


