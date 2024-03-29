from typing import Final

#pip install requests & pip install aiohttp
import requests
import aiohttp

# pip install python-telegram-bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print('Starting up bot...')

TOKEN: Final = "6140132163:AAGhUy8C9tj8afJfkbkbgjFWUyZiw9MMYGk"
BOT_USERNAME: Final = '@LNU_Coffee_Bot'
base_url = 'http://localhost:1880'


# /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')
    
# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the channel
    /help -> This message
    /reg -> start coffee machine and keep warm for 2 hours
    /brew -> Start coffee machine
    /warm, -> Keep warm for 1 hour
     """)
    
# /help command
async def reg_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f'{base_url}/brewing/start'
    print('Before request')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=3) as response:
            if response.status == 200:
                await update.message.reply_text('Request sent successfully')
            else:
                await update.message.reply_text('Error sending request')
    print('After request')

async def brew_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("brew")

async def warm_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("warm")




def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I\'m good!'

    if 'i love python' in processed:
        return 'Remember to subscribe!'

    return 'I don\'t understand'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # We don't want the bot respond if it's not mentioned in the group
    else:
        response: str = handle_response(text)

    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('reg', reg_command))
    app.add_handler(CommandHandler('brew', brew_command))
    app.add_handler(CommandHandler('warm', warm_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=1)
