from time import sleep
import telepot
import os


def start(chat):
    try:
        with open("start.txt") as f:
            dat = []
            data1 = ""
            dat = f.readlines()
            for x in dat:
                data1 += x
            bot.sendMessage(chat, data1)
    except:
        bot.sendMessage(chat, "Error occurred will start data is uploading")


def find_file(in_file):
    file_list = []
    with open("file_list.txt") as f:
        data = f.readlines()
        for x in data:
            if x[-1] == "\n":
                new_x = x[:-1]
            else:
                new_x = x
            file_list.append(new_x)
    if "/" + in_file in file_list:
        return True
    else:
        return False


def add_file_to_list(file_name):
    if file_name:
        with open("file_list.txt", "a+") as f:
            f.write("/" + file_name + "\n")
            bot.sendMessage(1314922309, f"{file_name} is add to file List\n To Enter details \nclick on /file_details")


def file_data(file, chat):
    if find_file(file):
        file_link = file + ".txt"
        try:
            with open(file_link) as f:
                data = []
                data1 = ""
                data = f.readlines()
                for x in data:
                    data1 += x
                bot.sendMessage(chat_id, data1)
        except:
            bot.sendMessage(chat, f"Error will sending the {file} file data\nTry again or Report to owner /report")


def delete_file(file_delete, chat):
    file_delete_data = file_delete[1:]
    delete_address = "C:/Users/HI/Desktop/Telegram_BOT/" + file_delete_data + ".txt"
    print(delete_address)
    if os.path.exists(delete_address):
        if file_delete_data == "start" or file_delete_data == "file_list" or file_delete_data == "edit" or file_delete_data == "about":
            bot.sendMessage(chat, f"That file '{file_delete_data}' can't be deleted ")
        else:
            os.remove(delete_address)
            bot.sendMessage(chat, f"{file_delete_data} as been deleted")
            file_list = []
            with open("file_list.txt") as f:
                for x in f:
                    if x[1:] == file_delete_data + "\n" or x[1:] == file_delete_data:
                        pass
                    elif x == " ":
                        pass
                    else:
                        file_list.append(x)
            with open("file_list.txt", "w+") as f:
                for z in file_list:
                    f.write(z)
                bot.sendMessage(chat, f"{file_delete_data} as been removed from file list.\n...Updated")

    else:
        bot.sendMessage(chat, f"The file '{file_delete_data}' does not exist (or) File is already deleted")


def edit():
    total_data = ''
    try:
        with open("edit.txt") as f:
            data = f.readlines()
            for x in data:
                print(x)
                total_data += x
            bot.sendMessage(chat_id, total_data)
    except:
        bot.sendMessage(chat_id, "Edit oppositions are not Loading...")


def about():
    about_data = ''
    try:
        with open("about.txt") as f:
            data = f.readlines()
            for x in data:
                print(x)
                about_data += x
            bot.sendMessage(chat_id, about_data)
    except:
        bot.sendMessage(chat_id, "About Section Is Not Found")


def new_chit_id(chat):
    chat_id_data = []
    with open("chat_id.txt") as f:
        data = f.readlines()
        for x in data:
            if x[-1] == "\n":
                new_x = x[:-1]
            else:
                new_x = x
            chat_id_data.append(new_x)
    if str(chat) in chat_id_data:
        pass
    else:
        with open("chat_id.txt", "a+") as f:
            f.write(str(chat) + "\n")
            bot.sendMessage(chat, "Thanks for joining with us")
            bot.sendMessage(1314922309, f"New Member : {chat}")


def leave_bot(chat):
    leave_list = []
    with open("chat_id.txt") as f:
        for x in f:
            if x == str(chat) + "\n" or x == str(chat):
                pass
            elif x == " ":
                pass
            else:
                leave_list.append(x)
    with open("chat_id.txt", "w+") as f:
        for z in leave_list:
            f.write(z)
        bot.sendMessage(chat, f"{chat} as been removed from Bot channel.\n...Updated")
        bot.sendMessage(1314922309, f"Member lost : {chat}")


def send_file():
    pass


def m_file(chat):
    total_files = ''
    try:
        with open("file_list.txt") as f:
            data = f.readlines()
            for x in data:
                print(x)
                total_files += x
            bot.sendMessage(chat, total_files)
    except:
        bot.sendMessage(chat, "No files in Bot")


def handle(msg):
    global message
    global chat_id
    global new_file

    chat_id = msg['chat']['id']
    message = msg['text'].lower()
    print("Message received from " + str(chat_id))

    if message[0] == '/':
        message = message[1:]
    if message == "start":
        start(chat_id)
        new_chit_id(chat_id)
    elif find_file(message):
        file_data(message, chat_id)
    elif message == "movies" or message == "file" or message == "files":
        m_file(chat_id)
    elif message == "about":
        about()
    elif message == "report":
        bot.sendMessage(chat_id, "To leave bot channel\n/leave_bot\nOther /other_message ")
    elif message[:13] == "other_message":
        bot.sendMessage(1314922309, str(chat_id) + " : \n" + message[13:])
        bot.sendMessage(chat_id, "Message as been send to owner")
    elif message[:6] == "delete":
        if chat_id == 1314922309:
            delete_file(message[6:], chat_id)
        else:
            bot.sendMessage(chat_id, f"You are not Owner to delete '{message[6:]}' File.")
    elif message == "edit":
        edit()
    elif message == "token":
        bot.sendMessage(chat_id, f"Your Telegram chat id : {chat_id}.")
    elif message[:4] == "name":
        if chat_id == 1314922309:
            new_file = message[5:] + ".txt"
            with open(new_file, "w") as f:
                bot.sendMessage(chat_id, f"new file name {message[4:]} is created")
            add_file_to_list(message[5:])
        else:
            bot.sendMessage(chat_id, f"You are not Owner to Create '{message[4:]}' File.")
    elif message[:12] == "file_details":
        if chat_id == 1314922309:
            with open(new_file, "a+") as file:
                file.write(message[13:])
                bot.sendMessage(chat_id, f"new file data \n\n'''{message[13:]}''' \n.....is stored")
            bot.sendMessage(chat_id, "storing process is completed")
            send_file()
        else:
            bot.sendMessage(chat_id, f"You are not Owner to write '{message[13:]}' in File.")

    elif message == "leave_bot":
        leave_bot(chat_id)
    else:
        bot.sendMessage(chat_id, f"{message} is not found.")



bot = telepot.Bot("5159467417:AAHDLTWAUJ9JmCKkYslmhpVmrThfMiuDIOM")
bot.message_loop(handle)
bot.sendMessage(1314922309, "Telegram bot is ready")

while True:
    sleep(10)

