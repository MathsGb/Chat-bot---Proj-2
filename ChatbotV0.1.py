import telebot

def matrícula(x):
    ListaAlunos = [20210009722, 20210009703, 20210009716]
    i = 0
    while( i < len(ListaAlunos)):
        if( x ==  ListaAlunos[ i ] ):
            return True
        i += 1
    return False

def verificar(mensagem):
    return True

TOKEN = "6092476379:AAELQfPNyo8B9SasLginEuWp-_6_WdZPJow"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def Inicio(mensagem):
    text = """Sejá muito bem vindo a Lensbot

Para iniciar precisamos saber se voce está matrículado na no curso."""
    bot.send_message(mensagem.chat.id, text)
    bot.send_message(mensagem.chat.id, "Por favor digite sua matrícula ")

@bot.message_handler(commands=["menu"])
def Inicio(mensagem):
    text = """Sejá muito bem vindo a Lensbot

Sou Lenina e estou aqui para ajudar em como se comunicar com a escolaridade, no futuro.... :P

Por enquanto que tal aproveitar alguma funções?

    - Você pode ver o seu /Horario
    - Olhar o site da /UABJ
    - Entre em contato com algum dos nossos /Emails
    - Ou podemos só jogar /Jokenpo
    - Se tiver alguma dúvida dê uma olhada no nosso /FAQ

Lembre-se sempre que se sentir perdido use /menu ou /help
    
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
    bot.send_message(mensagem.chat.id, "Lembre-se se quiser recomeçar só clicar no /menu")

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

@bot.message_handler(commands=["help"])
def ajuda(mensagem):
    Text = """Não se preucupe, sempre que não souber o que fazer você pode sempre começar de novo.
Aqui está a lista de comandos úteis:
/start
/Horario
/UABJ
/Emails
"""
    bot.send_message(mensagem.chat.id, Text)

@bot.message_handler(func = lambda msg: msg.text is not None and '/' not in msg.text)
def conferir(msg):
    if(matrícula(int(msg.text)) == True):
        Text = """Bem vindo Aluno jardineiro !!!

Talvez possa gostar de dar uma olhada no nosso /menu para ver tudo que esse Bot tem a oferecer.
"""
        bot.send_message(msg.chat.id, Text)
    else: bot.send_message(msg.chat.id, "Desculpe esse Bot só está disponível para alunos UABJ")

@bot.message_handler(commands=["denovo"])
def burro(mensagem):
    text = """Voce que sabe /Jokenpo
Não há como me vencer vamos pular logo pro fim , clique /aqui"""
    bot.reply_to(mensagem, text)

@bot.message_handler(commands=["FAQ"])
def perguntas(mensagem):
    text = """Aqui estão as 10  perguntas mais frequentes:
1° Como e quando posso saber a está em período de inscrição para bolsas universitárias?

R = Acompanhe o período de inscrição para bolsas no site oficial do SigaA, basta ir na aba Bolsas > Solicitar aquisição de bolsa logo terá um um quadro com as devidas datas de início e fim. Para se informar sobre editais ou documentos necessários observe o grupo oficial daqui do telegram ou vá no nosso site oficial /UABJ que provavelmente estará lá.

2° Como posso logar na rede wifi na UABJ e na rede da AEB?
R = Ao tentar entrar na rede da UABJ vc notará que ela pede um nome de usuário assim como senha, este , portanto, varia de aluno à aluno, sendo respectivamente seu nome e senha de login no SigaA.
Já para o caso da AEB estamos com alguns problemas em estabelecer a rede no momento então a wifi "UABJ" por enquanto é apenas para funcionários. Entretanto não se estresse, estamos trabalhando veemente para conseguir estabelecer a wifi lá.
... TBC

Iremos sempre atualiza-las conforme a demanda então se a sua dúvida não está aqui tenta manda diretamente para algum e-mail oficial na barra de /Emails. Por algum motivo ache isso trabalhoso ಠಿ⁠_⁠ಠ não se preocupe, estou trabalhando para que posso enviar mensagem diretamente daqui do telegram.

Caso esteja perdido sempre pode voltar para o /menu. """
    bot.send_message(mensagem.chat.id, text)

@bot.message_handler(commands=["aqui"])
def monke(mensagem):
    bot.send_message(mensagem.chat.id, "Fale com o criador : https://github.com/MathsGb ou dê o /start")
    # bot.send_sticker(mensagem.chat.id, "https://api.telegram.org/bot<token>/sendSticker?chat_id=<id>&file_id=CAADAgADOQADfyesDlKEqOOd72VKAg")
    # "https://i.kym-cdn.com/photos/images/newsfeed/001/867/654/334.jpg"

bot.polling()