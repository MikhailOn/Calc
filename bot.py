import telebot;
bot = telebot.TeleBot('1888931316:AAFhXxxjITM0jU1oPnj5EZbU4Bc7DNk--Oc');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Здравствуйте":
        bot.send_message(message.from_user.id, "Здравствуйте! Я страховой консультант Мила, и сейчас я помогу разобраться Вам с любым интересующим Вас вопросом!")
    elif message.text == "/help":
            bot.send_message(message.from_user.id, "Чтобы задать вопрос боту, сначала поприветствуйте его словом Здравствуйте")
    else:
                bot.send_message(message.from_user.id, "Я Вас не поняла. Напишите /help.")
bot.polling(none_stop=True, interval=0)

#Проверил бот, на слово "Здравствуйте" реагирует. Дальше в планах обучить бота давать инфу о некоторых страховых продуктах. Добавить кнопки на каждый и вывыодить список часто задаваемых вопросов и ответов на них. Но так как идея была в голосовм помощнике, попробую сделать, чтобы он реалигровал на голос...