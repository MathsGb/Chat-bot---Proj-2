from asyncio import wait
import telebot

TOKEN = "6092476379:AAELQfPNyo8B9SasLginEuWp-_6_WdZPJow"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def Inicio(mensagem):
    text = """Sejá muito bem vindo a Lensbot

Sou Lenina e estou aqui para ajudar em como se comunicar com a escolaridade, no futuro.... :P

Diga vc é um Aluno? /sim ou /nao

Por enquanto que tal aproveitar alguma funções?

    - Você pode ver o seu /Horario
    - Olhar o site da /UABJ
    - Entre em contato com algum dos nossos /Emails
    - Ou podemos só jogar /Jokenpo
    
    Diga vc é um Aluno? /sim ou /nao
    """

    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=["Horario"])
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
    bot.send_message(mensagem.chat.id, "É só baixar, se quiser pode voltar ao /start")

@bot.message_handler(commands=["UABJ"])
def site(mensagem):
    bot.send_photo(mensagem.chat.id, "https://www.bj1.com.br/wp-content/uploads/2022/03/UABJ.jpeg")
    bot.send_message(mensagem.chat.id, "http://www.uabj.ufrpe.br")
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /start")

@bot.message_handler(commands=["Emails"])
def atalho(mensagem):
    text = """Emails para caso queira entrar em contato:

MAYLA STELLA DO NASCIMENTO FERREIRA
Assistente Social
Contato: servicosocial.uabj@ufrpe.br

EVERSON DOS SANTOS MELO
 Psicólogo
 Contato: psicologiauabj@ufrpe.br

ROSANA MARIA DOS SANTOS
 Assistente em Administração
 Contato: admnaps.uabj@ufrpe.br
    """

    bot.send_message(mensagem.chat.id, text)
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /start")

@bot.message_handler(commands=["Jokenpo"])
def jogo(mensagem):
    text = """ Qual voce escolhe?

/Pedra
/Papel
/Tesoura
    """
    bot.send_message(mensagem.chat.id,text)

@bot.message_handler(commands=["Pedra"])
def venci(mensagem):
    text = """Eu escolhi Papel UWU
kkkkkkk não pense que pode vencer, quer ir /denovo ?"""
    bot.reply_to(mensagem, text)

@bot.message_handler(commands=["Papel"])
def venci(mensagem):
    text = """Eu escolhi Tesoura UWU
kkkkkkk não pense que pode vencer, quer ir /denovo ?"""
    bot.reply_to(mensagem, text)

@bot.message_handler(commands=["Tesoura"])
def venci(mensagem):
    text = """Eu escolhi Pedra UWU
kkkkkkk não pense que pode vencer, quer ir /denovo ?"""
    bot.reply_to(mensagem, text)

def matricula():
    
    return True
    

@bot.message_handler(commands=["sim"])
def aluno(msg):
    @bot.send_message(msg.chat.id, "Qual o sua matrícula?")

# @bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
# def resposta(msg):
#     if msg.text == "Hi":
#         bot.send_message(msg.chat.id,"Hello!")

@bot.message_handler(commands=["denovo"])
def burro(mensagem):
    text = """Voce que sabe /Jokenpo
Não há como me vencer vamos pular logo pro fim , clique /aqui"""
    bot.reply_to(mensagem, text)

@bot.message_handler(commands=["aqui"])
def monke(mensagem):
    bot.send_message(mensagem.chat.id, "Fale com o criador : https://github.com/MathsGb ou dê o /start")
    # bot.send_sticker(mensagem.chat.id, "https://api.telegram.org/bot<token>/sendSticker?chat_id=<id>&file_id=CAADAgADOQADfyesDlKEqOOd72VKAg")
    # "https://i.kym-cdn.com/photos/images/newsfeed/001/867/654/334.jpg"

def verificar(mensagem):
    return True

@bot.message_handler(func= verificar)
def Falhou(mensagem):
    text = """ Esse comando não existe, por favor insirá um comando válido ou dê /start denovo.
    Se quiser sair desse loop clique /aqui"""
    bot.send_photo(mensagem.chat.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmDxngEbCHtfceQvXnZ-mYH2iUU5b3JRd9sw&usqp=CAU")
    bot.send_message(mensagem.chat.id, text)

bot.polling()