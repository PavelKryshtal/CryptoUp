import telebot

token = '5572018108:AAGMogFFGc-lUM1wGggzOJ7vvsXGVK3VFVg'
bot = telebot.TeleBot(token)
chat_id = '@Cardano0321_bot'
text = 'Hello python'
bot.send_message(chat_id, text)
print(chat_id)