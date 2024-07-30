from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def reply(update, context):
    await update.message.reply_text("Hello there!")

async def options(update, context):
    keyboard = [
    [InlineKeyboardButton("Option 1", callback_data='1')],
    [InlineKeyboardButton("Option 2", callback_data='2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please choose:', reply_markup=reply_markup)

async def button(update, context):
    query = update.callback_query
    await query.answer()
    choise = query.data
    if choise == '1':
        await query.edit_message_text(text="You have selected option 1")
    elif choise == '2':
        await query.edit_message_text(text="You have selected option 2")
        
def main():
    """
    Handles the initial launch of the program (entry point).
    """
    token = "7096397068:AAFkXwYJS_3WJcMNGLUwjvLkdh94KkiMFn0"
    application = Application.builder().token(token).concurrent_updates(True).read_timeout(30).write_timeout(30).build()
    application.add_handler(CommandHandler("hello", reply))
    application.add_handler(CommandHandler("options",options)) # new command handler here
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Telegram Bot started!", flush=True)
    application.run_polling()

if __name__ == '__main__':
    
    main()