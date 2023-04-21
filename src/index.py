from dotenv import load_dotenv
from telegraf import Telegraf
from lib.downloadVoiceFile import downloadVoiceFile
from lib.postToWhisper import postToWhisper
from lib.htApi import textToSpeech
from lib.chat import ChatWithTools
from pathlib import Path
from io import BytesIO

load_dotenv()

workDir = "./tmp"

telegram_token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(telegram_token, parse_mode=None)
model = ChatWithTools()

if not os.path.exists(work_dir):
    os.makedirs(work_dir)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to my Telegram bot!")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Send me a message and I will echo it back to you.')

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    voice = message.voice
    bot.send_chat_action(message.chat.id, 'typing')

    try:
        local_file_path = download_voice_file(work_dir, voice.file_id, bot)
    except Exception as e:
        print(e)
        bot.reply_to(
            message,
            'Whoops! There was an error while downloading the voice file. Maybe ffmpeg is not installed?'
        )
        return

    transcription = post_to_whisper(model.openai, local_file_path)

    bot.reply_to(message, f'Transcription: {transcription}')
    bot.send_chat_action(message.chat.id, 'typing')

    try:
        response = model.call(transcription)
    except Exception as e:
        print(e)
        bot.reply_to(
            message,
            'Whoops! There was an error while talking to OpenAI. See logs for details.'
        )
        return

    print(response)

    bot.reply_to(message, response)
print("Bot launched")

def signal_handler(signal, frame):
    bot.stop()
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
