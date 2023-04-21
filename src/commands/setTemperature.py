from openai import Model

def setTemperatureCommand(bot, setTemp):
    @bot.message_handler(commands=['temperature'])
    def temperature(message):
        temp = message.text.split(" ")[1]
        temperature = float(temp)
        if (temperature < 0 or temperature > 1):
            bot.reply_to(message, "Temperature must be between 0 and 1.")
            return
        setTemp(temperature)
        bot.reply_to(message, f"Temperature set to {temperature}")