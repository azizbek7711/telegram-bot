from telegram.ext import Updater, CommandHandler
from telegram import  ReplyKeyboardMarkup, KeyboardButton


def start_command(update, context):
    print(update.message)
    print(context)
    update.message.reply_text(text=f"siz/start camndasini kiridiz")
    context.bot.send_message(chat_id="742070367", text="salom bu men!!!")


def show_menu(update,context):
    buttons=[
        [KeyboardButton(text="Menu 1"), KeyboardButton(text="Menu 2")],
        [KeyboardButton(text="Menu 3"), KeyboardButton(text="Menu 4")],
    ]
    print(update.message)
    print(context)
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(battons)
    )



def main():
    updater = Updater("5190341058:AAGNPKNKL7N9JC7eRJgnWsNRRt0z4WkaqEg")  #tokan

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))

    updater.start_polling()
    updater.idle()


if __name__=='__main__':
   main()


   #5190341058:AAGNPKNKL7N9JC7eRJgnWsNRRt0z4WkaqEg