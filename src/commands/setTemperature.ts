import { Telegraf } from "telegraf";
import { Model } from "openai";

export async function setTemperatureCommand(
  bot: Telegraf,
  setTemp: (temp: number) => void
) {
  bot.command("temperature", (ctx) => {
    const text = (ctx.message as any).text;
    const temp = text.split(" ")[1];
    const temperature = parseFloat(temp);

    if (isNaN(temperature)) {
      ctx.reply("Please enter a valid number.");
      return;
    }
    if (temperature < 0 || temperature > 1) {
      ctx.reply("Temperature must be between 0 and 1.");
      return;
    }

    setTemp(temperature);
    ctx.reply(`Temperature set to ${temperature}`);
  });
}
