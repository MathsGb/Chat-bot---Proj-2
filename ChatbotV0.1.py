
from asyncio import wait
import telebot

TOKEN = "6092476379:AAELQfPNyo8B9SasLginEuWp-_6_WdZPJow"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def Inicio(mensagem):
    text = """
    Sejá muito bem vindo a Lensbot

    Sou Lenina e estou aqui para ajudar em como se comunicar com a escolaridade, no futuro.... :P

    Por enquanto que tal aproveitar alguma funções?
    Voçe pode ver o seu /horario

    """
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=["horario"])
def Curso(mensagem):
    text = """Qual o seu curso na UABJ?

/Computacao
/Automacao
/Quimica
/Hidrica
    """
    bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Computacao", "Automacao", "Quimica", "Hidrica"])
def resposta(mensagem):
    bot.send_message(mensagem.chat.id, "https://drive.google.com/file/d/1NxgAicFzdM_369I5u6ExakDXoe_Luyit/view?usp=sharing")

def verificar(mensagem):
    return True

@bot.message_handler(func= verificar)
def Falhou(mensagem):
    text = """ Esse comando não existe, por favor insirá um comando válido ou dê /start denovo.
    Se quiser sair desse loop clique /aqui"""
    
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=["aqui"])
def monke(mensagem):
    bot.send_photo(mensagem.chat.id, "https://i.kym-cdn.com/photos/images/newsfeed/001/867/654/334.jpg")

@bot.message_handler(commands=[""])
def 

bot.polling()