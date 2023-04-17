import { AudioConfig, SpeechConfig, SpeechSynthesizer, ResultReason } from 'microsoft-cognitiveservices-speech-sdk';

const atSpeechKey = process.env.AZURE_SPEECH_KEY;
const atRegion = process.env.AZURE_SPEECH_REGION;
const atVoiceAgent = process.env.AZURE_VOICE_AGENT;

if (typeof atSpeechKey !== 'string' || typeof atRegion !== 'string' || typeof atVoiceAgent !== 'string') {
  throw new Error('Azure TTS Subscription credentials not set.');
}

const AudioPath = './tmp/azure-tts.wav';
const speechConfig = SpeechConfig.fromSubscription(atSpeechKey, atRegion);
speechConfig.speechSynthesisVoiceName = atVoiceAgent;

export async function textToSpeech(text: string) {
  // Create the speech synthesizer.
  const audioConfig = AudioConfig.fromAudioFileOutput(AudioPath);
  let synthesizer = new SpeechSynthesizer(speechConfig, audioConfig);

  await new Promise<void>(async (resolve, reject) => {
    synthesizer.speakTextAsync(
      text,
      function (result) {
        if (result.reason === ResultReason.SynthesizingAudioCompleted) {
          resolve();
        } else {
          reject();
          console.error(
            'Speech synthesis canceled, ' +
              result.errorDetails +
              '\nDid you set the speech resource key and region values?'
          );
        }
        synthesizer.close();
      },
      function (err) {
        reject(err);
        console.trace('err - ' + err);
        synthesizer.close();
      }
    );
  });
  return AudioPath;
}
