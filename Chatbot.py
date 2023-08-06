import telebot
from Metodos import Start_txt, email_text, Menu_text, FAQ_text, base_Text, Curso_text, help_Text

TOKEN = "6092476379:AAELQfPNyo8B9SasLginEuWp-_6_WdZPJow"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def Inicio(mensagem):
    bot.send_message(mensagem.chat.id, Start_txt)
    bot.send_message(mensagem.chat.id, "Por favor digite sua matrícula ")

@bot.message_handler(commands=["menu"])
def Inicio(mensagem):
    bot.send_message(mensagem.chat.id, Menu_text)

@bot.message_handler(commands=["Horario"])
def Curso(mensagem):
    bot.send_message(mensagem.chat.id, Curso_text)


@bot.message_handler(commands=["Computacao", "Automacao", "Quimica", "Hidrica"])
def resposta(mensagem):
    bot.send_message(mensagem.chat.id, "https://drive.google.com/file/d/1NxgAicFzdM_369I5u6ExakDXoe_Luyit/view?usp=sharing")
    bot.send_message(mensagem.chat.id, "É só baixar, se quiser pode voltar ao /menu")

@bot.message_handler(commands=["UABJ"])
def site(mensagem):
    bot.send_photo(mensagem.chat.id, "https://www.bj1.com.br/wp-content/uploads/2022/03/UABJ.jpeg")
    bot.send_message(mensagem.chat.id, "http://www.uabj.ufrpe.br")
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /menu")

@bot.message_handler(commands=["Emails"])
def atalho(mensagem):
    bot.send_message(mensagem.chat.id, email_text)
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /start")

@bot.message_handler(commands=["help"])
def ajuda(mensagem):
    bot.send_message(mensagem.chat.id, help_Text)

@bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
def conferir(msg):
    bot.send_message(msg.chat.id, base_Text)



@bot.message_handler(commands=["FAQ"])
def perguntas(mensagem):
    bot.send_message(mensagem.chat.id, FAQ_text)

@bot.message_handler(commands=["aqui"])
def dev(mensagem):
    bot.send_message(mensagem.chat.id, "Fale com o bot manager : https://github.com/MathsGb ou volte para o /menu")
    
bot.polling()