
import telebot
bot = telebot.TeleBot('1888931316:AAGpqnyk1bE_Wh-ksj8W1eiGMxPpdeMm0ag');

#Пытаемся сделать, чтобы бот понимал голос, импортируем библиотеки
import requests
#для обработки HTTP запросов
import webbrowser
#для открытия ссылок
import speech_recognition as sr
#распознование голоса
import os
#для работы с файловой системой
import pydub
#для обработки oga файлов (так как тг использует oga, а не wav)

from pydub import AudioSegment
AudioSegment.converter = os.getcwd() + "C:\\Users\\crzho\\Desktop\\CALCULATOR\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = os.getcwd() + "C:\\Users\\crzho\\Desktop\\CALCULATOR\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = os.getcwd() + "C:\\Users\\crzho\\Desktop\\CALCULATOR\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"
#ffmpeg для конвертации oga в wav, так как pyttsx3 понимает только wav

import pyttsx3
#cинтез речи, пишем код, чтобы голосовой помощник перекидывал нас на сайт компании
start = pyttsx3.init()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Что Вас интересует?")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            task = r.recognize_google(audio, language="ru-RU").lower()
            print(task)
        except:
            task = listen()
        return task

def request(task):
    if "сайт" in task:
        text = "открываю сайт нашей компании"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://ingos.ru', new=2)
    if "страхование жизни" in task:
        text = "перевожу в раздел страхования жизни"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/health_life/', new=2)
    if "автострахование" in task:
        text = "перевожу в раздел автострахования"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/auto/', new=2)
    if "страхование путешествующих" in task:
        text = "перевожу в раздел страхования путешествующих"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/travel/', new=2)
    if "страхование имущества" in task:
        text = "перевожу в раздел страхования имущества"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/property/', new=2)
    if "пенсия и инвестиции" in task:
        text = "перевожу в раздел пенсия и инвестиции"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/pension_investment/', new=2)
    if "каталог страховых продуктов" in task:
        text = "перевожу в каталог"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/ishop/', new=2)

while True:
    request(listen())

#Приветствие бота
import telebot
@bot.message_handler (content_types=['text'])
def get_text_messages(message):
    if message.text == "Здравствуйте":
        bot.send_message(message.from_user.id, "Здравствуйте! Я страховой консультант Мила, и сейчас я помогу разобраться Вам с любым интересующим Вас вопросом!")
    elif message.text == "/help":
            bot.send_message(message.from_user.id, "Чтобы задать вопрос боту, сначала поприветствуйте его словом Здравствуйте. Что Вас интересует: сайт, автострахование, страхование жизни,страхование путешествующих, страхование имущества, пенсия и инвестиции, страхование жизни и здоровья, каталог страховых продуктов? Скажите голосом.")
    else:
                bot.send_message(message.from_user.id, "Я Вас не поняла. Напишите /help.")
bot.polling(none_stop=True, interval=0);


#результат - перекидывает в любой раздел, если запускаю с компа и говорю в микрофон. не понимаю как интегрировать это в тг, чтобы это там работало.