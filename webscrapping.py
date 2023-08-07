import requests
from bs4 import BeautifulSoup
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
from Secrets import TOKEN

channel_id = '-1621919165'

bot = telegram.Bot(token=TOKEN)

    # Send each message chunk to the Telegram channel
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://www.prg.unicamp.br/graduacao/pad/'
    # Web scraping code
    # url = 'https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='elementor-text-editor elementor-clearfix')
    headlines = []

    for article in articles:
        headline_element = article.find('p')
        if headline_element is not None:
            headline = headline_element.text.strip()
            headlines.append({'headline': headline, })

    # Send messages to Telegram channel
    message = 'BBC News Headlines:\n\n'
    message_chunks = []
    for headline in headlines:
        # {headline["link"]}
        message_chunk = f'- {headline["headline"]}\n'
        if len(message + message_chunk) > 4000:
            message_chunks.append(message)
            message = 'BBC News Headlines (continued):\n\n'
        message += message_chunk

    # Add the last message to the message_chunks list
    message_chunks.append(message)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    # Send each message chunk to the Telegram channel
    for message_chunk in message_chunks:
        await update.message.reply_text(text=message_chunk)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("hello", hello))
app.run_polling()