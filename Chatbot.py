import telebot
import requests, urllib
from Secrets import TOKEN
from Texts import Start_txt, email_text, Menu_text, Curso_text, help_Text, devs_text, periodos_text, Offline_text
from utils import deleta_arquivos, cria_diretorio
from unidecode import unidecode

bot = telebot.TeleBot(TOKEN)

Totoro = bot.get_sticker_set("Totoro")

@bot.message_handler(commands=["start"])
def Inicio(mensagem):
	bot.set_chat_menu_button()
	bot.send_message(mensagem.chat.id, Start_txt)
	bot.send_sticker(mensagem.chat.id, Totoro.stickers[4].file_id)

@bot.message_handler(commands=["menu"])
def Inicio(msg):
	bot.send_message(msg.chat.id, Menu_text)

@bot.message_handler(commands=["horario"])
def Curso(msg):
	bot.send_message(msg.chat.id, Curso_text)

@bot.message_handler(commands=["computacao", "automacao", "quimica", "hidrica"])
def resposta(msg):
	try:
		cria_diretorio('./temp')
	except FileExistsError:
		deleta_arquivos('./temp')

	if msg.text == '/computacao':
		curso = 'eng_computacao'
	elif msg.text == "/automacao":
		curso = 'eng_controle_automacao'
	elif msg.text == "/quimica":
		curso = 'eng_quimica'
	elif msg.text == "/hidrica":
		curso = 'eng_hidrica'
	
	with open("./temp/curso.txt", "w") as arquivo:
		arquivo.write(curso)

	bot.send_message(msg.chat.id, periodos_text)


@bot.message_handler(commands=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
def periodo(msg):
	curso = None
	periodo = None

	for char in msg.text:
		try:
			periodo = int(char)
		except ValueError:
			pass

	with open("./temp/curso.txt", "r") as arquivo:
		curso = arquivo.read()
	
	try:
		arquivo = f'horario_{curso}_{periodo}_periodo.png'
		url = 'https://equipi.pythonanywhere.com//arquivos/' + arquivo
		image = open('./temp/horario.png','wb')
		image.write(urllib.request.urlopen(url).read())
		image.close()

		url_api = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={msg.chat.id}'
		img = open('./temp/horario.png', 'rb')
		requests.post(url_api, files={'photo': img})

		bot.send_message(msg.chat.id, "Aqui está seu horário, se quiser pode voltar ao /menu")

	except Exception as error:
		bot.send_sticker(msg.chat.id, Totoro.stickers[12].file_id)
		bot.send_message(msg.chat.id, "Houve um erro ao tentar baixar seu horário se quiser pode voltar ao /menu")


@bot.message_handler(commands=["UABJ"])
def site(msg):
	bot.send_photo(msg.chat.id, "https://www.bj1.com.br/wp-content/uploads/2022/03/UABJ.jpeg")
	bot.send_message(msg.chat.id, "http://www.uabj.ufrpe.br")
	bot.send_message(msg.chat.id, "Lembre-se se quiser recomeçar só clicar no /menu")


@bot.message_handler(commands=["emails"])
def atalho(msg):
	bot.send_message(msg.chat.id, email_text)
	bot.send_message(msg.chat.id, "Lembre-se se quiser recomeçar só clicar no /menu")

@bot.message_handler(commands=["help"])
def ajuda(msg):
	bot.send_message(msg.chat.id, help_Text)

@bot.message_handler(commands=["devs"])
def dev(msg):
	bot.send_message(msg.chat.id, devs_text)

# ==== Busca no banco de dados ====

@bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
def conferir(msg):
	try:
		resposta = requests.request("GET", ("https://equipi.pythonanywhere.com/" + unidecode(msg.text)))
		bot.send_message(msg.chat.id, resposta)

	except requests.exceptions.ConnectionError:
		bot.send_sticker(msg.chat.id, Totoro.stickers[12].file_id)
		bot.send_message(msg.chat.id, Offline_text)

# ==== Sugestão de perguntas ====

@bot.message_handler(commands=["Sugestao"])
def enviar_sugestao(mensagem):
    faq_link = "https://equipi.pythonanywhere.com/index_aluno"  
    bot.send_message(mensagem.chat.id, f"Para enviar uma sugestão, acesse o FAQ através deste link: {faq_link}")
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser voltar, é só clicar no /menu")

#=========== Bot start ==========

bot.polling()