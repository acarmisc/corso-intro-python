from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = '379951933:AAG_NhqaTB3wk4WvWvvkVrdOs_Z7TUKLCQc'


def start(bot, update):
	update.message.reply_text("Ciao!")

def controller(bot, update):
	msg = update.message.text
	if "come stai" in msg:
		update.message.reply_text("Bene, grazie, e tu?")
	elif "bene" in msg:
		update.message.reply_text("Sono contento per te!")
	elif "male" in msg:
		update.message.reply_text("Mi spiace!")		
	else:
		update.message.reply_text("Non ho capito")				

def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler(Filters.text, controller))

	updater.start_polling()

	updater.idle()

if __name__ == '__main__':
	main()
