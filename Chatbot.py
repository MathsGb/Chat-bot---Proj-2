import telebot

import requests, urllib
from bs4 import BeautifulSoup
from Secrets import TOKEN
from Metodos import Start_txt, email_text, Menu_text, FAQ_text, base_Text, Curso_text, help_Text, devs_text, periodos_text
from utils import deleta_arquivos, cria_diretorio


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def Inicio(mensagem):
	bot.set_chat_menu_button()
	bot.send_message(mensagem.chat.id, Start_txt)

@bot.message_handler(commands=["menu"])
def Inicio(mensagem):
	bot.send_message(mensagem.chat.id, Menu_text)

@bot.message_handler(commands=["horario"])
def Curso(mensagem):
	bot.send_message(mensagem.chat.id, Curso_text)

@bot.message_handler(commands=["computacao", "automacao", "quimica", "hidrica"])
def resposta(mensagem):
	try:
		cria_diretorio('./temp')
	except FileExistsError:
		deleta_arquivos('./temp')

	if mensagem.text == '/computacao':
		curso = 'eng_computacao'
	elif mensagem.text == "/automacao":
		curso = 'eng_controle_automacao'
	elif mensagem.text == "/quimica":
		curso = 'eng_quimica'
	elif mensagem.text == "/hidrica":
		curso = 'eng_hidrica'
	
	with open("./temp/curso.txt", "w") as arquivo:
		arquivo.write(curso)

	bot.send_message(mensagem.chat.id, periodos_text)


@bot.message_handler(commands=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
def periodo(mensagem):
	curso = None
	periodo = None

	for char in mensagem.text:
		try:
			periodo = int(char)
		except ValueError:
			pass

	with open("./temp/curso.txt", "r") as arquivo:
		curso = arquivo.read()
	
	try:
		arquivo = f'horario_{curso}_{periodo}_periodo.png'
		url = 'http://127.0.0.1:5000/arquivos/' + arquivo
		image = open('./temp/horario.png','wb')
		image.write(urllib.request.urlopen(url).read())
		image.close()

		url_api = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={mensagem.chat.id}'
		img = open('./temp/horario.png', 'rb')
		requests.post(url_api, files={'photo': img})

		# bot.send_message(mensagem.chat.id, url)
		bot.send_message(mensagem.chat.id, "Aqui está seu horário, se quiser pode voltar ao /menu")

	except Exception as error:
		bot.send_message(mensagem.chat.id, "Houve um erro ao tentar baixar seu horário :( se quiser pode voltar ao /menu")


@bot.message_handler(commands=["UABJ"])
def site(mensagem):
	bot.send_photo(mensagem.chat.id, "https://www.bj1.com.br/wp-content/uploads/2022/03/UABJ.jpeg")
	bot.send_message(mensagem.chat.id, "http://www.uabj.ufrpe.br")
	bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /menu")

@bot.message_handler(commands=["emails"])
def atalho(mensagem):
	bot.send_message(mensagem.chat.id, email_text)
	bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /start")

@bot.message_handler(commands=["help"])
def ajuda(mensagem):
	bot.send_message(mensagem.chat.id, help_Text)


@bot.message_handler(commands=["FAQ"])
def perguntas(mensagem):
	bot.send_message(mensagem.chat.id, FAQ_text)

@bot.message_handler(commands=["devs"])
def dev(mensagem):
	bot.send_message(mensagem.chat.id, devs_text)

# ================================== teste tratamento com webscrapping ==================================

@bot.message_handler(commands=['bolsas'])
def webtal(msg):
	url = 'https://www.prg.unicamp.br/graduacao/pad/'

	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	articles = soup.find_all('div', class_='elementor-text-editor elementor-clearfix')
	headlines = []

	for article in articles:
		headline_element = article.find('p')   # Selecionando cada elemento <p> naquela div
		if headline_element is not None:
			headline = headline_element.text.strip() + "\n"
			headlines.append({'headline': headline, })

	message = 'Essas são as ultimas informações que se tem sobre bolsas no nosso site:\n\n'
	message_chunks = []
	for headline in headlines:

		message_chunk = f'- {headline["headline"]}\n'
		if len(message + message_chunk) > 4000:    #tratamento para textos que excedam o limite de characteres do telegram
			message_chunks.append(message)
			message = 'informações sobre bolsas (continuação):\n\n'
		message += message_chunk

	message_chunks.append(message)
	for message_chunk in message_chunks:
		text = f'{message_chunk }'
		bot.send_message(msg.chat.id, text)

# =================================== Interação com site ===================================================

@bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
def conferir(msg):
	resposta = requests.request("GET", ("http://127.0.0.1:5000/" + msg.text))
	bot.send_message(msg.chat.id, resposta)


#======================================== Bot start =========================================================

bot.polling()