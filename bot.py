
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
#скачал ffmpeg для конвертации oga в wav, так как pyttsx3 понимает только wav
#однако, выдаёт ошибку RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)
#перерыл кучу форумов по этому вопросу - ничего не помогло

import pyttsx3
#cинтез речи, пишем код, чтобы голосовой помощник перекидывал нас на сайт компании
start = pyttsx3.init()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("скажи что-нибудь")
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

while True:
    request(listen())

#Приветствие бота
import telebot
@bot.message_handler (content_types=['text'])
def get_text_messages(message):
    if message.text == "Здравствуйте":
        bot.send_message(message.from_user.id, "Здравствуйте! Я страховой консультант Мила, и сейчас я помогу разобраться Вам с любым интересующим Вас вопросом!")
    elif message.text == "/help":
            bot.send_message(message.from_user.id, "Чтобы задать вопрос боту, сначала поприветствуйте его словом Здравствуйте")
    else:
                bot.send_message(message.from_user.id, "Я Вас не поняла. Напишите /help.")
bot.polling(none_stop=True, interval=0);


#результат - голосовой помощник перекидывает на сайт, но только, если запускать программу с компа - как интегрировать это все в телеграмм пока непонятно.