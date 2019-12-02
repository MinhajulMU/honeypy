from telegram.ext import Updater, CommandHandler
import telegram

chat_ids = [282504451]
def start(bot, update):
    update.message.reply_text(update.message.chat.id)
    chat_id.append(update.message.chat.ids)
    update.message.reply_text("Selamat ! anda sudah terdaftar dalam bot, sekarang anda sudah mulai bisa menerima notifikasi dari kami ")


def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater('920749265:AAFVpTsf8LdsrSlXSYL8e5MymABfcFfj4KI')
  bot = telegram.Bot(token='920749265:AAFVpTsf8LdsrSlXSYL8e5MymABfcFfj4KI')

  dispatcher = updater.dispatcher
  print("Bot started")
#  print(chat_id)
  bot.send_message(282504451,'sjjjjjjjjjjjjjjjjjjjjj')
  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)
#  print(updater.get_updates())
  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()