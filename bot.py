import telebot;
bot = telebot.TeleBot('1888931316:AAGpqnyk1bE_Wh-ksj8W1eiGMxPpdeMm0ag');

#Пытаемся сделать, чтобы бот понимал голос, импортируем библиотеки

import requests
#для обработки HTTP запросов
import speech_recognition
#распознование голоса
import os
#для работы с файловой системой
import pydub
#для обработки oga файлов (так как тг использует oga, а не wav)
from pydub import AudioSegment
AudioSegment.converter = os.getcwd() + "C:\Users\crzho\Desktop\ffmpeg-4.0.2-win32-static\bin\ffmpeg.exe"
AudioSegment.ffmpeg = os.getcwd() + "C:\Users\crzho\Desktop\ffmpeg-4.0.2-win32-static\bin\ffmpeg.exe"
AudioSegment.ffprobe = os.getcwd() + "C:\Users\crzho\Desktop\ffmpeg-4.0.2-win32-static\bin\ffmpeg.exe"
#скачал ffmpeg для конвертации oga в wav, так как pyttsx3 понимает только wav

## import pyttsx3
#для отправления на сервера тг голосовых файлов
## tts = pyttsx3
## voices = tts.getProperty('voices')

#Пытаюсь выбрать голос, но почему-то не выдаёт список голосов, не очень понимаю как это сделать


#Приветствие бота
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Здравствуйте":
        bot.send_message(message.from_user.id, "Здравствуйте! Я страховой консультант Мила, и сейчас я помогу разобраться Вам с любым интересующим Вас вопросом!")
    elif message.text == "/help":
            bot.send_message(message.from_user.id, "Чтобы задать вопрос боту, сначала поприветствуйте его словом Здравствуйте")
    else:
                bot.send_message(message.from_user.id, "Я Вас не поняла. Напишите /help.")
bot.polling(none_stop=True, interval=0)