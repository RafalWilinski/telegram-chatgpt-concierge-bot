import dotenv from "dotenv";
dotenv.config();

import { Telegraf } from "telegraf";
import { existsSync, mkdirSync } from "fs";
import { Model as ChatWithTools } from "./models/chatWithTools";

const workDir = "./tmp";
const telegramToken = process.env.TELEGRAM_TOKEN!;

const bot = new Telegraf(telegramToken);
let model = new ChatWithTools();

if (!existsSync(workDir)) {
  mkdirSync(workDir);
}

bot.start((ctx) => {
  ctx.reply("Welcome to my Telegram bot!");
});

bot.help((ctx) => {
  ctx.reply("Send me a message and I will echo it back to you.");
});


bot.on("message", async (ctx) => {
  const text = (ctx.message as any).text;

  if (!text) {
    ctx.reply("Please send a text message.");
    return;
  }

  console.log("Input: ", text);

  await ctx.sendChatAction("typing");
  try {
    const response = await model.call(text);

    await ctx.reply(response);
  } catch (error) {
    console.log(error);

    const message = JSON.stringify(
      (error as any)?.response?.data?.error ?? "Unable to extract error"
    );

    console.log({ message });

    await ctx.reply(
      "Whoops! There was an error while talking to OpenAI. Error: " + message
    );
  }
});

bot.launch().then(() => {
  console.log("Bot launched");
});

process.on("SIGTERM", () => {
  bot.stop();
});
