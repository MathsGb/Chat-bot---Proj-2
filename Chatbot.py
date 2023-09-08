import telebot
import requests, urllib
from bs4 import BeautifulSoup
from Secrets import TOKEN
from Texts import Start_txt, email_text, Menu_text, Curso_text, help_Text, devs_text, periodos_text, Offline_text
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

		url_api = f'http://127.0.0.1:5000/bot{TOKEN}/sendPhoto?chat_id={mensagem.chat.id}'
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


@bot.message_handler(commands=["devs"])
def dev(mensagem):
	bot.send_message(mensagem.chat.id, devs_text)

# ==== Busca no banco de dados ====

@bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
def conferir(msg):
	try:
		resposta = requests.request("GET", ("http://127.0.0.1:5000/" + msg.text))
		bot.send_message(msg.chat.id, resposta)

	except requests.exceptions.ConnectionError:
		Set = bot.get_sticker_set("Totoro")
		bot.send_sticker(msg.chat.id, Set.stickers[0].file_id)
		bot.send_message(msg.chat.id, Offline_text)

# ==== Sugestão de perguntas ====

@bot.message_handler(commands=["Sugestao"])
def enviar_sugestao(mensagem):
    faq_link = "http://127.0.0.1:5000/index_aluno"  # Substitua pelo endereço correto do FAQ
    bot.send_message(mensagem.chat.id, f"Para enviar uma sugestão, acesse o FAQ através deste link: {faq_link}")
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser voltar, é só clicar no /menu")

#=========== Bot start ==========

bot.polling()