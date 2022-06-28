import logging
from TeamSubscription import TeamSubscription
from TeamSubscriptionRepository import TeamSubscriptionRepository
from TeamSubscriptionRepositoryCache import TeamSubscriptionRepositoryCache
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, ApplicationBuilder, ContextTypes, CommandHandler, InlineQueryHandler

def main():
    application = ApplicationBuilder().token('TOKEN').build()

    main_repo.setup()
    cache_repo.setup()

    start_handler = CommandHandler('r', register_team)
    get_all_handler = CommandHandler('all', get_all)
    save_handler = CommandHandler('save', save)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    
    application.add_handler(start_handler)
    application.add_handler(get_all_handler)
    application.add_handler(save_handler)
    application.add_handler(unknown_handler)
    
    application.run_polling()

main_repo = TeamSubscriptionRepository("DBName")
cache_repo = TeamSubscriptionRepositoryCache("DBName")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def register_team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = cache_repo.add_item(TeamSubscription(update.effective_chat.id, update.message.text))
    if not result:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Error occured")

async def save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = cache_repo.get_items(update.effective_chat.id)
    saved = main_repo.add_item(result)
    message = ""
    if not saved:
        message = "Error occured"
    else:
        message = "Success!"
        cache_repo.delete_item(update.effective_chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def get_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = main_repo.get_items(update.effective_chat.id)
    if not result:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Nothing saved.')
        return
    registered = [x[1] for x in result]
    teams = "\n".join(registered)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=teams)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

if __name__ == '__main__':
    main()