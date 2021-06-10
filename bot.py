
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
#ffmpeg для конвертации oga в wav, так как pyttsx3 понимает только wav, а тг oga

import pyttsx3
#cинтез речи, пишем код, чтобы голосовой помощник перекидывал нас на сайт компании
start = pyttsx3.init()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Здравствуйте, я голосвой помощник Ингосстраха Мила. Что Вас интересует? Назовите страховой продукт или скажите САЙТ для перехода на сайт компании. Кроме того, я могу рассказать об истории компании (ИСТОРИЯ), о руководителях (РУКОВОДСТВО), покажу, где ближайший офис (ОФИС). Если вы вип клиент, скажите ВИП. Если Вас интересуют новости компании, скажите НОВОСТИ. Если вы хотите позвонить на линию службы поддержки, я подскажу Вам номер - скажите ТЕЛЕФОН. Если хотите стать партнёром, скажите ПАРТНЁР")
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
    if "партнёр" in task:
        text = "эта информация для вас"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/partners/', new=2)
    if "новости" in task:
        text = "открываю новости"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/company/news/', new=2)
    if "вип" in task:
        text = "Эта информация для вас"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.exclusive.ingos.ru/', new=2)
    if "телефон" in task:
        text = "8(495) 956 - 55 - 55"
        start.say(text)
        start.runAndWait()
    if "офис" in task:
        text = "показываю ближайшие офисы"
        start.say(text)
        start.runAndWait()
        webbrowser.open('https://www.ingos.ru/office/', new=2)
    if "руководство" in task:
        text = "с 1 февраля 2021 года гендиректор «Ингосстраха» Андрей Ларкин, прежде занимавший пост исполнительного вице-президента ПАО Вымпелком. "
        start.say(text)
        start.runAndWait()
    if "история" in task:
        text = "«Ингосстрах» — правопреемник Главного управления иностранного страхования СССР, созданного 16 ноября 1947 года. В 1972 году преобразовано в акционерное общество со 100%-м госкапиталом, в 1992 году приватизировано. Первые дочерние зарубежные компании были созданы в Лондоне в 1924 году — Блекбалси (прекратила работу в 2003 году) и в Гамбурге в 1927 году — СОФАГ (в 2016 году была продана страховой компании СОГАЗ)."
        start.say(text)
        start.runAndWait()
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
            bot.send_message(message.from_user.id, "На данный момент я могу: перевести на сайт компании, рассказать про автострахование, рассказать про страхование жизни, рассказать про страхование путешествующих, рассказать про страхование имущества, рассказать про пенсию и инвестиции, показать каталог страховых продуктов")
    else:
                bot.send_message(message.from_user.id, "Я Вас не поняла. Напишите /help.")
bot.polling(none_stop=True, interval=0);


#не получилось интегрировать в тг, поэтому получился просто голосовой помощник, способный поболтать о страховании и рассказать о продуктах "ингосстраха".