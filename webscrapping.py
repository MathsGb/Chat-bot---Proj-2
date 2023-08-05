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
    url = 'http://www.uabj.ufrpe.br/br/assistência-estudantil-na-uabj'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_='field field-name-body field-type-text-with-summary field-label-hidden')
    headlines = []

    for article in articles:
        headline_element = article.find('p', class_='rtejustify')
        if headline_element is not None:
            headline = headline_element.text.strip()
            # link = 'https://www.bbc.com' + article.find('a')['href']
            # headlines.append({'headline': headline, 'link': link})

    # Send messages to Telegram channel
    message = 'Programa de bolsas: \n\n'
    message_chunks = []
    for headline in headlines:
        message_chunk = f'- {headline["headline"]}\n{headline["link"]}\n\n'
        if len(message + message_chunk) > 4000:
            message_chunks.append(message)
            message = 'Programa de bolsas (continuação):\n\n'
        message += message_chunk

    # Add the last message to the message_chunks list
    message_chunks.append(message)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    for message_chunk in message_chunks:
        await update.message.reply_text(text=message_chunk)
        # time.sleep(1)  # 3600 seconds = 1 hour

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("hello", hello))
app.run_polling()