from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import requests
import json
import os, time
from google.cloud import storage
from google.cloud import bigquery


def main():
    SetLogLevel(0)
    FRAME_RATE = 16000
    CHANNELS = 1

    model = Model("vosk-model-kz-0.15")
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    start = time.time()
    mp3 = AudioSegment.from_mp3('audios/qalan30_20.mp3')
    mp3 = mp3.set_channels(CHANNELS)
    mp3 = mp3.set_frame_rate(FRAME_RATE)

    rec.AcceptWaveform(mp3.raw_data)
    result = rec.Result()
    text = json.loads(result)["text"]
    print(text)
    with open('/texts/text.txt', 'w', encoding='utf-8') as file:
        file.writelines(text)
    print("{:.3f} seconds".format(time.time() - start))

if __name__ == '__main__':
    main()
