from dotenv import load_dotenv
import telebot
from lib.chat import ChatWithTools
from pathlib import Path
from io import BytesIO
import os

load_dotenv()
work_dir = "./tmp"

if "TELEGRAM_TOKEN" not in os.environ or "TELEGRAM_TOKEN" not in os.environ:
    raise AssertionError("Please configure TELEGRAN_TOKEN as environment variables or in .env file")

telegram_token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(telegram_token, parse_mode=None)

model = ChatWithTools()

if not os.path.exists(work_dir):
    os.makedirs(work_dir)

@bot.message_handler(commands=['start'])
def start(client, message):
    message.reply_text("Hello! I'm a bot that can talk to the AI. Send me a message!")

@bot.on_message(commands=['stop'])
def stop(client, message):
    message.reply_text("Stopping...")
    bot.stop()

@bot.on_message(commands=['help'])
def help(client, message):
    message.reply_text("Send me a message and I'll give it to the AI!")

@bot.on_message(commands=["status"])
def status(client, message):
    message.reply_text("I'm running!")

@bot.on_message(commands=["ping"])
def ping(client, message):
    message.reply_text("Pong!")

@bot.message_handler(func=lambda message: True)
def chat(message):
    if not message.text:
        bot.reply_to(message, "Please send a text message.")
        return

    print("Input: ", message.text)

    message.reply_chat_action("typing")
    try:
        response = model.call(message.text)

        message.reply_text(response)
    except Exception as error:
        print(error)

        bot.reply_to(message,"Whoops! There was an error while talking to OpenAI. Error: " + str(error))

bot.infinity_polling()