# Telegram ChatGPT Concierge Bot (+ Voice!)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/e7XF13?referralCode=eZ-TPi)

![Telegram ChatGPT Concierge Bot](./img/demo.png)

This is a Telegram bot that uses:

- OpenAI's ChatGPT, obviously, as "the brain"
- [LangchainJS](https://github.com/hwchase17/langchainjs) to constructs prompts, handle convo history and interact with Google
- OpenAI's Whisper API to generate text from voice
- [Play.ht](https://play.ht) to generate voice from text and reply to voice messages

### How to use

> Prerequisite: You need Node 18, a Telegram bot token and an OpenAI API key with access to GPT-4. Optionally you can use other model by setting `OPENAI_MODEL` env var. Ask ChatGPT how to get these. You'll also need `ffmpeg` installed to use voice interactions.

1. `git clone https://github.com/RafalWilinski/telegram-chatgpt-concierge-bot`
2. `cd telegram-chatgpt-concierge-bot`
3. `touch .env` and fill the following:

```
TELEGRAM_TOKEN=
OPENAI_API_KEY=
PLAY_HT_SECRET_KEY=
PLAY_HT_USER_ID=
PLAY_HT_VOICE= # check docs for available voices https://playht.github.io/api-docs-generator/#utra-realistic-voices
AZURE_SPEECH_KEY= # Optionally, you can use azure's tts service, check docs to get speech_key、speech_region、voice_agent. https://azure.microsoft.com/en-us/products/cognitive-services/text-to-speech/ 
AZURE_SPEECH_REGION= # eg, eastus
AZURE_VOICE_AGENT= # eg, en-US-AnaNeural
OPENAI_MODEL=gpt-3.5-turbo # only if you don't have access to GPT-4
#SERVE_THIS_USER_ONLY=99999999 # uncomment this if you want to only serve this user id. The ID will be printed on stdout.
```

4. `npm install`
5. `npm start`

### Consulting

I, @RafalWilinski (creator of this repo), offer consulting. If you are interested on hiring weekly hours with me on a retainer, feel free to email me at raf.wilinski@gmail.com

---

Follow me on [Twitter](https://twitter.com/RafalWilinski)

Discuss on [Twitter](https://twitter.com/rafalwilinski/status/1645123663514009601) or [HackerNews](https://news.ycombinator.com/item?id=35510516)

Sponsored by [ChatWithCloud](https://chatwithcloud.ai)
