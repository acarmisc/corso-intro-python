from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = '379951933:AAG_NhqaTB3wk4WvWvvkVrdOs_Z7TUKLCQc'
messages = list()

def start(bot, update):
	update.message.reply_text("Ciao!")

def controller(bot, update):
	messages.append(update.message)
	msg = update.message.text
	response = "Risposta per %s" % msg
	messages.append(response)
	update.message.reply_text(response)
	import pdb; pdb.set_trace()					

def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler(Filters.text, controller))

	updater.start_polling()

	updater.idle()

if __name__ == '__main__':
	main()
