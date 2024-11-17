from flask import Flask, request
from flask import send_file
from TTS.api import TTS
from dotenv import load_dotenv
import os, sys

def load_model():
    TTS_MODEL = os.getenv("TTS_MODEL")

    available_models = ['tts_models/multilingual/multi-dataset/xtts_v2', 'tts_models/multilingual/multi-dataset/xtts_v1.1', 'tts_models/multilingual/multi-dataset/your_tts']

    if not TTS_MODEL or TTS_MODEL == '':
        print("=====================")
        print('ERROR: Couldn\'t find TTS_MODEL in .env file.' )
        print('Available models:')
        print('\n'.join(available_models))
        print("=====================")
        return 
    elif TTS_MODEL not in available_models:
        print("=====================")
        print('ERROR: TTS_MODEL is not correct.')
        print('Available models:')
        print('\n'.join(available_models))
        print("=====================")
        return
    else:
        print("=====================")
        print("Loading TTS model: " + TTS_MODEL)
        print("=====================\n")
        tts = TTS(TTS_MODEL, gpu=True) 
        print("\n=====================")
        print("Model loaded.")
        print("=====================")
        return tts

load_dotenv()
tts = load_model()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'
  
@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/tts_to_audio/', methods=['POST'])
def generate():
    text = request.json['text']
    speaker = request.json['speaker_wav']

    tts.tts_to_file(text=text, file_path="../output/output.wav", speaker_wav=f"../speakers/{speaker}.wav", language="en")

    return send_file("../output/output.wav", as_attachment=True)

if tts and __name__== '__main__':
    app.run()