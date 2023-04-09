import { createReadStream } from "fs";
import { OpenAIApi } from "openai";

export async function postToWhisper(openai: OpenAIApi, audioFilePath: string) {
  const transcript = await openai.createTranscription(
    createReadStream(audioFilePath) as any,
    "whisper-1"
  );
  return transcript.data.text;
}
